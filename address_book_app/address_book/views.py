from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from address_book.models import Person, Address, Phone, Email, Group
from django.views.decorators.csrf import csrf_exempt
import time
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
                        """.format(person.id,
                                   person.first_name,
                                   person.last_name)
        if person.address.street or person.address.building_num or person.address.flat_num or person.address.city != "":
            result += """<td>{} {} {} <br>{}</td>""".format(
                                       person.address.street,
                                       person.address.building_num,
                                       person.address.flat_num,
                                       person.address.city)
        result += """<td>{}</td>""".format([g.name for g in person.group.all()])
        result += "<td>"
        for phones in phone.filter(person=person.id):
            result += """{}: {}<br>""".format(phones.type, phones.phone_number)
        result += "</td>"

        result += "<td>"
        for emails in email.filter(person=person):
            result += """{}: {}<br>""".format(emails.type, emails.email_address)
        result += "</td>"

        result += """<td>
                        <form>
                            <input type="button" value="Edit" onclick="location.href='/edit_contact/{}'">
                        </form>
                        <form>
                            <input type="button" value="Delete" onclick="location.href='/delete_contact/{}'">
                        </form></td></tr>""".format(person.id, person.id)
    result += """ </table><form>
                    <input type="button" value="Add" onclick="location.href='/add_contact/'">
                    <input type="button" value="group list" onclick="location.href='/group_list/'">
                </form>"""
    result += html_end

    return HttpResponse(result)


def group_list(request):
    result = html_start
    groups = Group.objects.all()
    persons = Person.objects.all()
    result += """<table>
                        <tr>
                            <th width=20><b>ID</b></th>
                            <th width=70><b>Group</b></th>
                            <th width=120><b>Persons</b></th>
                        </tr>
                            """
    for group in groups:
        result += """
                        <tr>
                            <td>{}</td>
                            <td>{}</td>
                            """.format(group.id, group.name)
        for person in persons:
            if [g.id for g in person.group.all()] == group.id:

                result += """       <td>{} {}</td></br>                                     
                                """.format(person.first_name,
                                           person.last_name)
                result += "<td>"
    result += """ </table><form>
                  <input type="button" value="powrót" onclick="location.href='/address_book/'">
                                </form>"""

    result += html_end

    return HttpResponse(result)


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
                                                    [g.name for g in person_detail.group.all()])
    for phones in person_phone:
        result += "{}, {} <br>".format(phones.type, phones.phone_number)
    result += """</p>
                <p><b>Emails: </b>"""

    for emails in person_email:
        result += "{}, {} <br>".format(emails.type, emails.email_address)
    result += "</p>"
    result += """<form action="edit_contact/{}">
                    <input type="submit" value="Edit">
                </form>""".format(contact_id)
    result += """<form action="delete_contact/{}">
                    <input type="submit" value="Delete">
                </form>""".format(contact_id)
    result += """<form action="address_book">
                    <input    type="button" value="Powrót" onclick="location.href='/address_book/'">
                </form>""" + html_end

    return HttpResponse(result)


def edit_contact(request, contact_edit_id):
    pass
    # przekierowanie do strony contact_details
    # dodania lub usunięcia nowego adresu, maila lub telefonu dla niej.
    # usuniecie danych
    # Możliwość dodania użytkownika do wielu grup.


@csrf_exempt
def delete_contact(request, contact_delete_id):
    contact_to_delete = Person.objects.get(id=contact_delete_id)
    result = html_start
    if request.method == "GET":
        # result += """<p>Czy napewno chcesz usuąć ten kontakt?</p><br>
        #                 <form action="#" method="POST">
        #                     <input type="button" name="submit" value="Tak">
        #                     <input type="submit" name="submit" value="Nie" onclick="location.href='/address_book/'">
        #                 </form>"""
        # return HttpResponse(result)

        # if request.method == "POST":
        # answer = request.POST.get("submit")
        # if answer == "Yes":
        "<p>Kontakt {} {} został usunięty".format(contact_to_delete.first_name, contact_to_delete.last_name)
        contact_to_delete.delete()
        # return result

        # result += """<form action="address_book">
        #                 <input    type="button" value="Powrót" onclick="location.href='/address_book/'">
        #             </form>""" + html_end

    return HttpResponseRedirect("address_book")


@csrf_exempt
def add_contact(request):
    answer = html_start
    all_address = Address.objects.all()
    all_phones = Phone.objects.all()
    all_groups = Group.objects.all()
    if request.method == 'GET':
        answer += """<form action="#" method="POST">
                            <label>First Name:</label>
                                <input type="text" name="first_name"><br>
                            <label>Last Name:</label>
                                <input type="text" name="last_name"><br>
                            <label>Description: </label>
                                <input type="text" name="description"><br>
                            <label>Phone: </label>
                                <input type="number" name="phone" placeholder="number">
                                <input type="text" name="phone_type" placeholder="type"><br>
                            <label>Email: </label>
                                <input type="email" name="email" placeholder="email">
                                <input type="text" name="email_type" placeholder="type"><br>
                            <label>Address: </label>
                                <input type="text" name="city" placeholder="City">
                                <input type="text" name="street" placeholder="Street">
                                <input type="text" name="building_num" placeholder="Building Number">
                                <input type="text" name="flat_num" placeholder="Flat number"></br>
                            <label>Group: </label></br>"""
        for group in all_groups:
            answer += """<input type="checkbox" name="group" value="{}">{}<br>""".format(group, group.name)
        answer += """<input type="submit" value="Zapisz">
                            </form>
                            """
        return HttpResponse(answer)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        description = request.POST.get("description")
        city = request.POST.get("city")
        street = request.POST.get("street")
        building_num = request.POST.get("building_num")
        flat_num = request.POST.get("flat_num")
        phone = request.POST.get("phone")
        phone_type = request.POST.get("phone_type")
        email = request.POST.get("email")
        email_type = request.POST.get("email_type")
        group = request.POST.get("group")

        new_person = Person.objects.create(first_name=first_name, last_name=last_name, description=description)
        new_person.save()
        if city or street or building_num != "":
            Address.objects.create(city=city,
                                   street=street,
                                   building_num=building_num,
                                   flat_num=flat_num,
                                   person=new_person)

        if phone != "":
            Phone.objects.create(phone_number=phone,
                                 type=phone_type,
                                 person=new_person)

        if email != "":
            Email.objects.create(email_address=email, type=email_type, person=new_person)

        if group is not None:
            new_person.group.add(group)

        # answer = """<p>GIT</p>"""
        # return HttpResponse(answer)

    return HttpResponseRedirect("contact_details")


#przekierowanie do strony contct_details


def create_group(request):
    pass
    # Możliwość dodania do grupy wielu użytkowników.
