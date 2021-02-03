from django.shortcuts import get_object_or_404, render
from .models import Product
# Create your views here.


def all_products(request):
    """ A view to render products page, search it and sort products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to render product details page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
