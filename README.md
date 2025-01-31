# FAQ Project

This is a Django-based FAQ project that allows users to manage frequently asked questions. It includes features like rich text editing using CKEditor and a REST API using Django REST Framework.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 5.1.5
- Redis (for caching)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/faq_project.git
    cd faq_project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Configuration

- Update the `SECRET_KEY` in `faq_project/settings.py` for production use.
- Configure the `ALLOWED_HOSTS` in `faq_project/settings.py` for your deployment.

### Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage FAQs.
- Use the REST API endpoints to interact with the FAQ data programmatically.

## Features

- Rich text editing with CKEditor
- REST API with Django REST Framework
- Caching with Redis

# HOW TO USE

## Step 1: Log in to the Admin Panel
Start the development server (if it’s not already running):

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://localhost:8000/admin
```

Log in with the superuser credentials you created earlier.

## Step 2: Add FAQs via the Admin Panel

### Access the FAQ Model:
- After logging in, you’ll see the Django admin dashboard.
- Look for the FAQs section (this is the model you registered in `admin.py`).

### Add a New FAQ:
1. Click on **FAQs**.
2. Click the **Add FAQ** button in the top-right corner.
3. Fill in the fields:
   - **Question**: Enter the question (e.g., "What is Django?").
   - **Answer**: Use the WYSIWYG editor to format the answer (e.g., "Django is a web framework for Python.").
   - **Question (Hindi)**: Leave this blank for now (it will be auto-translated when you save).
   - **Question (Bengali)**: Leave this blank for now (it will be auto-translated when you save).
   - **Answer (Hindi)**: Leave this blank for now (it will be auto-translated when you save).
   - **Answer (Bengali)**: Leave this blank for now (it will be auto-translated when you save).

### Save the FAQ:
- Click the **Save** button.
- The save method in your FAQ model will automatically translate the question and answer into Hindi and Bengali using the `googletrans` library.

## Step 3: View and Edit FAQs

### View FAQs:
- After saving, you’ll be redirected to the list of FAQs.
- You’ll see the question, Hindi translation, and Bengali translation in the list.

### Edit an FAQ:
- Click on any FAQ to edit it.
- You can modify the question, answer, or translations manually if needed.

## Step 4: Test the API

### Fetch FAQs in English:
Open your browser or use a tool like `curl` or Postman to access:

```
http://localhost:8000/api/faqs/
```

This will return the FAQs in English (default language).

### Fetch FAQs in Hindi:
Access:

```
http://localhost:8000/api/faqs/?lang=hi
```

This will return the FAQs with Hindi translations.

### Fetch FAQs in Bengali:
Access:

```
http://localhost:8000/api/faqs/?lang=bn
```

This will return the FAQs with Bengali translations.

## License

This project is licensed under the MIT License.