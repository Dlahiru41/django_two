from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Task
from .forms import TaskForm

def landing(request):
    return render(request, 'tasks/landing.html')

@login_required
def data_entry(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = TaskForm()
    return render(request, 'tasks/data_entry.html', {'form': form})

@login_required
def dashboard(request):
    tasks = Task.objects.all()
    thirty_days_from_now = timezone.now() + timedelta(days=30)
    urgent_tasks_count = Task.objects.filter(is_urgent=True, due_by__lte=thirty_days_from_now).count()

    # You'll need to add more complex queries here to get data for the charts

    context = {
        'tasks': tasks,
        'urgent_tasks_count': urgent_tasks_count,
        # Add more context data for charts
    }
    return render(request, 'tasks/dashboard.html', context)