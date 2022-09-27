from django.http import JsonResponse
from django.shortcuts import render
from django.http import QueryDict
from rest_framework.viewsets import ModelViewSet

from task_1.models import Data_test
from task_1.serializers import DataSerializer


def index(request):
    if(request.POST):
        session_key = request.session.session_key
        names = request.POST.getlist("names[]")
        names_p = dict(request.POST)
        new_data = Data_test.objects.create(names=names)
    return render(request, 'task_1/index.html')


class DataView(ModelViewSet):
    queryset = Data_test.objects.all()
    serializer_class = DataSerializer
