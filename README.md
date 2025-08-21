# My Study Desk

A Django-based web application that helps students manage their studies efficiently.

## Features
- Manage notes, to-do list (add, update, delete)
- Track homework (completed / pending)
- Search YouTube videos
- Search articles in wikipedia
- Browse study-related books
- Dictionary & conversion utilities
- User authentication (register, login, logout)

## Installation

1. Clone this repository
   ```bash
   git clone https://github.com/sindhusai04/mystudydesk.git
   cd mystudydesk

## Setup
1. Create virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Run migrations
   ```bash
   python manage.py migrate

4. Run the Server
   ```bash
   python manage.py runserver

## Use
Open the browser and visit: http://127.0.0.1:8000/

Access the admin panel: http://127.0.0.1:8000/admin/

## TECH Stack
- Django 5.2
- Bootstrap (for UI)
- Python 3.x
