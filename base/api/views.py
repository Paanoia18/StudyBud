from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@csrf_exempt
def delete_room(request, id):
    if request.method == 'DELETE':
        try:
            room = Room.objects.get(id=id)
            room.delete()
            return JsonResponse({'message': 'Комната удалена'}, status=200)
        except Room.DoesNotExist:
            return JsonResponse({'message': 'Комната не найдена'}, status=404)
    return JsonResponse({'message': 'Неверный метод'}, status=405)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
