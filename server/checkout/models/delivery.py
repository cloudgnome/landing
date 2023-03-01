from django.db import models
from django.utils import timezone
from user.models import Language

__all__ = ['City','Address','Department','Payment','Status']

class City(models.Model):
    name = models.CharField(max_length = 255)
    language = models.ForeignKey(Language)
    last_modified = models.DateTimeField(auto_now_add = True)

    def dict(self):
        return {'id':self.id,'name':self.name}

    def __str__(self):
        return self.name

    def save(self):
        self.last_modified = timezone.now()

        super().save()

class Address(models.Model):
    name = models.CharField(max_length = 255)
    city = models.ForeignKey(City)
    language = models.ForeignKey(Language, on_delete = models.SET_NULL)

    class Meta:
        unique_together = (name, language, city)

class Department(models.Model):
    name = models.CharField(max_length = 255)
    city = models.ForeignKey(City, related_name = 'departments', on_delete = models.CASCADE)
    address = models.ManyToMany(Address, on_delete = models.SET_NULL)
    last_modified = models.DateTimeField(auto_now_add = True)
    number = models.PositiveIntegerField(null = True) # - is this still needed? 

    def dict(self):
        return {'id':self.id,'address':self.address,'city':self.city.id}

    def __str__(self):
        return self.name

    def save(self):
        self.last_modified = timezone.now()

        super().save()

class Payment(models.Model):
    name = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)

    class Meta:
        verbose_name = _("Тип оплати")

class Status(models.Model):
    name = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)

    class Meta:
        verbose_name = _("Статус замовлення")