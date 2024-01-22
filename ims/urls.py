
from django.urls import path
from . import views


urlpatterns = [
   
    # path('create_order/', views.create_assign, name='create_order'),
    path('', views.index, name= 'index'),
    path('addproduct', views.add_product, name= 'add_product'),
    path('product', views.assigned_product, name= 'product'),
    path('details/<str:pk>', views.product_detail, name= 'product_details'),
    path('update/<str:pk>/', views.update, name='update' ),
    path('delete/<str:pk>/', views.delete, name='delete' ),
    path('deleteProduct/<str:pk>/', views.delete_product, name='deleteProduct' ),
    path('updateProduct/<str:pk>/', views.update_product, name='updateProduct' ),
    
]
