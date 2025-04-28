# Bug Tracking System

A lightweight yet powerful web-based bug tracking system built with React.js and Django.

## Overview

This bug tracking system helps development teams track and manage software defects efficiently. The application provides user authentication, issue reporting, and comprehensive defect management capabilities through an intuitive interface.

## Features

- **User Authentication**: Secure login/registration system with token-based authentication
- **Bug Management**: Create, update, and manage bug reports with priority levels and status tracking
- **Project Organization**: Group bugs by projects for better organization
- **Collaboration Tools**: Comment system and file attachments for team communication
- **Responsive Design**: Clean, intuitive interface that works across devices

## Technologies Used

### Frontend
- React.js
- React Router DOM
- Formik & Yup (form handling and validation)
- Axios (API requests)
- Bootstrap (styling)

### Backend
- Django
- Django REST Framework
- Django CORS Headers
- Token Authentication

### Database
- SQLite (development)
- PostgreSQL (recommended for production)

## Installation

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bug-tracking-system.git
   cd bug-tracking-system
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install django djangorestframework django-cors-headers
   ```

4. Navigate to the Django project:
   ```
   cd bugtracker
   ```

5. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd bug-tracker-frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

## Usage

1. Access the frontend at `http://localhost:3000`
2. Login with your credentials or register a new account
3. Create projects and start reporting bugs
4. Assign bugs to team members, track progress, and collaborate through comments

## API Endpoints

### Authentication
- POST `/api/auth/register/` - Register a new user
- POST `/api/auth/login/` - Login and receive token
- POST `/api/auth/logout/` - Logout and invalidate token

### Projects
- GET `/api/projects/` - List all projects
- POST `/api/projects/` - Create a new project
- GET `/api/projects/:id/` - Retrieve a specific project
- PUT `/api/projects/:id/` - Update a project
- DELETE `/api/projects/:id/` - Delete a project

### Bugs
- GET `/api/bugs/` - List all bugs
- POST `/api/bugs/` - Create a new bug
- GET `/api/bugs/:id/` - Retrieve a specific bug
- PUT `/api/bugs/:id/` - Update a bug
- DELETE `/api/bugs/:id/` - Delete a bug

### Comments and Attachments
- POST `/api/comments/` - Add a comment to a bug
- POST `/api/attachments/` - Add an attachment to a bug

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
