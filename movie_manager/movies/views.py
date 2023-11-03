from django.shortcuts import render
from . models import MovieInfo
from django.shortcuts import redirect

# Create your views here.
from . forms import MovieForm


# def create(request):
#     frm=MovieForm()
#     if request.POST:
#         frm=MovieForm(request.POST)
#         if frm.is_valid():
#             frm.save()
#         else:
#             frm=MovieForm()
#     return render(request,'create.html',{'frm':frm})

def create(request):
    frm = MovieForm()
    if request.method == 'POST':
        frm = MovieForm(request.POST, request.FILES)  
        if frm.is_valid():
            frm.save()
        else:
            frm=MovieForm()
    return render(request, 'create.html', {'frm': frm})


def list(request):
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})

def edit(request,pk):
    edt=MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=edt)
        if frm.is_valid():
            edt.save()
    else:
        frm=MovieForm(instance=edt)
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})
