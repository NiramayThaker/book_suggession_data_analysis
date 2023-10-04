from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Book
from itertools import islice
import csv
import pandas as pd 
import json


class Command(BaseCommand):
        if not Book.objects.count():
            datafile = settings.BASE_DIR / 'data' / 'book-data.json'

        with open(datafile, 'r') as f:
            data = json.load(f)

        Book_data = []

        for d in data:
            Book_data.append(Book(
                title=d['title'],
                author=d['authors'],
                pageCount=d['pageCount'],
                # publishedDate=d['publishedDate'],
                # shortDescription=d['shortDescription'],
                # longDescription=d['longDescription'],
                categories=d['categories'],
            ))

        Book.objects.bulk_create(Book_data)

