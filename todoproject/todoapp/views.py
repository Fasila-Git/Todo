from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

# class based views
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'entire_tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'ts'
    fields = ('taskName', 'taskPriority', 'taskDate')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# function based views
def add(request):
    all_tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date', '')
        tasks = Task(taskName=name, taskPriority=priority,taskDate=date)
        tasks.save()

    return render(request, 'home.html',{'entire_tasks':all_tasks})

# def details(request):
#
#     return render(request,'details.html',)
def delete(request,taskId):
    task=Task.objects.get(id=taskId)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def edit(request,id):
    tasks=Task.objects.get(id=id)
    forms=Todoform(request.POST or None,instance=tasks)
    if forms.is_valid():
        forms.save()
        return  redirect('/')
    return render(request,'edit.html',{'editForm':forms, 'editTask':tasks})


