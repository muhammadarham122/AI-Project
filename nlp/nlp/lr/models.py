from django.db import models


class endpoint(models.Model):
    firstName = models.CharField(max_length=50, default=' ')
    lastName = models.CharField(max_length=50, default=' ')
    income = models.IntegerField()
    age = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    population = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.lastName, self.firstName)
