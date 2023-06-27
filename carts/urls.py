from django.urls import path
from . import views
urlpatterns = [
    path('',views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    
    # path('<slug:category_slug>/',views.store, name='product_by_category'),
    # path('<slug:category_slug>/<slug:product_slug>/',views.product_details, name='product_details')
]
