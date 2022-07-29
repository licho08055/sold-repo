import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


from .serializers import UserSerializer,SellSerializer,BuyerSerializer
from .models import User,Sell,Buyer



@api_view(['GET','POST'])
def UserListCreateView(request):
    if request.method=='GET':
        list=User.objects.all()
        serializer=UserSerializer(list,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        create=UserSerializer(data=request.data)
        if create.is_valid():
            create.save()
            return Response(create.data,status=status.HTTP_201_CREATED)
        return Response(create.errors,status=status.HTTP_403_FORBIDDEN)
    

@api_view(['GET','POST'])
def SellListCreateView(request):
    if request.method=='GET':
         sell=Sell.objects.all()
         serializer=SellSerializer(sell,many=True)
         return Response(serializer.data)
     
    elif request.method=='POST':
        serializer=SellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def SellDetailUpdateDeleteView(request,id):
    if request.method=='GET':
        detail=get_object_or_404(Sell,id=id)
        serializer=SellSerializer(detail)
        return Response(serializer.data)
    elif request.method=='PUT':
        update=get_object_or_404(Sell,id=id)
        serializer=SellSerializer(update,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        dels=get_object_or_404(Sell,id=id)
        dels.delete()
        return Response({'msg':'Sell delete!'})
    
    
@api_view(['GET','POST'])
def BuyerListCreateView(request):
    if request.method=='GET':
         sell=Buyer.objects.all()
         serializer=BuyerSerializer(sell,many=True)
         return Response(serializer.data)
     
    elif request.method=='POST':
        serializer=BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def BuyerDetailUpdateDeleteView(request,id):
    if request.method=='GET':
        detail=get_object_or_404(Buyer,id=id)
        serializer=BuyerSerializer(detail)
        return Response(serializer.data)
    elif request.method=='PUT':
        update=get_object_or_404(Buyer,id=id)
        serializer=BuyerSerializer(update,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        dels=get_object_or_404(Buyer,id=id)
        dels.delete()
        return Response({'msg':'Buyer delete!'})
        
    
    


    


