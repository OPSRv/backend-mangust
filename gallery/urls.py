from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/gallery/', views.GalleryList.as_view()),
    path('api/gallery/<int:pk>/', views.GalleryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
