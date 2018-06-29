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
    email = Email.objects.all()
    result += """<table>
                        <tr>
                            <th width=20><b>ID</b></th>
                            <th width=70><b>First and Last Name</b></th>
                            <th width=120><b>Address</b></th>
                            <th width=120><b>Groups</b></th>                            
                            <th width=100><b>Phone</b></th>
                            <th width=100><b>Email</b></th>
                        </tr>
                            """
    for person in persons:
        result += """
                        <tr>
                            <td>{}</td>
                            """.format(person.id)
        result += """       <td><a href='/contact_details/{}'><b>{} {}</b></a></td>
                            <td>{} {} {} <br>{}</td>                                        
                            <td>{}</td>                                        
                        """.format(person.id,
                                   person.first_name,
                                   person.last_name,
                                   person.address.street,
                                   person.address.building_num,
                                   person.address.flat_num,
                                   person.address.city,
                                   person.group.name)
        result += "<td>"
        for phones in phone.filter(person=person.id):
            result += """{}: {}<br>""".format(phones.type, phones.phone_number)
        result += "</td>"

        result += "<td>"
        for emails in email.filter(person=person):
            result += """{}: {}<br>""".format(emails.type, emails.email_address)
        result += "</td>"

        result += """<td>
                        <form action="edit_contact/{}">
                            <input type="submit" value="Edit">
                        </form>
                        <form action="delete_contact/{}">
                            <input type="submit" value="Delete">
                        </form></td></tr>"""
    result += """ </table><form action="add_contact/">
                    <input type="submit" value="Add">
                </form>"""
    result += html_end

    return HttpResponse(result)


def group_list(request):
    pass


def contact_details(request, contact_id):
    person_detail = Person.objects.get(id=contact_id)
    person_phone = Phone.objects.filter(person__id=contact_id)
    person_email = Email.objects.filter(person__id=contact_id)
    result = html_start
    result += """<p><b>ID: </b>{}</p>
                <p><b>First and Last Name: </b>{} {}</p>
                <p><b>Description: </b>{}</p>
                <p><b>Address: </b>{} {} {} <br>{}</p>
                <p><b>Groups: </b>{}</p>
                <p><b>Phone numbers: </b>""".format(person_detail.id,
                                                    person_detail.first_name,
                                                    person_detail.last_name,
                                                    person_detail.description,
                                                    person_detail.address.street,
                                                    person_detail.address.building_num,
                                                    person_detail.address.flat_num,
                                                    person_detail.address.city,
                                                    person_detail.group.name)
    for phones in person_phone:
        result += "{}, {} <br>".format(phones.type, phones.phone_number)
    result += """</p>
                <p><b>Emails: </b>"""

    for emails in person_email:
        result += "{}, {} <br>".format(emails.type, emails.email_address)
    result += "</p>"
    result += """<form action="edit_contact/{}">
                    <input type="submit" value="Edit">
                </form>
                <form action="delete_contact/{}">
                    <input type="submit" value="Delete">
                </form>
                <form action="address_book">
                    <input type="submit" value="Powrót">
                </form>""" + html_end

    return HttpResponse(result)

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
