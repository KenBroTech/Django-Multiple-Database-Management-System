from django.shortcuts import render, redirect
from .models import Club
from .forms import ClubForm

# Create your views here.


def club(request):
    club = Club.objects.all()
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('club')
    else:
        form = ClubForm()
    context = {
        'club': club,
        'form': form,
    }
    return render(request, 'club/club.html', context)
