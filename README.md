# README.md

## Django REST API for 5-Minutes Per Day Plan

This project is a backend implementation using Django and Django REST Framework to serve data for a 5-minute per day plan. It is designed to be consumed by a mobile application or a website.

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd django_rest_api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

### Populating Data
Since this project does not include any templates, we must populate the models with initial data using Django's shell or the Django Admin panel.

1. Open Django shell:
   ```sh
   python manage.py shell
   ```
2. Run the following commands to create categories and activities:
   ```python
   from tracker.models import Category, Activity
   athletics = Category.objects.create(name="Athleticism")
   boosters = Category.objects.create(name="Boosters")
   Activity.objects.create(category=athletics, name="Advanced Mobility Exercises", frequency="Maximize", duration=60)
   Activity.objects.create(category=boosters, name="Knowledge Boosters", frequency="2x/Day", duration=30)
   ```
3. Exit the shell using `exit()`.

### API Endpoints
The API exposes the following endpoints:
- `GET /api/categories/` - Retrieve all categories
- `GET /api/activities/` - Retrieve all activities
- `GET /api/daywise-activities/` - Retrieve day-wise activities
- `POST /api/daywise-activities/` - Mark an activity as complete (requires authentication)

### Frontend Integration
Since this is only a backend implementation, a UI framework (like React or Vue) must be used to display the data.

---
