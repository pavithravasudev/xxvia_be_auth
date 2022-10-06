from rest_framework import serializers 
from xxvia_be_auth_app.models import User

# Serializers to handle Schedules and Students

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstname', 'lastname', 'emailaddress', 'userrole']