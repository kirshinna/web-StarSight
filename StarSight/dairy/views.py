from django.shortcuts import render, redirect
from .models import Observation
from .form import ObservationForm

def add_observation(request):
    if request.method == "POST":
        form = ObservationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("observations_list")
    else:
        form = ObservationForm()

    return render(request, "dairy/add_observation.html", {"form": form})

def observations_list(request):
    observations = Observation.objects.order_by('-date')
    return render(request, "dairy/dairy_home.html", {"observations": observations})
