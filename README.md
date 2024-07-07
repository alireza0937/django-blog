# Django Project

This is a Django project that includes user authentication, blog functionality, and a commenting system.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [APIs](#apis)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000/admin/` to access the Django admin interface.
- Visit `http://127.0.0.1:8000/` to see the blog homepage.
- Use the registration, login, and profile features to manage user accounts.

## Docker Setup

1. **Ensure you have Docker and Docker Compose installed**. If not, you can download them from the official Docker [website](https://www.docker.com/products/docker-desktop).

2. **Build and run the containers**:

    ```sh
    docker-compose up --build
    ```

    This command will build the Docker images and start the containers as defined in your `docker-compose.yml` file.

3. **Apply migrations**:

    Once the containers are up and running, open a new terminal and run:

    ```sh
    docker-compose exec django python manage.py migrate
    ```

4. **Create a superuser**:

    ```sh
    docker-compose exec django python manage.py createsuperuser
    ```

5. **Access the application**:

    - The web application will be accessible at `http://localhost:8000/`.
    - The admin interface will be accessible at `http://localhost:8000/admin/`.

## APIs

For detailed information about the available APIs, refer to the [APIs documentation](apis.md).

## Project Structure

- **users**: Handles user registration, login, logout, and profile management.
- **blog**: Manages blog posts, including creating, updating, and deleting posts.
- **comment**: Handles creating comments on blog posts.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
