from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/programs/', views.ProgramsList.as_view()),
    path('api/programs/<int:pk>/', views.ProgramDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
