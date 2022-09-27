from rest_framework.serializers import ModelSerializer

from task_1.models import Data_test


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data_test
        fields = ['id', 'names']
