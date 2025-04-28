# GolfNow — A Simple Way to Book Local Tee Times

GolfNow is a web app built to make it easier for golfers to find and book tee times at rural and local golf courses.  
It’s designed to help small clubs connect with players who might not otherwise find them online.

This project was created as part of my capstone to apply what I’ve learned in backend development, database management, and frontend design.

---

## Tech Stack

- Django 5.2 (Python Web Framework)
- SQLite (Lightweight Database)
- HTML/CSS (Frontend Design)
- Git & GitHub (Version Control)
- ScreenRec (For Presentation Recording)

---

## Main Features

- Create an account or continue as a guest
- Browse local golf courses with images and details
- Search for courses by name
- View course-specific detail pages
- Book tee times with confirmation codes
- Profile page to view and cancel bookings
- Clean, user-friendly design

---

## How to Run It Locally

### Prerequisites

- Python 3.10+
- Django 5.2
- Git installed

### Steps

1. Clone the repo:
   git clone https://github.com/Ad0ss/Golfnow-Application.git

2. Move into the project directory:
   cd golfnow_project

3. Install Django if needed:
   pip install django

4. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

6. Open your browser and go to:
   http://127.0.0.1:8000/
