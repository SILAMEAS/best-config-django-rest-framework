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
