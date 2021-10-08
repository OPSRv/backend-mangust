from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/musicband/', views.MusicBandList.as_view()),
    path('api/musicband/<int:pk>/', views.MusicBandDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
