from . import views
from django.urls import include, path
from .views import MenuView , BookView , MenuItemView , SingleMenuItemView , securedview
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('home/', views.index, name='home'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', include(router.urls)),
    #path('menu/', MenuView.as_view(), name='menu'),
    # path('bookings/', BookView.as_view()),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),    
    path('securedview/', views.securedview),
    
    
]