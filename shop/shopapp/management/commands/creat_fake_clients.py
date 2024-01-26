from shopapp.models import Client
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create fake clients"

    def add_arguments(self, parser):

        parser.add_argument('quantity', type=int, help='Create fake clients')

    def handle(self, *args, **kwargs):

        quantity: int = kwargs.get('quantity')

        for i in range(quantity):
            one_client = \
                Client(name=f'name_{i}',
                       email=f'name_{i}@email.com',
                       phone_number=800+i,
                       address=f'address_for_name_{i}')

            self.stdout.write(str(one_client))

            one_client.save()