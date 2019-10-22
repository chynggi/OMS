from django.forms import ModelForm
from OMS.models import *
class Form(ModelForm):
    class Meta:
        model = Customer
        '''
        userid = models.CharField(max_length=30,primary_key=True);
        password = models.CharField(max_length=50);
        name = models.CharField(max_length=50);
        phone = models.CharField(max_length=50);
        postal = models.CharField(max_length=5);
        address= models.CharField(max_length=300);
        address_ex1= models.CharField(max_length=300);
        address_ex2= models.CharField(max_length=300);
        '''
        fields =['userid','password','name','phone','postal','address','address_ex1','address_ex2']

class Formalt(ModelForm):        
    class Meta:
        model = Customer
        '''
        userid = models.CharField(max_length=30,primary_key=True);
        password = models.CharField(max_length=50);
        name = models.CharField(max_length=50);
        phone = models.CharField(max_length=50);
        postal = models.CharField(max_length=5);
        address= models.CharField(max_length=300);
        address_ex1= models.CharField(max_length=300);
        address_ex2= models.CharField(max_length=300);
        '''
        fields =['userid','password']
        

class Form2(ModelForm):
    class Meta:
        model = OrderInfo
        '''
        date = models.DateTimeField();
        cusno = models.ForeignKey(Customer,on_delete=models.CASCADE)
        prodno = models.ForeignKey(ProdInfo,on_delete=models.CASCADE)
        '''
        fields =['date','cusno','prodno','units']
        
class Form3(ModelForm):
    class Meta:
        model = BusinessInfo
        '''
        regno1 = models.CharField(max_length=3);
        regno2 = models.CharField(max_length=2);
        regno3 = models.CharField(max_length=5);
        name = models.CharField(max_length=50);
        code = models.CharField(max_length=4);
        address = models.CharField(max_length=200);
        '''
        fields =['regno1','regno2','regno3','name','code','address']
        
class Form4(ModelForm):
    class Meta:
        model = ProdInfo
        '''
        name = models.CharField(max_length=50);
        category = models.CharField(max_length=50);
        units = models.PositiveIntegerField(default=0)
        busno = models.ForeignKey(BusinessInfo,on_delete=models.CASCADE);
        '''
        fields =['name','category','units','busno']
        
class Form5(ModelForm):
    class Meta:
        model = PriceInfo
        '''
        prodno = models.ForeignKey(ProdInfo,on_delete=models.CASCADE);
        start = models.DateTimeField();
        end = models.DateTimeField();
        price = models.PositiveIntegerField(default=0)
        unit = models.CharField(max_length=50);
        '''
        fields =['prodno','start','end','price','unit']                