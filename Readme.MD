# Best Config: Django REST Framework 🛠️

A boilerplate and configuration guide for setting up production-ready Django REST Framework (DRF) APIs with best practices.

---

## 🚀 Project Overview

This repository provides a robust starting point for any DRF-based API project. It includes:

- Clean project structure
- Serializer, view, and routing templates
- Pagination, filtering, and search
- Authentication & permissions (Token, JWT)
- API documentation via Swagger / Redoc
- Celery for background tasks
- Dockerized development & production
- CI/CD-ready configuration (GitHub Actions)

---

## 🧱 Tech Stack

| Layer              | Tools & Libraries                          |
|--------------------|--------------------------------------------|
| Python             | 3.9+ (tested on 3.10, 3.11)                |
| Framework          | Django 4.x                                 |
| API Toolkit        | Django REST Framework (DRF)                |
| Auth               | Django REST Framework Simple JWT / Token   |
| API Docs           | drf-yasg or drf-spectacular (OpenAPI)      |
| Filtering & Search | django-filter, DRF SearchFilter            |
| Pagination         | DRF LimitOffset/PageNumber Pagination       |
| Background Tasks   | Celery + Redis                              |
| Database           | PostgreSQL (local: SQLite supported)        |
| Containerization   | Docker & Docker Compose                     |
| Code Quality       | Flake8, Black, isort, MyPy                  |
| CI/CD              | GitHub Actions (linting, tests)             |

---

## 🗂️ Folder Layout


---

## ⚙️ Getting Started

### 1. Clone the repo & enter directory

