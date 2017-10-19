from django.core.management.base import BaseCommand
from beers.models import Brewery

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        print('hi')

    """def _createBrewery(self):
        testBrew1 = Brewery(name='Test Brewery 1', address="Address one")
        testBrew1.save()

        testBrew2 = Brewery(name='Test Brewery 2', address="Address two")
        testBrew2.save()

    def handle(self, *args, **options):
        self._createBrewery()"""