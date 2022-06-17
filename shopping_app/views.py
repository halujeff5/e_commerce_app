from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from challenges.models import blazers, t_shirts, shirts, sweaters
# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def index (request):
    return render (request, 'index.html')
def shirt(request):

    my_data = shirts.objects.all() #for all the records 
    one_data = shirts.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    context={
       
      'my_data':my_data,
      'one_data':one_data,
    
    } 
    return render(request, 'shirts.html', context)
def t_shirt(request):

    my_data = t_shirts.objects.all() #for all the records 
    one_data = t_shirts.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    context={
       
      'my_data':my_data,
      'one_data':one_data,
    
    } 
    return render(request, 't_shirts.html', context)
def shirt(request):

    my_data = shirts.objects.all() #for all the records 
    one_data = shirts.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    context={
       
      'my_data':my_data,
      'one_data':one_data,
    
    } 
    return render(request, 'shirts.html', context)
def sweater(request):

    my_data = sweaters.objects.all() #for all the records 
    one_data = sweaters.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    context={
       
      'my_data':my_data,
      'one_data':one_data,
    
    } 
    return render(request, 'sweaters.html', context)

def upload(request):
    return render (request, 'upload.html')
def checkout(request):
    return render (request, 'checkout.html')

def blazer(request):

    my_data = blazers.objects.all() #for all the records 
    one_data = blazers.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    context={
       
      'my_data':my_data,
      'one_data':one_data,
    
    } 

    return render(request, 'blazers.html', context)
 