```bash
git clone https://github.com/SILAMEAS/best-config-django-rest-framework.git
cd best-config-django-rest-framework






# Development on render  
    Build Command : pip install -r requirements.txt
    ---
    Start Command : waitress-serve gear_store.wsgi:application
    ---
    Depend on project name : gear_store
# Create venv 
    python -m venv ./venv-drf
### activate
### cmd
    source venv-drf/Scripts/activate
### git bash
    source venv-drf/Scripts/activate
# Installing requirements
    pip install -r ./requirements.txt

# Create a New Django Project
    django-admin startproject myproject .

#  Create a Django App
    python manage.py startapp myapp

# Make migrations 
    python .\manage.py makemigrations

# Run Migrate 
    python .\manage.py migrate
# Running Django

### cmd
    python .\manage.py runserver
### git bash
    python manage.py runserver

# Populate : Render loop data to database
    python .\manage.py populate_db

# Generate diagram to file models.dot
    python .\manage.py graph_models api > models.dot
---
You can copy data in file models.dot paste in 
---
 https://dreampuf.github.io/GraphvizOnline/?engine=dot#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D

# Installing django-silk for view and optimize sql query

https://github.com/jazzband/django-silk

    pip install django-silk

** MIDDLEWARE = ['silk.middleware.SilkyMiddleware']

** INSTALLED_APPS = ('silk')
### urls.py 
    path('silk/', include('silk.urls', namespace='silk'))
### python manage.py migrate
http://localhost:8000/silk

# Create Super User
          python .\manage.py createsuperuser

# Allow Cor origin
    pip install django-cors-headers
INSTALLED_APPS = ['corsheaders']

MIDDLEWARE = [  
'corsheaders.middleware.CorsMiddleware',

'django.middleware.common.CommonMiddleware'
]

** CORS_ORIGIN_ALLOW_ALL=True 

---
Or


CORS_ORIGIN_WHITELIST = [

'http://google.com',

'http://hostname.example.com',

'http://localhost:8000',

'http://127.0.0.1:9000'
]
 
# Testing API 
          python manage.py test

# JWT 
### Install : djangorestframework-simplejwt : 

https://github.com/jazzband/djangorestframework-simplejwt

get start : 
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
---
          pip install djangorestframework-simplejwt
---
### add time life of jwt
        from datetime import timedelta

        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            ),
        }
        
        SIMPLE_JWT = {
            'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Change to your desired access token lifetime
            'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Change to your desired refresh token lifetime
        }

# Open API :
https://drf-spectacular.readthedocs.io/en/latest/readme.html
### pip install drf-spectacular
          python ./manage.py spectacular --color --file schema.yml
---
          from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
---
### urlpatterns = [
          # YOUR PATTERNS
---
               path('api/schema/', SpectacularAPIView.as_view(), name='schema')
---
          # Optional UI:
---
              path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
              path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Filter Backend
          pip install django-filter
  ** INSTALLED_APPS = 
  ['django_filters']

  ** REST_FRAMEWORK = 
  {'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']}
---
# Install isort
    pip install isort
---
    isort .\api\views.py

# Config url upload imag can access
    import os
    
    MEDIA_URL = '/media/'  # URL prefix for accessing media files
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directory where media files are stored
# Run shell
    python manage.py shell
# Collecte all dependecy and make it in file requirements.txt
    pip freeze > requirements.txt

# Allow file uploads

    from rest_framework.parsers import MultiPartParser, FormParser
---

    parser_classes = [MultiPartParser, FormParser]
---

    SPECTACULAR_SETTINGS = {
    'TITLE': 'LA Gear Store',
    'DESCRIPTION': 'Online Shopping sell accessories computer',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,  # Ensures correct handling of file uploads
    # OTHER SETTINGS

# SuperAdminOnly for PUT/POST/DELTE and get for all

    from rest_framework import permissions
    
    class SuperAdminOnly(permissions.BasePermission):
        """
        Custom permission to allow only super admins to modify data.
        """
    
        def has_permission(self, request, view):
            # Allow GET, HEAD, OPTIONS for everyone
            if request.method in permissions.SAFE_METHODS:
                return True
            # Allow PUT, POST, DELETE only for super admins
            return request.user and request.user.is_superuser
---
    from rest_framework import viewsets
    from .models import YourModel
    from .serializers import YourSerializer
    from .permissions import SuperAdminOnly
    
    class YourViewSet(viewsets.ModelViewSet):
        queryset = YourModel.objects.all()
        serializer_class = YourSerializer
        permission_classes = [SuperAdminOnly]  # Apply custom permission


# Reset Password

    python manage.py shell

    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.get(email="your_email", is_superuser=True)
    user.set_password("new_password")
    user.save()
    exit()

# Run Script

    python manage.py shell < reset_password.py

### Deployment Vercel

---

#### 1.1 Install Dependencies
Ensure you have the necessary dependencies for a Vercel deployment:

---
        pip install gunicorn whitenoise django-vercel
if error : run this

        pip install gunicorn whitenoise dj-database-url

#### 1.2 Configure settings.py
Modify your settings.py for Vercel:

Update ALLOWED_HOSTS

---
        ALLOWED_HOSTS = ["*"]

Enable Whitenoise for Static Files

        MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",  # Add this line
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ]
Serve Static Files

Add:

        STATIC_URL = "/static/"
        STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
        STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

Use PostgreSQL (Recommended)
Vercel doesn’t support SQLite, so configure PostgreSQL (NeonDB or Supabase).

        import dj_database_url
        
        DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
        }
Set your PostgreSQL URL in .env:

        DATABASE_URL=postgres://user:password@host:port/dbname

#### 2.2 Create a vercel.json file
This tells Vercel how to deploy Django.

---

        {
        "version": 2,
        "builds": [{ "src": "vercel_wsgi.py", "use": "@vercel/python" }],
        "routes": [{ "src": "/(.*)", "dest": "vercel_wsgi.py" }]
        }

#### Step 3: Add vercel_wsgi.py
Create a vercel_wsgi.py file to connect Django with Vercel:

---
        from vercel_wsgi import handle_wsgi
        from myproject.wsgi import application  # Replace `myproject` with your Django project name
        
        app = handle_wsgi(application)

#### Step 4: Deploy to Vercel
Create a vercel_wsgi.py file to connect Django with Vercel:

---
#### * 4.1 Login to Vercel
    vercel login

---
#### * 4.2 Deploy the Project
    vercel

#### Step 5: Set Environment Variables
In the Vercel Dashboard (vercel.com):

* Go to your project settings.
* Add Environment Variables like DATABASE_URL, SECRET_KEY, etc.
---

#### Step 6: Migrate and Collect Static Files
After deployment, run:
    
    vercel env pull .env  # Pull Vercel environment variables locally
    vercel --prod

On Vercel's dashboard, open the Terminal and run:

    python manage.py migrate
    python manage.py collectstatic --noinput


#### Alternative Ways to Run Commands on Vercel

Option 1: Run Commands Locally Using Vercel CLI
Since Vercel doesn’t provide an interactive terminal, you can run commands locally and let them take effect on Vercel.

#### 1.Pull environment variables from Vercel:

---
    vercel env pull .env

#### 2.Run migrations locally (if using a cloud database like Neon, Supabase, or Railway):

---
    python manage.py migrate

#### 3.Collect static files and push them to Vercel:

---
    python manage.py collectstatic --noinput
    vercel --prod

#### Option 2: Use a Custom Vercel API Route

If you must run a command on Vercel, you can create a temporary API route.

1. Create a new file inside your Django app folder (e.g., run_migrate.py):

        import os
        from django.core.management import call_command
        from django.http import JsonResponse
        def migrate(request):
        call_command("migrate")
        return JsonResponse({"message": "Migrations applied successfully!"})
2. Add a URL route to call this function:


    from django.urls import path
    from .run_migrate import migrate
    
    urlpatterns = [
    path("run-migrate/", migrate),
    ]
3. Deploy the changes using:


    vercel --prod
4. Open your browser and visit:


    https://your-vercel-app.vercel.app/run-migrate/

## NOTE : Install Required Dependencies

If you haven’t installed gunicorn and whitenoise, install them:

    pip install gunicorn whitenoise
    pip freeze > requirements.txt

Commit and redeploy to Vercel.

#### Update vercel.json

---

        {
        "version": 2,
        "builds": [
        {
        "src": "vercel_wsgi.py",
        "use": "@vercel/python"
        }
        ],
        "routes": [
        {
        "src": "/(.*)",
        "dest": "vercel_wsgi.py"
        }
        ]
        }

####  Check for Missing Environment Variables

---
On Vercel, go to Dashboard > Project > Settings > Environment Variables and ensure all required variables (like DATABASE_URL, SECRET_KEY, etc.) are added.

#### Redeploy to Vercel
After making the changes, redeploy using:

        vercel --prod
