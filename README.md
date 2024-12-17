

Labelbox Web App 

Labelbox is a web application that enables efficient and scalable data annotation tasks, specifically for image annotation. The project is designed to ensure that all annotation projects/tasks are stored in a database, and that annotated data is processed and stored without any dependency on local device storage. 

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Description

Labelbox Web App allows users to annotate images for data analysis tasks. This system is designed to:
- Store annotation projects/tasks in a database.
- Fetch images for annotation from the database.
- Output annotated data into a database without storing or downloading any data on the user’s local device.

This project is built to be scalable, secure, and cloud-ready, providing a seamless experience for users without the need for local data storage.

Features 
- Image Annotation: Annotate images directly in the browser. 
- Database Storage: Stores annotation tasks and annotated data in a secure database. 
- No Local Storage: No data is stored on the user’s device; all operations are done in the cloud. 
- Efficient Task Management: Create and manage multiple annotation tasks. 

Technologies Used 
- Backend: Django (with Django REST Framework) 
- Database: SQL - for storing annotation tasks and data. 

Installation 

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/labelbox-web-app.git
   ```

2. Change into the project directory:

   ```bash
   cd labelbox-web-app
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your database (SQL or MongoDB). If you're using SQL, make sure the database is configured properly in `settings.py`.

6. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

Once the application is running, you can access the web app through:

```
http://127.0.0.1:8000
```

### Annotation Projects
- Create new annotation projects via the admin panel or through API calls.
- Annotate images using the provided tools in the web interface.

### API Endpoints
- **GET /api/images/**: Fetch images from the database for annotation.
- **POST /api/annotations/**: Submit annotated data back into the database.


## Contributing

We welcome contributions! To contribute to this project, follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch (`git checkout -b feature-branch`).
4. Make your changes and commit them (`git commit -am 'Add new feature'`).
5. Push to your fork (`git push origin feature-branch`).
6. Create a pull request.

