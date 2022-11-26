E-Book Management


Overview

.The Web browsable API is a huge usability win for your developers

.Authentication policies including optional packages for OAuth1a and OAuth2.

.Serialization that supports both ORM and non-ORM data sources.

.Customizable all the way down - just use regular function-based views if you don't need the more powerful features.

.Extensive documentation, and great community support.





## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


##  Requirements

.Use Django 3.2 LTS, and the default SQLite database.

## Installation


Install using  pip.

```bash
 pip install djangorestframework
```
 Add ```'rest_framework'``` to your ```INSTALLED_APPS``` setting.


```bash
   INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
## Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing ebook details.

Startup up a new project like so...

```bash
 pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
```

Now edit the ```example/urls.py``` module in your project:
```

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ebookapp import views
from ebookapp.views import BookViewset,CreateUserview
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView
router=routers.DefaultRouter()
router.register('book',BookViewset)


urlpatterns = [
path('api-auth/',include('rest_framework.urls')),
path('api/token/', TokenObtainPairView.as_view()),
path('api/token/refresh/', TokenRefreshView.as_view()),
path('custom-url/', include('drf_expiring_token.urls')),
path('',include(router.urls)),
path('admin/', admin.site.urls),
]
```
We'd also like to configure a couple of settings for our API.

Add the following to your``` settings.py ```module:
```
REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),
     'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'drf_expiring_token.authentication.ExpiringTokenAuthentication',

    ),
 ```
That's it, we're done!

```
    ./manage.py runserver
 ```
You can now open the API in your browser at``` http://127.0.0.1:8000/```, and view ebook details

You can also interact with the API using command line tools such as ```postman```. For example, to list ebook details
```
import requests



headers={}
headers['Authorization']='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5MzY0NDk5LCJpYXQiOjE2NjkzNjQxOTksImp0aSI6Ijk0OGU5NGIxMTI1NzQ4MDk5YzhlMjZiNDM0ZmE5NTljIiwidXNlcl9pZCI6NX0.Xh1Nie3byOBUpRsdmwGLdvwQAmn-FiS1VZLXc--NkcE'
r=requests.get('http://127.0.0.1:8000/book/',headers=headers)
print(r.text)
```
```
{
        "id": 1,
        "url": "http://127.0.0.1:8000/book/1/",
        "book_title": "The India Story",
        "Author_name": "Bimal Jalal",
        "Genre": "Literary criticism",
        "Review": 4,
        "Favorite": true
    },
```    