# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('update/<int:order_id>/', views.update_order, name='update_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('list/', views.order_list, name='order_list'),
    path('search/', views.search_orders, name='search_orders'),
    # Add URL patterns for user profile, login, and logout views
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    # Add URL patterns for user authentication views
]
