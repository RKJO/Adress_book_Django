from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return "{}".format(self.name)


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    building_num = models.IntegerField()
    flat_num = models.IntegerField(null=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.city, self.street, self.building_num, self.flat_num)


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    description = models.CharField(max_length=120, null=True)
    group = models.ManyToManyField(Group)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.first_name, self.last_name, self.description, self.group)


class Phone(models.Model):
    phone_number = models.IntegerField()
    type = models.CharField(max_length=15)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}, {}".format(self.phone_number, self.type, self.person)


class Email(models.Model):
    email_address = models.EmailField()
    type = models.CharField(max_length=15)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}, {}".format(self.email_address, self.type, self.person)

