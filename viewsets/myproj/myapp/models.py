from django.db import models

class EmployeeJob(models.Model): 
	department_name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	salary = models.IntegerField()

	def __str__(self):
		return self.department_name


# class ManagerTable(models.Model):



class Employee(models.Model):
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	hire_date = models.DateField()
	department = models.ForeignKey(EmployeeJob, on_delete=models.CASCADE)
	current_employee = models.BooleanField(default=True)

	def validate_unique(self, exclude=None):
		"""
		can also do this within Operator class 
			# class Meta:
			# 	unique_together = ('first_name', 'last_name')
		"""
		employees = Employee.objects.all()
		# import pdb; pdb.set_trace()
		for employee in employees:
			if employee.first_name == self.first_name and employee.last_name == self.last_name: 
				raise ValidationError('Combination of first & last name alreads exists in DB = {} {}'.format(employee.first_name, employee.last_name))

		self.first_name.capitalize()
		self.last_name.capitalize()
		
		

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)
