# 🐾 Animal Shelter Foundation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-brightgreen.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-✓-blue.svg)](https://www.docker.com/)

A comprehensive web platform for the Animal Shelter Foundation, facilitating animal adoptions, donations, volunteer management, and community engagement.

## 🌟 Features

- **Animal Adoption**

   - Browse adoptable animals with detailed profiles
   - Search and filter animals by species, breed, age, and more
   - Online application system for potential adopters

- **Donation System**

   - One-time and recurring donation options
   - Secure payment processing
   - Donation tracking and receipts

- **Volunteer Management**

   - Volunteer registration and scheduling
   - Event participation tracking
   - Volunteer hour logging

- **Events & Blog**

   - Upcoming adoption events and fundraisers
   - Educational blog posts about animal care
   - Newsletter subscription

- **User Authentication**

   - Secure user registration and login
   - Profile management
   - Adoption application tracking

## 🛠️ Tech Stack

- **Backend**: Django 5.0
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (Production: PostgreSQL/MySQL ready)
- **Web Server**: Nginx
- **Application Server**: Gunicorn
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions (optional)

## 🏗️ Project Structure

```ini
animal_shelter_foundation/
├── core/                  # Django project settings
├── home/                  # Homepage app
├── adopt/                 # Animal adoption system
├── donate/                # Donation processing
├── volunteer/             # Volunteer management
├── about/                 # About us pages
├── events/                # Events and blog
├── contact/               # Contact form and information
├── users/                 # User authentication
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded files
├── templates/             # Base templates
├── .env.example           # Environment variables template
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Docker configuration
└── requirements.txt       # Python dependencies

```

## 🚀 Local Development Setup

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Git
- Docker & Docker Compose (for containerized development)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/animal-shelter-foundation.git
cd animal-shelter-foundation

```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

```

3. **Install dependencies**

```bash
pip install -r requirements.txt

```

4. **Set up environment variables**

```bash
cp .env.example .env

```

Edit `.env` with your configuration.

5. **Run migrations**

```bash
python manage.py migrate

```

6. **Create a superuser**

```bash
python manage.py createsuperuser

```

7. **Run the development server**

```bash
python manage.py runserver

```

8. **Access the admin panel**
   Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## 🐳 Docker Setup (Production)

1. **Build and start containers**

```bash
docker-compose up --build -d

```

2. **Run migrations**

```bash
docker-compose exec web python manage.py migrate

```

3. **Create superuser**

```bash
docker-compose exec web python manage.py createsuperuser

```

4. **Collect static files**

```bash
docker-compose exec web python manage.py collectstatic --noinput

```

The application will be available at `http://localhost`

## ⚙️ Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Static and Media
STATIC_URL=/static/
MEDIA_URL=/media/
STATIC_ROOT=/app/staticfiles
MEDIA_ROOT=/app/media

# Email (configure for production)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=webmaster@animalshelter.org

# Security (set to True in production)
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False

```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Running Tests

```bash
python manage.py test

```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap 5](https://getbootstrap.com/) - Frontend framework
- [Docker](https://www.docker.com/) - Containerization
- All contributors who have helped with the project

---

Developed with ❤️ for the Animal Shelter Foundation
