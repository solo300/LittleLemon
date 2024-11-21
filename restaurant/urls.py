from . import views
from django.urls import include, path
from .views import MenuView , BookView , MenuItemView , SingleMenuItemView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', include(router.urls)),
    # path('menu/', MenuView.as_view()),
    # path('bookings/', BookView.as_view()),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),    
    
]