from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator ,  MinValueValidator
from django.db import models

STATE_CH = (
   ('AndhraPradesh' ,'AndhraPradesh'), ('ArunachalPradesh' , 'ArunachalPradesh'), ('Assam' , 'Assam'), ('Bihar' , 'Bihar'), ('Goa' , 'Goa'), ('Gujarat' , 'Gujarat'), ('Kerala' , 'Kerala'), ('Maharashtra', 'Maharashtra'), ('Punjab' , 'Punjab'), ('Rajasthan' , 'Rajasthan'), ('TamilNadu' , 'TamilNadu')
)


class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city =models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField( max_length= 50 , choices = STATE_CH ) 
    
    
    def _str_(self):
        return str(self.id)
    
    
CATEGORY_CHOICES = (
        ("G" , " Glasses"),
        ("H" , " Hats"),
        ("S" , "Shirts"),
        ("T" , "Topwear"),
    )
    
    
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(  choices = CATEGORY_CHOICES  , max_length = 2 )
    Product_image = models.ImageField(upload_to="productimg")
    
    def _str_(self):
        return str(self.id)
    
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    Product = models.ForeignKey(Product , on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    
    
    def _str_(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.Quantity * self.Product.discounted_price
    
    
STATUS_CHOICES = (
        ("Accepted" , "Accepted"),                                         
        ("Packed" , "Packed"),
        ("Ontheway" , "Ontheway"),
        ("Cancel" , "Cancel")
)
    
    
    
    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES, default="Pending")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    