from django.shortcuts import render,redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .form import ShopForm
from .models import Shop
from .serializers import ShopSerialiser
from .utils import haversine
# Create your views here.



@api_view(['GET'])
def searchShops(request):
    try:
        userLat=float(request.GET.get('latitude'))
        userLon=float(request.GET.get('longitude'))
    except(TypeError, ValueError):
        return Response({"error": "Invalid latitude or longitude"}, status=400)
    shops = Shop.objects.all()
    sorted_shops=sorted(shops,key=lambda shop: haversine(userLat, userLon, shop.latitude, shop.longitude))

    serialized=ShopSerialiser(sorted_shops,many=True)

    return Response(serialized.data)


def home(request):
    return render(request, 'home.html')

def registerShop(request):
    if request.method =='POST':
        form=ShopForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('homePage')
    else:
        form=ShopForm()
    return render(request,'register.html',{'form':form})
    
class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerialiser




