from django.shortcuts import render, redirect
from main.models import *
from main.forms import *
from panel.forms import *
from django.forms import modelformset_factory

ProductImageSet =  modelformset_factory(ProductImage, ProductImageForm, extra=5)



def index_page(request):
  return render(request, 'panel/index.html')


def category_table(request):
  cat = Category.objects.all()
  return render(request, 'panel/general-table.html', context={'all':cat})


def category_form(request):
  form = CategoryForm()
  if request.method == 'POST':
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/panel/category_table/')
  return render(request, 'panel/general-form.html', context={'form':form})


def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/panel/category_table/')
    return render(request, 'panel/general-form.html', context={'form': form, })

def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('/panel/category_table/')


def product_table(request):
  cat = Product.objects.all()
  return render(request, 'panel/product_table.html', context={'all':cat})

def product_form(request):
  form = ProductForm()
  imageform = ProductImageSet(queryset=ProductImage.objects.none())

  if request.method == 'POST':
    form = ProductForm(request.POST)
    imageform = ProductImageSet(request.POST, request.FILES)
    if form.is_valid():
      pro = form.save()

    if imageform.is_valid():
      for i_form in imageform:
          if i_form.is_valid():
            if 'image' in i_form.cleaned_data:
               p_image = i_form.save(commit=False)
               p_image.product = pro
               p_image.save()

      return redirect('/panel/product_table/')
  return render(request, 'panel/product_form.html', context={'form':form, 'imageform':imageform})


def product_edit(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    imageform = ProductImageSet(queryset=product.images.all())
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        imageform = ProductImageSet(request.POST, request.FILES)
        if form.is_valid():
            pro = form.save()

        if imageform.is_valid():
          for i_form in imageform:
              if i_form.is_valid():
                if 'image' in i_form.cleaned_data:
                  p_image = i_form.save(commit=False)
                  p_image.product = pro
                  p_image.save()
          return redirect('/panel/product_table/')
    return render(request, 'panel/product_form.html', context={'form': form, 'imageform':imageform})

def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/panel/product_table/')

def order_table(request):
  ord = Order.objects.all()
  return render(request, 'panel/order_table.html', context={'all':ord})

def order_details(request, pk):
   ord = Order.objects.get(id=pk)
   return render(request, 'panel/order-details.html', context={'ord':ord})

def product_details(request, pk):
   obj = Product.objects.get(id=pk)
   return render(request, 'panel/product_detail.html', context={'obj':obj})