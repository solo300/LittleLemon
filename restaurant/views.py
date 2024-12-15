from django.shortcuts import render
from rest_framework import viewsets , generics , permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 


from .models import Booking , Menu , User 
from .serializers import MenuSerializer , BookingSerializer , UserSerializer


# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])

def securedview(request):
    
    return Response({"message":"authentication working"})

def index(request):
    return render(request, 'restaurant/index.html' , {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
class MenuView(APIView):
    
    
    def get(self,request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many = True)
    
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response(serializer.errors, status=400)
    
class BookView(APIView):
    
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
    
        return Response(serializer.data)
    
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
