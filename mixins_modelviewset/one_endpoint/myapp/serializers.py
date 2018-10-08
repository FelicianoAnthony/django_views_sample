from .models import Computer
from rest_framework import serializers

#https://stackoverflow.com/questions/44085153/how-to-validate-a-json-object-in-django

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('id','computer_name','bfid','description','timestamp','updated','active')

        