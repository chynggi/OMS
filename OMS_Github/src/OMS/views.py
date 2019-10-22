from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from OMS.forms import *
from OMS.models import *

# Create your views here.

def index(request):
    try:
        if request.session['userid'] is None:
            return render(request,'OMS/index.html');
        else:
            orderlist = OrderInfo.objects.all()
    except KeyError:
        return render(request,'OMS/index.html');                
    return render(request,'OMS/Orders.html',{'orderList':orderlist})
        
def delete(request,tp,num):
    data=None;    
    if tp == 'order':
        data = OrderInfo.objects.get(id=num)
        data.delete();
        return HttpResponseRedirect(reverse('OMS:Orders'))
    elif tp == 'custom':
        data = Customer.objects.get(id=num)
        data.delete();
        return HttpResponseRedirect(reverse('OMS:postresult'))
    elif tp == 'buss':
        data = BusinessInfo.objects.get(id=num)
        data.delete();
        return HttpResponseRedirect(reverse('OMS:business'))
    elif tp == 'prod':
        data = ProdInfo.objects.get(id=num)
        data.delete();
        return HttpResponseRedirect(reverse('OMS:product'))
    elif tp == 'price':
        data = PriceInfo.objects.get(id=num)
        data.delete();
        return HttpResponseRedirect(reverse('OMS:price'))
    else: 
        return HttpResponseRedirect(reverse('OMS:index'))
    
        
    
        
        
def signup(request):
    message = None;
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            message = None;
            form.save()
        else:
            message = "ERROR"
    else:
        form = Form() 
    return render(request,'OMS/signup.html',{'form':form,'message':message})

def login(request):
    message = None;
    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['password']
        if Customer.objects.get(userid=username,password=password):
            request.session['userid'] = username;
            return HttpResponseRedirect(reverse('OMS:Orders'))
        else:
            message="ERROR"
    else:
        form = Formalt() 
    return render(request,'OMS/login.html',{'form':form,'message':message})

def logout(request):
    request.session['userid'] = None;
    return HttpResponseRedirect(reverse('OMS:index'))

def postal(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form() 
    return render(request,'OMS/posttest.html',{'form':form})


def postresult(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    customList = Customer.objects.all()
    return render(request,'OMS/postresult.html',{'customList':customList})

def postview(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    custom = Customer.objects.get(id=num)
    return render(request,'OMS/Postview.html',{'custom':custom})

def postedit(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    custom = Customer.objects.get(id=num)
    if request.method == 'POST':
        form = Form(request.POST,instance=custom)
        if form.is_valid():
            form.save()
    else:
        form = Form()     
    return render(request,'OMS/posttest.html',{'form':form,'custom':custom})

def Orders(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    if request.method == 'POST':
        form = Form2(request.POST)
        
        if form.is_valid():
            
            form.save()
    else:
        form = Form2() 
        
    customList = None
    if request.session['userid'] is "admin":
        customList = Customer.objects.all()
    else:
        customList = Customer.objects.filter(userid=request.session['userid'])
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/Orderreg.html',{'form':form,'customList':customList,'prodlist':prodlist})

def Orderscus(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    if request.method == 'POST':
        form = Form2(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form2() 
    user = Customer.objects.get(userid=request.session['userid'])
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/Orderreg_cus.html',{'form':form,'prodlist':prodlist,'user':user})

def Ordersedit(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    order= OrderInfo.objects.get(id=num)
    if request.method == 'POST':
        form = Form2(request.POST,instance=order)
        if form.is_valid():
            form.save()
    else:
        form = Form2()     
    customList = Customer.objects.all()
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/Orderreg.html',{'form':form,'order':order,'customList':customList,'prodlist':prodlist})

def Orderscusedit(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    order= OrderInfo.objects.get(id=num) 
    if request.method == 'POST':
        form = Form2(request.POST,instance=order)
        if form.is_valid():
            form.save()
    else:
        form = Form2()       
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/Orderreg_cus.html',{'form':form,'order':order,'prodlist':prodlist})



def Ordersresult(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    orderlist = None;
    if request.session['userid'] is "admin":
        orderlist = OrderInfo.objects.all()
    else:
        user = Customer.objects.get(userid=request.session['userid'])
        print(user.id)
        orderlist = OrderInfo.objects.filter(cusno=user.id)
    return render(request,'OMS/Orders.html',{'orderlist':orderlist})

def Orderview(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    order= OrderInfo.objects.get(id=num)
    return render(request,'OMS/OrderView.html',{'order':order})


def Business(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    if request.method == 'POST':
        form = Form3(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form3() 
    return render(request,'OMS/bussreg.html',{'form':form})

def Businessedit(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    buss = BusinessInfo.objects.get(id=num)
    if request.method == 'POST':        
        form = Form3(request.POST,instance=buss)
        if form.is_valid():
            form.save()
    else:
        form = Form3()     
    return render(request,'OMS/bussreg.html',{'form':form,'buss':buss})

def Bussresult(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    busslist = BusinessInfo.objects.all();
    return render(request,'OMS/business.html',{'busslist':busslist})

def Bussview(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    buss = BusinessInfo.objects.get(id=num)
    return render(request,'OMS/bussview.html',{'buss':buss})


def Product(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    if request.method == 'POST':
        form = Form4(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form4() 
    busslist = BusinessInfo.objects.all();
    return render(request,'OMS/prodreg.html',{'form':form,'busslist':busslist})

def Productedit(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    prod = ProdInfo.objects.get(id=num)
    if request.method == 'POST':
        form = Form4(request.POST,instance=prod)
        if form.is_valid():
            form.save()
    else:
        form = Form4()     
    busslist = BusinessInfo.objects.all();
    
    
    
    return render(request,'OMS/prodreg.html',{'form':form,'prod':prod,'busslist':busslist})

def Prodresult(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/product.html',{'prodlist':prodlist})

def Prodview(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    prod = ProdInfo.objects.get(id=num)
    return render(request,'OMS/prodview.html',{'product':prod})

def Price(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    if request.method == 'POST':
        form = Form5(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form5() 
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/pricereg.html',{'form':form,'prodlist':prodlist})

def Priceedit(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    price = PriceInfo.objects.get(id=num)
    if request.method == 'POST':
        form = Form5(request.POST,instance=price)
        if form.is_valid():
            form.save()
    else:
        form = Form5()     
    prodlist = ProdInfo.objects.all()
    return render(request,'OMS/pricereg.html',{'form':form,'price':price,'prodlist':prodlist})

def Priceresult(request):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    pricelist = PriceInfo.objects.all()
    return render(request,'OMS/price.html',{'pricelist':pricelist})

def Priceview(request,num):
    if request.session['userid'] is None:
        return HttpResponseRedirect(reverse('OMS:index'))
    price = PriceInfo.objects.get(id=num)
    return render(request,'OMS/PriceView.html',{'prices':price})