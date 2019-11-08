from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import post, ourevents
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect


def home(request):
    listofevents = {
        'events': ourevents.objects.all()
        }
    return render(request,'eventcyrcle/home.html', listofevents)

class EventListView(ListView):
    model = ourevents
    template_name = 'eventcyrcle/home.html'
    context_object_name = 'events'

class PostDetailView(DetailView):
    model = post

class PostCreateView(CreateView):
    model = post
    fields = ['name', 'company', 'ctype', 'industry', 'Interest']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def about(request):
    return render(request,'eventcyrcle/about.html')

def ecards(request):
    return render(request,'eventcyrcle/ebussinescards.html')
    
def testinfopage(request):
    uu = []
    for e in post.objects.all():
        uu.append(e.author)
    if request.user in uu:
        people = {
            'posts': post.objects.all()
            }
        #return render(request,'eventcyrcle/home.html', people)
        return render(request,'eventcyrcle/testinfopage.html',people)
    else:
        return HttpResponseRedirect(reverse ('post-create'))

def joinfirst_event(request):
    form = EventIDform()
    return render(request,'eventcyrcle/joinfirst_event.html', {'form': form})



