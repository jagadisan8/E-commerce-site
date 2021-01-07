from django.shortcuts import render
from shop.models import products


# Create your views here.
def index(request):
    product_objects = products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    return render(request,'shop/index.html',{"product_objects":product_objects})
