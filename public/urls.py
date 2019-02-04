from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('sections/', views.SectionView.as_view(), name='index'),
]
