from django.shortcuts import render, redirect
from .models import School
from .forms import SchoolFrom

# Create your views here.


def school(request):
    school = School.objects.all()
    if request.method == 'POST':
        form = SchoolFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SchoolFrom()
    context = {
        'school': school,
        'form': form
    }
    return render(request, 'school/school.html', context)
