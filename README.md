# photo-sharing-app

This repository contains the source code for a full-stack photo-sharing app built with Django on the backend and Bootstrap on the frontend.

**Features:**

* CRUD (Create, Read, Update, Delete) functionality for photos
* User management system with account creation, photo upload, viewing other users' photos, and editing/deleting personal photos
* Simple web interface built with Bootstrap

**Note:** This is not a social network and does not include the complexities associated with platforms like Instagram or Twitter.

**Tech Stack:**

* Backend:
    * Django: Core framework for handling URLs, logic, user authentication, and database operations
    * Django-taggit: Enables a simple tagging system for photos
    * Pillow: Provides image manipulation capabilities
    * Django-crispy-forms: Simplifies displaying Bootstrap forms
* Frontend:
    * Django templates: Dynamically display data in HTML files
    * Bootstrap 5: Framework for web design

**Installation:**

See individual documentation for each technology used for installation instructions.

**Usage:**

1. Clone the repository:

```
git clone https://github.com/your-username/photo-sharing-app.git
```

2. Set up the development environment:
    * Install Python and required libraries (refer to Django documentation)
    * Create a virtual environment
    * Activate the virtual environment

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Apply database migrations:

```
python manage.py migrate
```

5. Create a superuser account (optional, for administrative access):

```
python manage.py createsuperuser
```

6. Run the development server:

```
python manage.py runserver
```

**Contributing:**

We welcome contributions to this project. Please refer to the CONTRIBUTING.md file for guidelines.

**License:**

This project is licensed under the MIT License (see LICENSE.md).

**Disclaimer:**

This is a basic example showcasing concepts and does not guarantee production-ready quality or security. 