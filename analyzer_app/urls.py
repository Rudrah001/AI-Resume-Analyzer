from django.urls import path,include
from analyzer_app import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('analyze/',views.analyze,name='analyze')
]