# Task-manager
learning Django step by step (project 1)


📋 Task Manager - Django  Application
Task Manager is a full-stack web application designed for efficient personal task management. It features a modern frontend built with React and a robust backend powered by Django REST Framework, complete with a secure JWT (JSON Web Token) authentication system. Users can register, log in, create, view, update, and delete their personal tasks in a secure environment.

✨ Key Features
🔐 Secure Authentication: User registration and login using JWT.

👤 Data Isolation: Each user can only view and manage their own tasks.

✅ Full Task Management: Create, Read, Update, and Delete tasks (Complete CRUD operations).

🎯 Interactive User Interface: Frontend built with React for a smooth user experience.

📱 Responsive Design: The application works on various screen sizes.

🔒 Secure Sessions: Logout functionality with token blacklisting.

🏗️ Tech Stack
Backend
Python 3.8+

Django 5.2 & Django REST Framework

Simple JWT for authentication

SQLite (default database for development)

Frontend
React 19

React Router DOM for navigation

Axios for HTTP requests

Context API for global user state management

🚀 Quick Start
Follow these steps to run the project on your local machine.

Prerequisites
Python 3.8 or later

Node.js 18 or later and npm

Git

Installation & Setup
1. Clone the Repository
bash
git clone https://github.com/waadbakhash/Task-manager.git
cd Task-manager
1. Set Up & Run the Backend (Django)
bash
# Navigate to the backend directory
cd backend

# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server (will run on port 8000)
python manage.py runserver
The backend server will now be running at: http://localhost:8000

3. Set Up & Run the Frontend (React)
bash
# Open a new terminal and navigate to the frontend directory
cd frontend

# Install required dependencies
npm install

# Run the React development server
npm start
The frontend application will now be running at: http://localhost:3000

🗄️ API Endpoints (Backend)
The API provides the following endpoints:

Method	Endpoint	Description	Auth Required
POST	/api/register/	Register a new user	❌
POST	/api/login/	Login to obtain tokens	❌
POST	/api/logout/	Logout (blacklist refresh token)	✅
GET	/api/profile/	View user profile data	✅
GET	/api/tasks/	List all tasks for the logged-in user	✅
POST	/api/tasks/	Create a new task	✅
GET	/api/tasks/{id}/	Retrieve details of a specific task	✅
PUT	/api/tasks/{id}/	Fully update a specific task	✅
PATCH	/api/tasks/{id}/	Partially update a specific task	✅
DELETE	/api/tasks/{id}/	Delete a specific task	✅
Note: The access token should be included in the request header as: Authorization: Bearer {your_access_token}.

📁 Project Structure
text
Task-manager/
├── backend/                 # Django project
│   ├── tasks/              # Main Django app
│   │   ├── models.py       # Task model definition
│   │   ├── serializers.py  # DRF serializers
│   │   ├── views.py        # API views and logic
│   │   └── urls.py         # App URL routing
│   ├── task_manager/       # Django project settings
│   ├── manage.py
│   └── requirements.txt    # Python dependencies
└── frontend/               # React application
    ├── public/
    ├── src/
    │   ├── components/     # Reusable UI components
    │   ├── context/        # React Context for auth state
    │   ├── pages/          # Main pages (Login, Register, Dashboard)
    │   └── App.js          # Main app component
    └── package.json        # Node.js dependencies
🧪 Running Tests
To run the backend tests:

bash
cd backend
python manage.py test
🤝 Contributing
Contributions are welcome! To suggest improvements or add new features, please follow these steps:

Fork the project.

Create a new branch for your feature (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add: Some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request to merge your changes.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

