from django.urls import path, include
from . import views
app_name='studentapp'
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
]