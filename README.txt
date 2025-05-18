📱 TASHA – Informal Service Provider Platform

TASHA is a mobile and web-based platform that connects informal service providers with customers in real time. It provides:

    ✅ Verified profiles and ratings

    💳 Secure digital payments

    📅 Job tracking and scheduling

    ☎️ USSD/SMS onboarding support for feature phone users

🔧 Project Structure

tasha/
├── accounts/               # Custom user app (if used)
├── services/               # Core app for service provider features
├── tasha/                  # Project settings
├── db.sqlite3              # SQLite database (dev only)
├── manage.py               # Django management script
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS)
└── README.md               # This file

🚀 Getting Started (Local Development)
🔁 Prerequisites

    Python 3.8+

    pip

    Virtual environment (recommended)

    Git

📥 Step 1: Clone the Repository

git clone https://github.com/your-username/tasha.git
cd tasha

📦 Step 2: Create Virtual Environment and Install Dependencies

python -m venv env
source env/bin/activate      # On Windows use: env\Scripts\activate
pip install -r requirements.txt

If requirements.txt doesn't exist, generate it after installation:

pip freeze > requirements.txt

🛠 Step 3: Database Setup

python manage.py makemigrations
python manage.py migrate

👤 Step 4: Create Superuser

python manage.py createsuperuser

Then log in at: http://127.0.0.1:8000/admin
▶️ Step 5: Run Development Server

python manage.py runserver

Visit: http://127.0.0.1:8000
🧩 Key Features
✅ Service Provider Registration

    User account links to a ServiceProvider profile

    Providers have location, service type, contact, and bio

💼 Admin Panel

Manage:

    Users

    Service Providers

    Future features (Bookings, Payments, Ratings)

🌐 Deployment Guide (e.g., Heroku or Render)

    Update settings in tasha/settings.py:

        Add ALLOWED_HOSTS

        Set DEBUG = False

        Configure static files and media handling

    Use Gunicorn and Whitenoise (for production):

pip install gunicorn whitenoise

Prepare files:

    Procfile

    runtime.txt (optional for Heroku)

    requirements.txt

Run collectstatic:

    python manage.py collectstatic

🛡 Security Notes

    Make sure to use environment variables for secret keys in production

    Enable CSRF and HTTPS in deployment

    Monitor user-submitted data for abuse

✨ Upcoming Features

    📞 Booking & contact system between users and providers

    📍 Map/location services

    💬 Customer reviews & provider ratings

    💰 Integration with mobile money or Paystack

    📲 USSD & SMS registration support

🤝 Contributing

    Fork this repo

    Create a feature branch (git checkout -b feature/your-feature)

    Commit changes

    Push and create a Pull Request

📄 License

MIT License