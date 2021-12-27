from django.db import models

class ProductList (models.Model):
     
    brand_name = models.CharField(max_length=200,null=True, verbose_name = 'Brand Name')
    model_name = models.CharField(max_length=200,null=True, verbose_name = 'Model')
    display = models.CharField(max_length=200,null=True, verbose_name = 'Display')
    ram = models.CharField(max_length=200,null=True, verbose_name = 'Ram')
    storage = models.CharField(max_length=200,null=True, verbose_name = 'Storage')
    battry = models.CharField(max_length=200,null=True, verbose_name = 'Battery')
    os = models.CharField(max_length=200,null=True, verbose_name = 'Operating System')
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, verbose_name = 'Price')    
    date_entry = models.DateTimeField(auto_now = False, auto_now_add=False,verbose_name ='Date Entry')

    def _str_(self):
        return '%s' % (self.brand_name)
        
    class Meta:
        verbose_name = 'Product List'
        verbose_name_plural = 'Product Lists'

