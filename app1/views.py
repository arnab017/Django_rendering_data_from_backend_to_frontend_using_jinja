from django.shortcuts import render

# Create your views here.
d={
    'name1':'Arnab',
    'name2':'Tushar',
    'name3':'David',
}

def home(request):
    return render(request,'home.html',context=d)