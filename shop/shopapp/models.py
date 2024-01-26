from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

for_phone_number_validation =\
    RegexValidator(
        regex=r"^[0-9]{3,11}$",
        message="Номер состоит из символов и цифр"
        "в количестве 11"
    )

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(validators=[for_phone_number_validation], max_length=11)
    address = models.TextField()
    date_time_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client(' \
        f'name: {self.name}, '\
        f'email: {self.email}, '\
        f'phone number: '\
        f'{self.phone_number}, '\
        f'address: {self.address}, '\
        f'date time registration: '\
        f'{self.date_time_registration}, '\
        f')'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=10)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    date_time_additions_product = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos_products/', blank=True, null=True)
    
   

    def __str__(self):
        return f'Product(' \
        f'name: {self.name}, ' \
        f'price: {self.price}, ' \
        f'quantity: {self.quantity}, '\
        f'date time additions product: ' \
        f'{self.date_time_additions_product}' \
        f')'
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    total_amount_order = models.DecimalField(max_digits=20, decimal_places=10)
    date_time_placing_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        product_count: int = self.product.count()
        product_list: str =', '.join(str(product) for product in self.product.all())
            
        return f'Order(' \
            f'client: {self.client}, ' \
            f'product count: {product_count}, ' \
            f'product list: {product_list}, ' \
            f'total amount order: {self.total_amount_order}, ' \
            f'date time placing order: {self.date_time_placing_order}, ' \
            f')'
    

        

        



