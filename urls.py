from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path("", views.index,name='home'),

    path('index/', views.index, name='index'),

    path('pricing/', views.pricing, name='pricing'),

    path('course/', views.course, name='course'),

    path("about", views.about,name='about'),

    path('base/', views.base, name='base'),

    path("services", views.services,name='services'),

    path('contact/', views.contact, name='contact'),

    path('Asement/', views.asement_view, name='Asement'),

    path('result/', views.result_view, name = 'result'),

    path('signup',views.signup,name="signup"),
    
    # path('signin',views.signin,name="signin"),
    #path('signin', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),  # Change the URL pattern to 'signin/'

    path('signout',views.signout,name="signout"),

    path('pricing/face.html', views.face_view, name='face'),

]
