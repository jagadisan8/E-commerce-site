from django.shortcuts import render
from shop.models import products
from django.core.paginator import Paginator


# Create your views here.
def index(request):

    """ search """
    product_objects = products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    """ paginator """
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{"product_objects":product_objects})


def detail(request,id):
    product_object = products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})
