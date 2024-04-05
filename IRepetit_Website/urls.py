from django.urls import path

from IRepetit_Website.views import index, registration, tutor, user_login, user_logout, user_profile

urlpatterns = [
    path('', index, name='index', ),
    path('login', user_login, name='login', ),
    path('profile', user_profile, name='profile', ),
    path('logout', user_logout, name='logout', ),
    path('registration', registration, name='registration', ),
    path('tutor', tutor, name='tutor', ),
]
