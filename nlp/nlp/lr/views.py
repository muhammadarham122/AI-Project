from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import numpy as np
from . forms import predForm
from django.core import serializers
from rest_framework import status
from rest_framework import viewsets, status
from django.contrib import messages
from .models import endpoint
from .serializers import endpointSerializer
from io import StringIO
import pickle
import joblib


def form(request):
    return render(request, 'forms.html')


class EndpointView(viewsets.ModelViewSet):
    serializer_class = endpointSerializer
    queryset = endpoint.objects.all()


# def prediction(request, firstName, lastName, income, age,
#                rooms, bedrooms, population, price):
#     # myDict = (request.POST).dict()
#     # x = [['firstName', 'lastName', 'income', 'age',
#     #       'rooms', 'bedrooms', 'population', 'price']]
#     mydata = joblib.load(
#         'D:/AI Project/nlp/nlp/lr/linear.pkl')
#     mydata = request.form.values
#     # unit = np.array(list(mydata.values()))
#     # unit = unit.reshape(1, -1)
#     data = mydata.predict([[income, age, rooms,
#                             bedrooms, population]])
#     print(data)


def houseprice(request):
    if request.method == "POST":
        form = predForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            income = form.cleaned_data['income']
            age = form.cleaned_data['age']
            rooms = form.cleaned_data['rooms']
            bedrooms = form.cleaned_data['bedrooms']
            population = form.cleaned_data['population']
            price = form.cleaned_data['price']
            mydata = joblib.load(
                'D:/AI Project/nlp/nlp/lr/linear.pkl')
            #mydata = request.form.values
            # unit = np.array(list(mydata.values()))
            # unit = unit.reshape(1, -1)
            data = mydata.predict([[income, age, rooms,
                                    bedrooms, population]])
            print(data)
            print(income)
            print(age)
            print(rooms)

    form = predForm()

    return render(request, 'forms.html', {'form': form})
