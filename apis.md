# APIs Documentation

## Root Directory `urls.py`

| URL Pattern                          | View                                                        | Template                           | Name                     | Method      | Description                            |
|--------------------------------------|-------------------------------------------------------------|------------------------------------|--------------------------|-------------|----------------------------------------|
| `/admin/`                            | `admin.site.urls`                                           | -                                  | -                        | GET         | Django Admin Interface                 |
| `/login/`                            | `auth_views.LoginView.as_view(template_name='users/login.html')` | `users/login.html`                 | `login`                  | GET, POST   | User login                            |
| `/logout/`                           | `auth_views.LogoutView.as_view(template_name='users/logout.html')` | `users/logout.html`                | `logout`                 | GET         | User logout                           |
| `/password-reset/`                   | `CustomPasswordResetView.as_view(template_name='users/password_reset.html')` | `users/password_reset.html`        | `password-reset`         | GET, POST   | Initiate password reset (handled by Celery)               |
| `/password-reset/done`               | `auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')` | `users/password_reset_done.html`   | `password_reset_done`    | GET         | Password reset email sent confirmation |
| `/password-reset-confirm/<uidb64>/<token>/` | `auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html')` | `users/password_reset_confirm.html`| `password_reset_confirm` | GET, POST   | Confirm password reset token          |
| `/password-reset-complete/`          | `auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html')` | `users/password_reset_complete.html`| -                       | GET         | Password reset complete               |
| `/`                                  | `include('blog.urls')`                                      | -                                  | -                        | -           | Blog app URLs                         |
| `/`                                  | `include('users.urls')`                                     | -                                  | -                        | -           | Users app URLs                        |
| `/comment/`                          | `include('comment.urls')`                                   | -                                  | -                        | -           | Comment app URLs                      |

## Comment App `urls.py`

| URL Pattern                          | View                           | Name                | Method      | Description           |
|--------------------------------------|--------------------------------|---------------------|-------------|-----------------------|
| `/comment/<int:pk>`                  | `views.CommentCreateView.as_view()` | `create-comment`    | GET, POST   | Create a comment      |

## Blog App `urls.py`

| URL Pattern                          | View                           | Name                     | Method      | Description                   |
|--------------------------------------|--------------------------------|--------------------------|-------------|-------------------------------|
| `/`                                  | `views.PostListView.as_view()` | `blog-home`              | GET         | List all blog posts           |
| `/post/<int:pk>`                     | `views.PostDetailView.as_view()`| `post-detail`            | GET         | View a single post            |
| `/post/new`                          | `views.PostCreateView.as_view()`| `post-create`            | GET, POST   | Create a new post             |
| `/post/<int:pk>/update`              | `views.PostUpdateView.as_view()`| `post-update`            | GET, POST   | Update an existing post       |
| `/post/<int:pk>/delete`              | `views.PostDeleteView.as_view()`| `post-delete`            | POST        | Delete an existing post       |
| `/post/<str:username>`               | `views.SingleUserAllPosts.as_view()`| `single-user-all-posts` | GET         | View all posts by a user      |
| `/about`                             | `views.about`                  | `blog-about`             | GET         | About page                    |

## Users App `urls.py`

| URL Pattern                          | View                           | Name                | Method      | Description           |
|--------------------------------------|--------------------------------|---------------------|-------------|-----------------------|
| `/register/`                         | `views.register`               | `register`          | GET, POST   | User registration     |
| `/profile/`                          | `views.profile`                | `profile`           | GET, POST   | User profile          |
