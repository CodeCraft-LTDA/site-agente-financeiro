from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('definition/', views.definition, name='definition'),
    path('finance/', views.finance, name='finance'),
    path('change_password', views.change_password, name='change_password'),
    path('pdf/<int:year>/<int:month>/<int:day>/', views.pdf_by_date, name='pdf_by_date'),
    path('pdf/today/', views.redirect_to_today_pdf, name='redirect_to_today_pdf'),
]
