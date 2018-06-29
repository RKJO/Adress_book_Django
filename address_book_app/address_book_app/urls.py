"""address_book_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from address_book.views import address_book, contact_details, edit_contact, delete_contact, add_contact, group_list, \
    create_group


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^address_book/', address_book),
    re_path(r'^contact_details/(?P<contact_id>\d+)', contact_details),
    re_path(r'^edit_contact/(?P<contact_edit_id>\d+)', edit_contact),
    re_path(r'^delete_contact/(?P<contact_delete_id>\d+)', delete_contact),
    re_path(r'^add_contact/', add_contact),
    re_path(r'^create_group/', create_group),
    re_path(r'^group_list/', group_list),
]
