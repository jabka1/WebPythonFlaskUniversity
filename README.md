# WebPythonFlaskUniversity

### Overview:
These are university laboratory works on Python web programming using the Flask framework. The project encompasses essential features such as user authentication, JWT token generation, database models, RESTful API endpoints, and various views for efficiently managing tasks, posts, and user accounts.

### Project: https://github.com/jabka1/SocialNetworkExampleFlask

### Features:
1. **User Authentication:**
   - Registration and login functionality with hashed password storage.
   - User profile management with options to update username, email, password, and profile picture.

2. **JWT Token Generation:**
   - JWT (JSON Web Token) generation for secure user authentication.
   - API endpoints protected with JWT authentication.

3. **Todo Management:**
   - Create, edit, and delete tasks (todos) with a user-specific view.
   - RESTful API endpoints for managing todos, including listing, adding, editing, and deleting tasks.

4. **Post Management:**
   - Create, edit, and delete posts with different types (News, Publication, Other) and associated categories and tags.
   - User-specific view for managing posts.
   - Public view for listing all posts with pagination.
   - RESTful API endpoints for managing posts, including listing, adding, editing, and deleting posts.

5. **API Users:**
   - RESTful API endpoints for managing user resources, including listing, adding, updating, and deleting users.

6. **Customizable Configuration:**
   - Configuration options for different environments (development, testing, production).
   - Easily extendable for additional features and customization.

### Setup Instructions:
1. Clone the repository: `git clone https://github.com/jabka1/WebPythonFlaskUniversity`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Go to the laboratory work `cd lab<labNum>`
6. Run the application: `python app.py`
7. Access the application in your browser at `http://localhost:5000`

### Usage:
- Visit the registration page to create a new account.
- Log in using your credentials.
- Explore the various features such as managing todos, creating posts, updating your profile, and more.
- Access the provided RESTful API endpoints for additional functionality.

### Customization:
- The file `app/config.py` contains various configurations for running.

### Testing:
- Pytest is available at the command `pytest tests/`.
- Pytest with the percentage of code that has been tested is available at the command `pytest --cov=app tests/`
- Testing of TODO operations with Unit tests is available with the command `python -m unittest app/test_app`
