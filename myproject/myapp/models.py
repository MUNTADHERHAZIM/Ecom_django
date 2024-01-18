from django.db import models
import datetime
# Create your models here.

class category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class customer (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'customers'
        


class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	image = models.ImageField(upload_to='uploads/product/')
	# Add Sale Stuff
	is_sale = models.BooleanField(default=False)
	sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

	def __str__(self):
		return self.name     



class order (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.TextField(max_length=100, null=True, blank=True ,default='')
    phone = models.CharField(max_length=50 , null=True, blank=True ,default='')
    date = models.DateField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.name
    