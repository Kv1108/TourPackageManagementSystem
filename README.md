# Tour Package Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

A complete tour package management system with admin panel and user interface.

## Features
- Admin can create/manage tour packages
- Day-wise itinerary management
- Responsive frontend design
- Image upload support

## Installation
1. Clone repository:
   ```bash
   git clone https://github.com/Kv1108/TourPackageManagementSystem.git
   cd TourPackageManagementSystem
   ```
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create admin user:
   ```bash
   python manage.py createsuperuser
   ```
6. Run server:
   ```bash
   python manage.py runserver
   ```
