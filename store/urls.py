  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    
    path('crear_producto/',views.CreateProducto.as_view(), name="crear_producto"),
    path('listar_producto/',views.ListProducto.as_view(), name="listar_producto"),
    path('editar_producto/<pk>',views.UpdateProducto.as_view(),name="editar_producto"),
    path('eliminar_producto/<pk>',views.DeleteProducto.as_view(),name="eliminar_producto"),
]