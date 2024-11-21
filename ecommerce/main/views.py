from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from main.forms import *
from django.core.paginator import Paginator

def index_page(request):
    latest_pro = Product.objects.all().order_by('-created_at')[0:3]
    all_pro = Product.objects.all
    context= {
              'all_pro':all_pro,
              'latest':latest_pro,
              }
    return render(request, 'main/index.html',context )


def category(request, pk):
    cat = Category.objects.get(id=pk)
    cat_pro = Product.objects.filter(category=cat)


    min_val = request.GET.get('min_val') or 0
    max_val = request.GET.get('max_val')



    if cat_pro:
        min_price = int(cat_pro.order_by('price')[0].final_price)
        max_price = int(cat_pro.order_by('price')[0].final_price)+1
    else:
        min_price, max_price = 0,0

    latest = cat_pro.order_by('-created_at')[0:3]

    cat_pro_disc = Product.objects.filter(category=cat, discount__gt = 0)

    if max_val:
        a= int(min_val.replace('$', ''))
        b= int(max_val.replace('$', ''))

        cat_pro = cat_pro.filter(price__range=(a,b))
        cat_pro_disc = cat_pro_disc.filter(price__range=(a,b))

    sort_by = request.GET.get('sort_by')

    if sort_by == '0':
        cat_pro = cat_pro.order_by('id')
    elif sort_by == '1':
        cat_pro = cat_pro.order_by('name')
    elif sort_by == '2':
        cat_pro = cat_pro.order_by('-name')
    elif sort_by == '3':
        cat_pro = cat_pro.order_by('price')
    elif sort_by == '4':
        cat_pro = cat_pro.order_by('-price')
    
    paginator = Paginator(cat_pro, 4)
    page = request.GET.get('page', 1)

    page_obj = paginator.get_page(page)

    context= {
        'latest': latest,
        'cat_pro': page_obj,
        'cat_pro_disc': cat_pro_disc,
        'min_price': min_price,
        'max_price': max_price,
        'sort':sort_by,
        'cat': cat,


    }
    return render(request, 'main/shop-grid.html', context)


def login_page(request):
  form = LoginForm()
  if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            upass = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
  return render(request, 'main/login.html' ,context={'form': form,})

def register_page(request):
    form = RegistrationFrom()
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    return render(request, 'main/register.html',context={'form': form,})

def logout_page(request):
    logout(request)
    return redirect('/')

def shop_details(request, pk):
    product_details = Product.objects.get(id=pk)

    related_pro = Product.objects.filter(category = product_details.category)

    related_pro = related_pro.exclude(id = product_details.id)

    return render(request, 'main/shop-details.html', context={'details':product_details, 'rel':related_pro})

def shoping_cart(request):
    return render(request, 'main/shoping-cart.html')

def add_to_cart(request, pk):
    pro = Product.objects.get(id=pk)
    cart, created = Cart.objects.get_or_create(user = request.user, is_ordered = False)

    cart_item, created = Cartitem.objects.get_or_create(cart = cart, product = pro)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')

def delete_item(request, pk):
    form = Cartitem.objects.get(id=pk)
    form.delete()
    return redirect('/cart')

def checkout(request):
    form = OrderForm()
    return render(request, 'main/checkout.html', context={'form':form,})

def save_order(request):
    cart, created = Cart.objects.get_or_create(user = request.user, is_ordered = False)
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.cart = cart
        order.save()
        cart.is_ordered = True
        cart.save()
        return redirect('/')
    return render(request, 'main/checkout.html', context={'form':form})