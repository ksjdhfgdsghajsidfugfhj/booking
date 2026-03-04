from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=
                                           [MaxValueValidator(18), MinValueValidator(75)], default=0)
    phone_number = PhoneNumberField(region='KG', default='+996')
    USER_STATUS = (
    ('client', 'client'),
    ('owner', 'owner'),
    )
    status = models.CharField(choices=USER_STATUS, default='client', max_length=20)

class Country(models.Model):
    country_name = models.CharField(max_length=32)
    country_image = models.ImageField(upload_to='country_images/')

    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=32)
    city_image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return self.city_name

class Services(models.Model):
    service_name = models.CharField(max_length=32)
    service_image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.service_name

class Hotels(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_hotel')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_hotel')
    hotel_name = models.CharField(max_length=32)
    hotel_image = models.ImageField(upload_to='hotel_images/')
    address = models.CharField(max_length=256)
    services = models.ManyToManyField(Services)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}: {self.hotel_name}'

class ImageHotel(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')

class Room(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=32)
    ROOM_TYPE = (
    ('Семейный', 'Семейный'),
    ('Одноместный', 'Одноместный'),
    ('Двухместный', 'Двухместный'),
    ('Люкс', 'Люкс')
    )
    room_type = models.CharField(choices=ROOM_TYPE, max_length=20)
    ROOM_STATUS = (
    ('Свободный', 'Свободный'),
    ('Забронировано', 'Забронировано')
    )
    room_status = models.CharField(choices=ROOM_STATUS, max_length=20, default='Свободный')
    room_image = models.ImageField(upload_to='room_images/')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)

class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_room/')

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)], default=1)

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    grown_ups = models.PositiveSmallIntegerField(default=0)
    children = models.PositiveSmallIntegerField(default=0)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=
                                           [MaxValueValidator(18), MinValueValidator(75)], default=0)
    phone_number = PhoneNumberField(region='KG', default='+996')
    USER_STATUS = (
    ('client', 'client'),
    ('owner', 'owner'),
    )
    status = models.CharField(choices=USER_STATUS, default='client', max_length=20)

class Country(models.Model):
    country_name = models.CharField(max_length=32)
    country_image = models.ImageField(upload_to='country_images/')

    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=32)
    city_image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return self.city_name

class Services(models.Model):
    service_name = models.CharField(max_length=32)
    service_image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.service_name

class Hotels(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_hotel')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_hotel')
    hotel_name = models.CharField(max_length=32)
    hotel_image = models.ImageField(upload_to='hotel_images/')
    address = models.CharField(max_length=256)
    services = models.ManyToManyField(Services)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}: {self.hotel_name}'

class ImageHotel(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')

class Room(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=32)
    ROOM_TYPE = (
    ('Семейный', 'Семейный'),
    ('Одноместный', 'Одноместный'),
    ('Двухместный', 'Двухместный'),
    ('Люкс', 'Люкс')
    )
    room_type = models.CharField(choices=ROOM_TYPE, max_length=20)
    ROOM_STATUS = (
    ('Свободный', 'Свободный'),
    ('Забронировано', 'Забронировано')
    )
    room_status = models.CharField(choices=ROOM_STATUS, max_length=20, default='Свободный')
    room_image = models.ImageField(upload_to='room_images/')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)

class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_room/')

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)], default=1)

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    grown_ups = models.PositiveSmallIntegerField(default=0)
    children = models.PositiveSmallIntegerField(default=0)
