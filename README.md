# Project

## Installation

Follow these steps to set up the  project on your local machine.

### Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

### Steps

1. **Clone the Repository:**

 ```bash
   git clone https://github.com/shilpacvenugopal/myproject.git
   ```
```bash
   cd myproject/
   ```

2. **Create a Virtual Environment:**

   ```bash
   virtualenv venv
   ```

3. **Activate the Virtual Environment:**

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Admin User):**

   ```bash
   python manage.py createsuperuser
   ```


7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **Usage**
1. How to use the API endpoints for Table2:
   ```bash
http://127.0.0.1:8000/dashboard/dashboard/
```
Methods
   - GET:  For reading
   - POST:  For creation
   - PUT: For updation
   - DELETE: For deletion

3. Importing data to Table2 from CSV or Excel:
  After running the command
 ```bash
   python manage.py runserver
   ```
in broswer search http://localhost:8000/admin/ 
in dashboard open table2 and import the file 
3. Image upload with conversion to webp format:
After running the command
 ```bash
   python manage.py runserver
   ```
in broswer search http://localhost:8000/admin/ 
in dashboard open imagemodel and add the image

5. Token authentication API with Django Rest Framework:
   - Endpoint: http://127.0.0.1:8000/dashboard/api/token-auth/
   - Method: POST
   - Data parameters: username, password

## Dependencies:
- Django
- Django Rest Framework
- Django Import-Export



