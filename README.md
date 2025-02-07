# TODO App

This is a simple **Django-based TODO app** that allows users to manage their tasks efficiently. The application provides features to **add, update, mark as completed, and delete tasks**.

## Features

- **Create Tasks (C - Create)**: Users can add new TODO tasks with a title and description.
- **Read Tasks (R - Read)**: All tasks are listed on the main page, showing their details.
- **Update Tasks (U - Update)**: Users can edit the title and description of a task.
- **Delete Tasks (D - Delete)**: Unwanted tasks can be removed.
- **Mark as Completed**: Tasks can be marked as completed using a checkbox.
- **Responsive UI**: A clean and minimalistic user interface.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (with Poppins font), JavaScript
- **Database**: SQLite (for development)

## Approach (CRUD - Create, Read, Update, Delete)

The application follows **CRUD operations** using Django:

- **Create (`views.py` - `todo_create`)**: Users can add new tasks through a form.
- **Read (`views.py` - `todo_list`)**: Retrieves and displays all tasks from the database.
- **Update (`views.py` - `todo_update`)**: Allows editing task details.
- **Delete (`views.py` - `todo_delete`)**: Removes tasks from the database.

Additionally, Django **templates (`templates/`)** handle dynamic rendering, while **models (`models.py`)** define the database structure.

## Project Structure

```plaintext
📦 todoproject
├── 📜 manage.py                 # Django management script
├── 📜 db.sqlite3                # SQLite database (for local development)
├── 📂 todoproject               # Django project settings
│   ├── 📜 settings.py           # Main settings file
│   ├── 📜 urls.py               # URL routing configuration
│   ├── 📜 wsgi.py               # WSGI application entry point
│
├── 📂 todoapp                   # Main app handling tasks
│   ├── 📂 migrations            # Database migrations
│   ├── 📂 templates             # HTML templates
│   │   ├── 📜 base.html         # Base template
│   │   ├── 📜 todo_list.html    # List view template
│   │   ├── 📜 todo_form.html    # Form for creating/updating tasks
│   │   ├── 📜 todo_confirm_delete.html  # Confirmation page for deleting tasks
│   ├── 📂 static                # CSS and JS files
│   │   ├── 📜 styles.css        # Main CSS file
│   ├── 📜 models.py             # Database model for tasks
│   ├── 📜 views.py              # Handles user requests
│   ├── 📜 forms.py              # Django forms for handling input
│   ├── 📜 urls.py               # App-specific URL routing
