from django.db import models

# Create your models here.
class User(models.Model):
	id = models.CharField(max_length=10, primary_key=True)
	real_name=models.CharField(max_length=100)
	tz=models.CharField(max_length=100)

	def __str(self):
		return self.real_name

class UserActivity(models.Model):
	user_activity = models.ForeignKey(User,related_name = 'user_activities',on_delete=models.CASCADE)
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
