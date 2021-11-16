from django.shortcuts import render

from .models import Availability
from .forms import AvailabilityForm
from django.urls import reverse

from django.views.generic import(
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )

# Create your views here.
#delete availability view
class DeleteAvailabilityView(DeleteView):
    template_name='availability/delete-availability.html'
    
    queryset=Availability.objects.all()

    def get_success_url(self):
        return reverse("counsellor:my-availability")

class UpdateAvailabilityView(UpdateView):
    template_name='availability/update-availability.html'
    form_class=AvailabilityForm
    queryset=Availability.objects.all()

    #def get_object(self):
    #id_=self.kwargs.get("id")
    #return get_object_or_404(Article, id=id_)

    #you can also override the success url by two methos
    #success_url="/" or
    #def get_success_url(self)
    #return "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)