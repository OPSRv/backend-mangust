from rest_framework import generics
from .serializers import ProgramSerializer, ProgramSerializerDetail
from .models import Program


class ProgramsList(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramDetail(generics.RetrieveAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializerDetail
