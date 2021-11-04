from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BookSerializer
from .models import Book
import requests
import json
import ast

@api_view(['GET'])
def ExternalBook(request): 
    url = "https://www.anapioficeandfire.com/api/books?name="+request.GET["name"]
    response = requests.get(url)
    data = response.json()
    for element in data: 
         del element['url'] 
         del element['mediaType'] 
         del element['characters'] 
         del element['povCharacters']
         element['number_of_pages'] = element.pop('numberOfPages')
         element['publisher'] = element.pop('publisher')
         element['country'] = element.pop('country')
         element['release_date'] = element.pop('released')
         element['release_date'] = element['release_date'].split('T')[0]

    return Response({"status_code": 200,"status": "success", "data" :data})

@api_view(['GET','POST'])
def CreateBook(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        output = serializer.data
        for element in output: 
            element['authors'] = ast.literal_eval(json.loads(element['authors']))

        return Response({"status_code": 200,"status": "success", "data" : output})

    elif request.method == 'POST':
         output = request.data
         request.data['authors'] = json.dumps(str(request.data['authors']))
         serializer = BookSerializer(data=request.data)
         if serializer.is_valid():
           serializer.save()
           request.data['authors'] = ast.literal_eval(json.loads(request.data['authors']))
           return Response({"status_code": 201,"status": "success", "data" : [{"book": output}]})


@api_view(['GET','PATCH','DELETE'])
def ViewBook(request, id):
  message="ID "+str(id)+" Does Not Exist in DB"
  try:
    
         if request.method == 'GET':
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book, many=False)
            output = serializer.data
            output['authors'] = ast.literal_eval(json.loads(serializer.data['authors']))
            return Response({"status_code": 200,"status": "success", "data" : output})

         elif request.method == 'PATCH':
              book = Book.objects.get(id=id)
              output = request.data
              request.data['authors'] = json.dumps(str(request.data['authors']))
              serializer = BookSerializer(instance=book, data=request.data)
              message = ""
              if serializer.is_valid():
                 serializer.save()
                 message = "The book "+serializer.data['name']+" was updated successfully"
                 request.data['authors'] = ast.literal_eval(json.loads(request.data['authors']))
                 return Response({"status_code": 200,"status": "success", "message": message, "data" : output})

         elif request.method == 'DELETE':
              book = Book.objects.get(id=id)
              message=""
              serializer = BookSerializer(book, many=False)
              message = "The book "+serializer.data['name']+" was updated successfully"
              book.delete()
              return Response({"status_code": 200,"status": "success", "message": message, "data" : []})

  except Book.DoesNotExist:
         return Response({"status_code": 404,"status": "resource not found", "message": message, "data" : []})
