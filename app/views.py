from django.shortcuts import render

def condition(request):
    dict={'name':'ammu','age':19,'a':10,'marks':45,'grade':'B'}
    return render(request,'condition.html',context=dict)

# Create your views here.
