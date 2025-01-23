from django.urls import path
from app_main_page.views import main_page

app_name = "app_main_page"

urlpatterns = [
 path('', main_page, name='main_page'),
]