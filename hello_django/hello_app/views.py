from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_hello(request):
    movie_data={'movies':[{
        'title':'Godfather',
        'year':1990,
        'summary':'story of nice',
        'success' :False
    },
    {'title':'Into The Wild',
        'year':1990,
        'summary':'story of nice',
        'success' :False},
        {'title':'Jungle',
        'year':1990,
        'summary':'story of nice',
        'success' :False},
        {'title':'Martian',
        'year':1990,
        'summary':'story of nice',
        'success' :False}]}
    return render(request, 'hello.html',movie_data)

