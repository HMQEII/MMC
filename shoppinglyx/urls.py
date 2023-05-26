# from django.contrib import admin
# from django.urls import path, include
# from app import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_view
# from app.forms import LoginForm


# urlpatterns = [
    
#     path('', views.home),
#     path('product-detail/' , views.product_detail, name = 'product-detail'),
#     path('cart/' , views.add_to_cart , name = 'add-to-cart'),
#     path('buy/' , views.buy_now , name = 'but-now'),
#     path('profile/' , views.profile , name = 'profile'),
#     path('address/' , views.address , name = 'address'),
#     path('orders/' , views.orders , name = 'orders'),
#     path('changepassword/' , views.mobile , name = 'mobile'),
#     path('login/' , views.login , name = 'login'),
#     # path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
#     path('registration/' , views.CustomerRegistrationView.as_view(), name = 'customerregistration'),
#     path('checkout/' , views.checkout, name = 'checkout'),
    
  
        
#     path('admin/', admin.site.urls),
#     path('', include('app.urls'))
# ]

from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    # path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    
    # path('product-detail/' , views.product_detail, name = 'product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart, name="pluscart"),
    path('buy/' , views.buy_now , name = 'but-now'),
    # path('profile/' , views.profile , name = 'profile'),
    path('address/' , views.address , name = 'address'),
    path('orders/' , views.orders , name = 'orders'),
    path('changepassword/' , views.mobile , name = 'mobile'),
    path('login/' , views.login , name = 'login'),
    path('registration/' , views.CustomerRegistrationView.as_view(), name = 'customerregistration'),
    path('checkout/' , views.checkout, name = 'checkout'),
    path('about/' , views.about, name = 'about'),
    path('chatbot/', views.about, name='chatbot'),
    
    
    
  
        
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
    
    


]   + static ( settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



