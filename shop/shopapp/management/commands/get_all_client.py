from typing import Any
from django.core.management.base import BaseCommand
from shopapp.models import Client

class Command(BaseCommand):
    help = "Get all clients"

    def handle(self, *args: Any, **options: Any):
        clients = Client.objects.all()
        self.stdout.write(f' {clients}')