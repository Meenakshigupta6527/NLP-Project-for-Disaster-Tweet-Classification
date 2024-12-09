from django.urls import path
from predictapp import views
#from predictapp.views import predict_tweet
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('visualizations', views.visualizations, name='visualizations'),
    path('prediction', views.prediction, name='prediction'),
    path('', views.predict_tweet, name='predict_tweet'),
    path('template', views.template, name='template')
]