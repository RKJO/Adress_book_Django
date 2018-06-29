from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exemp
# Create your views here.

form = """<form action="http://google.com">
        <input type="submit" value="Go to Google" />
        </form>"""


def address_book(request):  # all contacts
    pass


def group_list(reuest):
    pass


def contact_details(request, contact_id):
    pass


def edit_contact(request, contact_edit_id):
    pass
    # przekierowanie do strony contact_details
    # dodania lub usunięcia nowego adresu, maila lub telefonu dla niej.
    # usuniecie danych
    # Możliwość dodania użytkownika do wielu grup.


def delete_contact(request, contact_delete_id):
    pass
    # przekierowanie do strony address_book

"""from time import sleep
sleep(60) # Delay for 1 minute (60 seconds).
sleep(0.1) # Time in seconds."""


def add_contact(request):
    pass
    # przekierowanie do strony contct_details


def create_group(request):
    pass
    # Możliwość dodania do grupy wielu użytkowników.
