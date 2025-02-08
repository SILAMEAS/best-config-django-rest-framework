# Running Django
### activate
    source venv-drf/Scripts/activate
### cmd
    python .\manage.py runserver
### git bash
    python manage.py runserver
# Create venv 
    python -m venv ./venv-drf

# Installing requirements
    pip install -r ./requirements.txt

# Make migrations 
    python .\manage.py makemigrations

# Run Migrate 
    python .\manage.py migrate

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
