from rest_framework import serializers
from .models import Profile
from Door.models import Door
from Door.serializers import DoorSerializer




class ProfileSerializer(serializers.ModelSerializer) :

    username = serializers.CharField(source='user.username',read_only=True)
    image = serializers.CharField(source='image.url',read_only=True)
    doors = serializers.SerializerMethodField(read_only=True)

    class Meta :
        model  = Profile
        fields = ('id','slug','user','username','image','doors')

    def get_doors(self,profile_obj):
        doors_qs = Door.objects.filter(profile=profile_obj)
        serializer = DoorSerializer(door_qs,many=True)
        return serializer.data



class SimpleProfileSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(source='user.username',read_only=True)
    image = serializers.CharField(source='image.url',read_only=True)

    class Meta :
        model  = Profile
        fields = ('id','slug','username','image')
