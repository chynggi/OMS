from django.contrib import admin
from OMS.models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    '''
    userid = models.CharField(max_length=30,unique=True);
    password = models.CharField(max_length=50);
    name = models.CharField(max_length=50);
    phone = models.CharField(max_length=50);
    postal = models.CharField(max_length=5);
    address= models.CharField(max_length=300);
    address_ex1= models.CharField(max_length=300);
    address_ex2= models.CharField(max_length=300);
    '''
    #fields = ['title','name','cdate'] # 나열순서에 의해 form에 반영
    list_display = ('userid','name','phone','postal','address','address_ex1','address_ex2')
    list_filter = ['postal']
    search_fields = ['userid','name','phone','postal','address','address_ex1','address_ex2']
    
class BusinessAdmin(admin.ModelAdmin):
    '''
    regno1 = models.CharField(max_length=3);
    regno2 = models.CharField(max_length=2);
    regno3 = models.CharField(max_length=5);
    name = models.CharField(max_length=50);
    code = models.CharField(max_length=4);
    address = models.CharField(max_length=200);
    '''
    #fields = ['title','name','cdate'] # 나열순서에 의해 form에 반영
    list_display = ('regno1','regno2','regno3','name','code','address')
    list_filter = ['id']
    search_fields = ['userid','name','phone','postal','address','address_ex1','address_ex2']    
class ProductAdmin(admin.ModelAdmin):
    '''
    name = models.CharField(max_length=50);
    category = models.CharField(max_length=50);
    units = models.PositiveIntegerField(default=0)
    busno = models.ForeignKey(BusinessInfo,on_delete=models.CASCADE);
    '''
    #fields = ['title','name','cdate'] # 나열순서에 의해 form에 반영
    list_display = ('name','category','units','busno')
    list_filter = ['id']
    search_fields = ['name','category','units','busno']  
class OrderAdmin(admin.ModelAdmin):
    '''
    date = models.DateTimeField();
    cusno = models.ForeignKey(Customer,on_delete=models.CASCADE)
    prodno = models.ForeignKey(ProdInfo,on_delete=models.CASCADE)
    units = models.PositiveIntegerField(default=0)
    '''
    #fields = ['title','name','cdate'] # 나열순서에 의해 form에 반영
    list_display = ('date','cusno','prodno','units')
    list_filter = ['id']
    search_fields = ['date','cusno','prodno','units']  
class PriceAdmin(admin.ModelAdmin):
    '''
    regno1 = models.CharField(max_length=3);
    regno2 = models.CharField(max_length=2);
    regno3 = models.CharField(max_length=5);
    name = models.CharField(max_length=50);
    code = models.CharField(max_length=4);
    address = models.CharField(max_length=200);
    '''
    #fields = ['title','name','cdate'] # 나열순서에 의해 form에 반영
    list_display = ('prodno','start','end','price','unit')
    list_filter = ['id']
    search_fields = ['prodno','start','end','price','unit']  
 
    
    
    

# Register your models here.
admin.site.register(Customer,CustomerAdmin);
admin.site.register(BusinessInfo,BusinessAdmin);
admin.site.register(ProdInfo,ProductAdmin);
admin.site.register(OrderInfo,OrderAdmin);
admin.site.register(PriceInfo,PriceAdmin);