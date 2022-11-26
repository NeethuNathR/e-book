from .models import Books
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self,validated_data):
          del validated_data['password2']
          user=get_user_model().objects.create(username=validated_data['username'])
          user.set_password(validated_data['password'])
          user.save()
          return user

    class Meta:
        model=get_user_model()
        fields=('username','email','password','password2')



class BookSerializer(serializers.HyperlinkedModelSerializer):

     class Meta:
         model=Books
         fields=('id','url','book_title','Author_name','Genre','Review','Favorite')