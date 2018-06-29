from django.shortcuts import render
from django.http import HttpResponse
from address_book.models import Person, Address, Phone, Email, Group
# Create your views here.

html_start = """ <html>
                    <head>
                    </head>
                    <body>"""

html_end = """  </body>
            </html>"""


def address_book(request):  # all contacts
    result = html_start
    persons = Person.objects.all()
    phone = Phone.objects.all()

    for person in persons:
        result += """<table>
                        <tr>
                            <td><b>ID</b></td>
                            <td><b>First and Last Name</b></td>
                            <td><b>Address</b></td>
                            <td><b>Phone</b></td>
                            <td><b>Email</b></td>
                            <td><b>Groups</b></td>
                        </td>
                            """
        result += """
                        <tr>
                            <td>{}</td>
                            """.format(person.id)
        result += """       <td><a href='/contact_details/{}'><b>{} {}</b></a></td>
                            <td>{} {} {}<br/> {}<br /></td>
                        
                        """.format(person.id,
                                   person.first_name,
                                   person.last_name,
                                   person.address.street,
                                   person.address.building_num,
                                   person.address.flat_num,
                                   person.address.city)

        # for phone in person.phone:
        #     result += """<td>{}: {}<br/>""".format(phone.type, phone.phone_number)
        # result += "</td>"
        #
        # for email in person.email:
        #     result += """<td>{}: {}<br/>""".format(email.type, email.email_address)
        # result += "</td>"
        #
        # for group in person.group:
        #     result += """<td>{}<br/>""".format(group.name)
        # result += "</td>"
        #
        # result += "</td>"
        result += """<td>
                        <form action="edit_contact/{}">
                            <input type="submit" value="Edit">
                        </form>
                        <form action="delete_contact/{}">
                            <input type="submit" value="Delete">
                        </form></tr></table>"""
    result+=""" <form action="add_contact/">
                    <input type="submit" value="Add">
                </form>"""
    result += html_end

    return HttpResponse(result)


def group_list(request):
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
