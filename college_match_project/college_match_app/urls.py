from django.contrib import admin
from django.urls import path
from college_match_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),  # Homepage redirects to 'About Us'
    path('news/', news, name='news'),
    path('top_colleges/', top_colleges, name='top_colleges'),
    path('get_consultancy/', get_consultancy, name='get_consultancy'),
    path('dream_college/', dream_college, name='dream_college'),
    path('scholarships/', scholarship, name='scholarships'),
    path('', about_us, name='about_us'),
    path('faq/', faq, name='faq'),
    path('dis/', dis, name='dis'),
    path('tc/', tc, name='tc'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name='contact'),
    path('sitemap/', sitemap, name='sitemap'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/',logout_page,name='logout'),
    path('profile/', profile, name='profile'),
    path('home/', home, name='home'),











]
