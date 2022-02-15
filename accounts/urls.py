"""sysposfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from.views import *
urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('service/', Services.as_view(), name='Services'),
    path('service/<int:ser_id>', Services.as_view(), name='Services'),
    path('clothdetails',ClothData.as_view()),
    path('clothdetails/<int:cloth_id>',ClothData.as_view()),
    path('pricedetails',PriceData.as_view()),
    path('pricedetails/<int:price_id>',PriceData.as_view()),
    path('accountdetails',AccountData.as_view()),
    path('accountdetails/<int:ac_type_id>',AccountData.as_view()),
    path('plant',PlantData.as_view()),
    path('plant/<int:plant_id>',PlantData.as_view()),

]