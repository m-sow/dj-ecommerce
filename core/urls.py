from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('checkout/', views.CheckoutView.as_view(), name="checkout"),
    path('order-summary/', views.OrderSummaryView.as_view(), name="order-summary"),
    path('product/<slug>/', views.ItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>/', views.add_to_cart, name="add-to-cart"),
    path('remove_from_cart/<slug>', views.remove_from_cart, name="remove-from-cart"),
    path('remove_item_from_cart/<slug>', views.remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name="payment"),
]
