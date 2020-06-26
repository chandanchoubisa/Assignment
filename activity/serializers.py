from activity.models import User,UserActivity
from rest_framework import serializers




class UserActivitySerializer(serializers.ModelSerializer):

	class Meta:
		model = UserActivity
		fields = ('start_time','end_time')

class UserSerializer(serializers.ModelSerializer):
	activity_periods = UserActivitySerializer(many=True,source='user_activities')
	class  Meta:
		model = User
		fields = ('id','real_name','tz','activity_periods')



