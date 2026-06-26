from django.core.management.base import BaseCommand
from core.product_queries import tag_seed, product_seed, category_seed

class Command(BaseCommand):
    help = "Create records for Category, Tag"

    def handle(self, *args, **options):
        self.stdout.write("Start seeding....")
        tag_seed()
        category_seed()
        product_seed()