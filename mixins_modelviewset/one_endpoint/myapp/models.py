from django.db import models

class Computer(models.Model):
    computer_name = models.CharField(max_length=10)
    bfid = models.IntegerField(default=0, unique=True)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.computer_name






# class Department(models.Model): 
#     department_name = models.CharField(max_length=50)
#     department_id = models.IntegerField(unique=True)






# class Employee(models.Model):
#     employee = models.CharField(max_length=50)
#     employee_id = models.CharField(max_length=4)
#     state = models.CharField(max_length=2)
#     hire_date = models.DateField()
#     manager_id = models.CharField(max_length=2)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     salary = models.ForeignKey(Salary, on_delete=models.CASCADE)


# class Salary(models.Model):
#     salary = models.IntegerField()

# """


# /state/<employee>


# /department/<employee>

# state/


# employee/ -- GET-POST 
# employee/<employee_id> -- GET-UPDATE-DELETE

# state/



# """




