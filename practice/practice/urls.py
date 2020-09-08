from django.contrib import admin
from django.urls import path

# import view
import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstapp.views.home, name="home")
]
