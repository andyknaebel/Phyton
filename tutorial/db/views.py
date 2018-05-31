from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import todoForm
from .models import todo

# Create your views here.
# THis first example is just a direct reponse 
# That can be used for simple testing
def dbview(request):
    return HttpResponse('got db app base')


# This example is more realistic / real life
# example of calling a html page where full
# interactivity can be programed
def dataview(request):
    todos = todo.objects.all()
    title = 'listing all todos'
    args = {'title': title, 'todos': todos}
    return render(request, 'db/datapage.html', args)


def add_data(request):
    if request.method != "POST":
        form = todoForm()
        args = {'form': form}
        return render(request, 'db/add_data.html', args)
    else:
        form = todoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
        return redirect('/db/data')