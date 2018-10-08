
from .models import EmployeeJob,  Employee
from rest_framework import serializers


# https://stackoverflow.com/questions/44085153/how-to-validate-a-json-object-in-django
#https://stackoverflow.com/questions/39291258/when-and-how-to-validate-data-with-django-rest-framework
	#If you need to manually control the creation of the object, perform_create is the hook that you need to override, not create.

class EmployeeJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeJob
        fields = ('id', "department_name", "job_title", "state", "salary")
        


 


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', "first_name", "last_name", "department", "hire_date", "current_employee")

