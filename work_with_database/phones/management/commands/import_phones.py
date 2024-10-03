import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import data from')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))  

        for phone in phones:
            # Создаем объект Phone и сохраняем его в базе данных
            phone_obj = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=parse_date(phone['release_date']),
                lte_exists=phone['lte_exists'].lower() == 'true'  # Преобразуем строку в булевое значение
            )
            phone_obj.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added {phone_obj.name}'))
