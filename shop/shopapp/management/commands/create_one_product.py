from decimal import Decimal
from shopapp.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create one product"

    def add_arguments(self, parser):

        parser.add_argument('name', type=str, help='Name product')
        parser.add_argument('description', type=str, help='Description product')
        parser.add_argument('price', type=str, help='Price product')
        parser.add_argument('quantity', type=int, help='Quantity product')

    def handle(self, *args, **kwargs):

        name: str = kwargs.get('name')
        description: str = kwargs.get('description')
        price: str = kwargs.get('price')
        decimal_price: Decimal = Decimal(price)
        quantity: int = kwargs.get('quantity')

        product = \
            Product(name=name,
                    description=description,
                    price=decimal_price,
                    quantity=quantity)

        self.stdout.write(str(product))

        product.save()