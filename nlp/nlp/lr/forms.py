from django import forms


class predForm(forms.Form):
    firstName = forms.CharField(max_length=15)
    lastName = forms.CharField(max_length=15)
    income = forms.IntegerField()
    age = forms.IntegerField()
    rooms = forms.IntegerField()
    bedrooms = forms.IntegerField()
    population = forms.IntegerField()
    price = forms.IntegerField()
