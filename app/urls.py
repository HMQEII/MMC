# from django.urls import path
# from app import views
# from django.conf import settings
# from django.conf.urls.static import static



# urlpatterns = [
#     path('', views.home),
#     path('product-detail/', views.product_detail, name='product-detail'),
#     path('cart/', views.add_to_cart, name='add-to-cart'),
#     path('buy/', views.buy_now, name='buy-now'),
#     path('profile/', views.profile, name='profile'),
#     path('address/', views.address, name='address'),
#     path('orders/', views.orders, name='orders'),
#     path('changepassword/', views.change_password, name='changepassword'),
#     path('mobile/', views.mobile, name='mobile'),
#     path('login/', views.login, name='login'),
#     # path('registration/', views.customerregistration, name='customerregistration'),
    
#     path('registration/', views.CustomerRegistrationForm , name='customerregistration'),
    
    
#     path('checkout/', views.checkout, name='checkout'),
# ] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm, MyPasswordChangeform
from django.contrib.auth import views as auth_views
from app.views import ProfileView

urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    # path('',views.ProductView.as_view(),name="home"),
    # path('product-detail/', views.Product, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form =LoginForm), name ='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    
    
    # path('accounts/login/', auth_views.LoginView.as_view ( template_name="app/login.html", authentication_form =LoginForm), name = "login"),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeform),name='passwordchange'),
    
    path('registration/', views.CustomerRegistrationForm, name='customerregistration'),
    
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
    # path('about/', views.about, name='about'),
    
    # path('chatbot/', views.about, name='chatbot'),
    
    
   
    path('checkout/', views.checkout, name='checkout'), ]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    




