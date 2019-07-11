from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import DoorSerializer
from .models import Door
from .permissions import IsOwnerAndAuthenticated

class DoorViewSet(viewsets.ModelViewSet):
    serializer_class = DoorSerializer
    queryset = Door.objects.all()
    permission_classes = [IsOwnerAndAuthenticated,]

    @action(methods=['PUT'],detail=True)
    def set_door_state(self,request,pk):
        door_obj = self.get_object()
        door_new_state = self.request.data.get('new_state')
        doo_obj.opened = door_new_state
        doo_obj.save()
        return Response({'response':'door updated'},status=status.HTTP_200_OK)
