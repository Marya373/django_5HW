from django.core.management.base import BaseCommand
from shopapp.models import Client

class Command(BaseCommand):
    help = "Creat client"

    def handle(self, *args, **kwargs):
        client = Client(name='Mary', email='8926@gmail.com', phone_number='79850005611')

        self.stdout.write(f'{client}')

        client.save()