from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, ProductImage
from orders.models import Status, Order, ProductsInOrder
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    # products = Product.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    # import pdb; pdb.set_trace()
    products_images_phones = products_images.filter(product__category__id=1).order_by('-created')[0:4]
    products_images_laptops = products_images.filter(product__category__id=2).order_by('-created')[0:4]
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by('-created')[0:4]
    return render(request, 'home.html', locals())

def product(request, product_id):
    # post = get_object_or_404(Product, pk=pk)v
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'product.html', locals())

def laptops(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by('-created')
    products_images_laptops = products_images.filter(product__category__id=2).order_by('-created')
    paginator = Paginator(products_images_laptops, 8)  # 8 laptops in each page
    page = request.GET.get('page')
    try:
        products_images_laptops = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products_images_laptops = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products_images_laptops = paginator.page(paginator.num_pages)
    return render(request, 'laptops.html', {'page': page, 'products_images_laptops': products_images_laptops})

def phones(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by('-created')
    products_images_phones = products_images.filter(product__category__id=1).order_by('-created')
    paginator = Paginator(products_images_phones, 8)  # 8 laptops in each page
    page = request.GET.get('page')
    try:
        products_images_phones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products_images_phones = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products_images_phones = paginator.page(paginator.num_pages)
    return render(request, 'phones.html', {'page': page, 'products_images_phones': products_images_phones})
