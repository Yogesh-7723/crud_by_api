from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Library
from django.views.decorators.csrf import csrf_exempt
from .serializers import LibrarySerializer
from rest_framework import status

# Create your views here.

def index(request):
  return HttpResponse("<h1>Jai Shree ShiyaRam Balaji Hanuman</h1>")

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@csrf_exempt
def crud_operation(request):
  headers= {
      'XSRF-TOKEN': request.META.get('CSRF_COOKIE')
  }
  if request.method == 'GET':
    id = request.data.get('id', None)
    print(id)
    if id is not None:
          data = Library.objects.get(id=id)
          serialize = LibrarySerializer(data)
          return Response(serialize.data,headers=headers,status=status.HTTP_200_OK)
    data = Library.objects.all()
    serialize = LibrarySerializer(data,many=True)
    return Response(serialize.data,headers=headers,status=status.HTTP_200_OK)
        
  if request.method == 'POST':
    serialize = LibrarySerializer(data=request.data)
    if serialize.is_valid():
      serialize.save() 
      return Response({'success':'Data Successfully Created'},headers=headers,status=status.HTTP_201_CREATED) 
    return Response(serialize.errors,headers=headers,status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'PUT':
    data = request.data
    id = data.get('id', None)
    stu = Library.objects.get(id=id)
    serialize = LibrarySerializer(stu,data=data,partial=True)
    if serialize.is_valid():
      serialize.save()
      return Response({'success':'Successfully Updated'},headers=headers)
    return Response(serialize.errors,headers=headers,status=status.HTTP_400_BAD_REQUEST)
      
  
  elif request.method == 'PATCH':
    data = request.data
    id = data.get('id', None)
    stu = Library.objects.get(id=id)
    serialize = LibrarySerializer(stu,data=data)
    if serialize.is_valid():
      serialize.save()
      return Response({'success':'Successfully Updated'},headers=headers)
    return Response(serialize.errors,headers=headers,status=status.HTTP_400_BAD_REQUEST)
  
  else:
    if request.method == 'DELETE':
      data = request.data
      id = data.get('id', None)
      stu = Library.objects.get(id=id)
      stu.delete()
      return Response({'success':'Successfully Delete'},headers=headers)

  
    