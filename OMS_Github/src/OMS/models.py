from django.db import models

# Create your models here.

#class Postal(models.Model):
    #postal = models.PositiveIntegerField(default=0,primary_key=True)
    #address_sn = models.CharField(max_length=300);
    #address = models.CharField(max_length=300);

class Customer(models.Model):
    class Meta:
        unique_together = (('id','userid'))
    userid = models.CharField(max_length=30,unique=True);
    password = models.CharField(max_length=50);
    name = models.CharField(max_length=50);
    phone = models.CharField(max_length=50);
    postal = models.CharField(max_length=5);
    address= models.CharField(max_length=300);
    address_ex1= models.CharField(max_length=300);
    address_ex2= models.CharField(max_length=300);
    def __str__(self):
        return self.name;
    
class BusinessInfo(models.Model):
    regno1 = models.CharField(max_length=3);
    regno2 = models.CharField(max_length=2);
    regno3 = models.CharField(max_length=5);
    name = models.CharField(max_length=50);
    code = models.CharField(max_length=4);
    address = models.CharField(max_length=200);
    def __str__(self):
        return self.name;
    
class ProdInfo(models.Model):
    name = models.CharField(max_length=50);
    category = models.CharField(max_length=50);
    units = models.PositiveIntegerField(default=0)
    busno = models.ForeignKey(BusinessInfo,on_delete=models.CASCADE);
    def __str__(self):
        return self.name;

class OrderInfo(models.Model):
    date = models.DateTimeField();
    cusno = models.ForeignKey(Customer,on_delete=models.CASCADE)
    prodno = models.ForeignKey(ProdInfo,on_delete=models.CASCADE)
    units = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name;
    
class PriceInfo(models.Model):
    class Meta:
        unique_together = (('prodno','start','end'))
    prodno = models.ForeignKey(ProdInfo,on_delete=models.CASCADE);
    start = models.DateTimeField();
    end = models.DateTimeField();
    price = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50);
    def __str__(self):
        return self.price;
    


