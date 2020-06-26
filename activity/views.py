from django.shortcuts import render

from faker import Faker
from datetime import datetime
from datetime import timedelta
import random
import calendar

from activity.models import User,UserActivity
from activity.serializers import UserSerializer,UserActivitySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def populate_db(n):
	# Helper fuhnction for populating db with fake data
	faker = Faker()
	for i in range(n):

		fake_id = faker.bothify(text='?###?#???')
		fake_name = faker.name()
		fake_tz = faker.timezone()

		for i in range(random.randint(1,4)):

			fake_startdate = faker.date_time_between()
			random_hours=random.randint(0,6)
			random_min=random.randint(1,61)
			fake_enddate = fake_startdate+timedelta(hours=random_hours,minutes=random_min)
			start_time = convert_dateformat(fake_startdate)
			end_time = convert_dateformat(fake_enddate)
			# Creating objects of User and Activity Models
			user = User(id=fake_id,real_name=fake_name,tz=fake_tz)
			user.save()
			activity = UserActivity(user_activity=user,start_time=start_time,end_time=end_time)
			activity.save()




def convert_dateformat(convert_date):
	# This function converts value in datetime format into required format
	convert_time= convert_date.strftime("%I:%M%p")
	y_t=str(convert_date)
	y_t=y_t.split(" ")
	d=y_t[0].split("-")
	mon=calendar.month_name[int(d[1])][:3]
	str_time = mon+" "+d[2]+" "+d[0]+"  "+convert_time
	return str_time

"""
Function for handling request for populating the database with fake data
For now GET and POST both are allowed here.
"""

@api_view(('GET','POST'))
def data_loading(request):
		populate_db(5)
		return Response("Dummy data Successfully added",status=status.HTTP_201_CREATED,)



# Handling GET request for showing data in required format

@api_view(('GET',))
def details(request):
	if request.method=='GET':
		#Getting all User objects details from query
		activity = User.objects.all()

		#Passing all User object data as an instance to UserSerializer
		serialize = UserSerializer(instance=activity, many=True)

		info = {'ok':True,'members':serialize.data}
		return Response(info,status=status.HTTP_200_OK)
	return Response("Something Went Wrong",status=status.HTTP_400_BAD_REQUEST)








