TASHA - Informal Services Marketplace

HOW TO RUN LOCALLY:
--------------------
1. Create a virtual environment and activate it:
   python -m venv env
   source env/bin/activate (Linux/macOS) or env\Scripts\activate (Windows)

2. Install Django:
   pip install django

3. Navigate to the project folder and run:
   python manage.py migrate
   python manage.py runserver

4. Visit http://127.0.0.1:8000/ in your browser.

TO DEPLOY ONLINE:
--------------------
- Use platforms like Heroku, Railway, or PythonAnywhere.
- Set DEBUG=False and configure ALLOWED_HOSTS.
- Add production database and static file configurations.
- Ensure secret key and database credentials are secured using environment variables.
