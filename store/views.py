from django.core import paginator
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from store.forms import ProductoForm
from django.views.generic import CreateView,UpdateView,DeleteView,ListView #vistas basadas en clases
from django.urls import reverse_lazy # redirecionar

class CreateProducto(CreateView):
    model = Product
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy('store')

class ListProducto(ListView):
    model = Product
    template_name = "listar_producto.html"

class UpdateProducto(UpdateView):
    model = Product
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy('listar_producto')

class DeleteProducto(DeleteView):
    model = Product
    template_name = "producto_confirm_delete.html"
    success_url = reverse_lazy('listar_producto')
    

# Create your views here.
def store(request, category_slug=None):
    #categories =None
    #products = None
    if category_slug != None:
        categories =get_object_or_404(Category, slug=category_slug)#get_object_or_404 -> devuelve 404 page si se escribe algo que no exita dentro de la categoria del url solicitado
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products,6)
        page= request.GET.get('page')
        paged_products =paginator.get_page(page)
        product_count= products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,6)
        page= request.GET.get('page')
        paged_products =paginator.get_page(page)
        product_count= products.count()
    
    context={
        'products':paged_products,
        'product_count':product_count,
        
    }
    return render(request,'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()# verificar si esta en carro actualmente el producto
    except Exception as e:
        raise e
    
    context={
        'single_product':single_product,
        'in_cart': in_cart,
    }
    return render(request,'store/product_detail.html', context)
    

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))#Q -> fucniona como un OR y cuando hay coma como un AND(en este caso no)
            product_count= products.count()
    context={
        'products':products,
        'product_count':product_count,

        
    }

    return render(request,'store/store.html',context)