from django.shortcuts import render,HttpResponse
from.models import MovieInfo
from django.shortcuts import redirect

# Create your views here.
from.forms import MovieForm

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
    recent_visits=request.session.get('recent_visits', [])
    count=request.session.get('count',0)
    count=int(count)
    count=count + 1
    request.session['count']=count
    recent_movie_set=MovieInfo.objects.filter(pk__in=recent_visits)
    movie_set=MovieInfo.objects.all()
    response=render(request,'list.html',{
        'recent_movie_set':recent_movie_set,
        'movies':movie_set,'visits':count})
    return response

def edit(request,pk):
    edt=MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,request.FILES,instance=edt)
        if frm.is_valid():
            edt.save()
    else:
        recent_visits=request.session.get('recent_visits', [])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        frm=MovieForm(instance=edt)
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})
