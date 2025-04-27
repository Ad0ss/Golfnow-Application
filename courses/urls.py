from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('book/', views.book, name='book'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
