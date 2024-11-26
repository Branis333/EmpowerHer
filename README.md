EmpowerHer

EmpowerHer is an online platform dedicated to empowering African women by providing a space to share experiences, access resources, and engage in meaningful discussions on topics like women’s rights, leadership, mental health, and entrepreneurship. This project is built using Django and aims to foster a supportive and informative community.

Features

Blog System: Users can create, read, update, and comment on blog posts.

User Authentication: Secure login, registration, and profile management.

Categories and Tags: Blog posts can be organized by categories and tags.

Responsive Design: Optimized for both desktop and mobile devices.

Admin Panel: Manage posts, comments, and users efficiently.

Requirements

Prerequisites

Python 3.8+

pip (Python package manager)

SQLite or PostgreSQL (for production)

Node.js and npm (optional for advanced front-end setup)

Python Dependencies

Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt

Project Setup

1. Clone the Repository

git clone https://github.com/your-username/EmpowerHer.git
cd EmpowerHer/django_project2

2. Set Up Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Run the Development Server

python manage.py runserver

Access the app at http://127.0.0.1:8000/.
