from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext_lazy as _
from .tasks import send_password_reset_email
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        associated_users = User.objects.filter(email=email)
        if associated_users.exists():
            for user in associated_users:
                send_password_reset_email.delay(user.id)
                return render(self.request, "users/password_reset_done.html")
        return render(self.request, "users/wrong_email.html")
