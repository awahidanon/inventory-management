
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
    path('generate_invoice/<int:pro_id>/', views.generate_invoice, name='generate_invoice'),
    path('view_department/', views.department_view, name='view_department' ),
    path('view_category/', views.category_view, name='view_category' ),
    path('generate_report/<str:period>/', views.generate_report, name='generate_report'),
    path('assign_report/', views.assign_report, name='assign_report'),
    
    
   
     
    
]
