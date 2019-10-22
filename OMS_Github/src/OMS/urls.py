"""OrderMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name='OMS'
urlpatterns = [ 
    path('delete/<str:tp>/<int:num>/', views.delete,name='delete'),
    path('postal/', views.postal,name='postal'),
    path('signup/', views.signup,name='signup'),
    path('index/', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('postaledit/<int:num>/', views.postedit,name='postaledit'),
    path('postview/<int:num>/', views.postview,name='postalview'),
    path('postresult/', views.postresult,name='postresult'),
    path('Orderreg/', views.Orders,name='Orderreg'),
    path('Orderedit/<int:num>/', views.Ordersedit,name='Orderedit'),
    path('Orderregcus/', views.Orderscus,name='Orderregcus'),
    path('Ordereditcus/<int:num>/', views.Orderscusedit,name='Ordereditcus'),
    path('Orders/', views.Ordersresult,name='Orders'),
    path('orderview/<int:num>/', views.Orderview,name='orderview'),
    path('bussreg/', views.Business,name='bussreg'),
    path('bussedit/<int:num>/', views.Businessedit,name='bussedit'),
    path('business/', views.Bussresult,name='business'),
    path('bussview/<int:num>/', views.Bussview,name='bussview'),
    path('prodreg/', views.Product,name='prodreg'),
    path('prodedit/<int:num>/', views.Productedit,name='prodedit'),
    path('product/', views.Prodresult,name='product'),
    path('prodview/<int:num>/', views.Prodview,name='prodview'),
    path('pricereg/', views.Price,name='pricereg'),
    path('priceedit/<int:num>/', views.Priceedit,name='priceedit'),
    path('price/', views.Priceresult,name='price'),
    path('priceview/<int:num>/', views.Priceview,name='priceview'),
    
]
