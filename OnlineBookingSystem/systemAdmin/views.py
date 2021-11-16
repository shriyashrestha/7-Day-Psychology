from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Admin
from counsellor.form import CounsellorForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import(
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )
from availability.forms import WorkingHoursForm
from availability.models import Shifts
from counsellor.models import Counsellor
from appointments.models import Appointment
from client.models import Client
from client.form import ClientForm

# Create your views here.
def admin_login_view(request):
    adminName=None
    name="User"
    adminID=None
    loadPage=None
    if request.method=='GET':
        if 'action' in request.GET:
            action=request.GET.get('action')
            if action=='logout':
                if request.session.has_key('adminName'):
                    request.session.flush()
                return redirect('systemAdmin:admin-logIn')

        if 'adminName' in request.session:
            adminName=request.session['adminName']
            adminID=request.session['adminID']
            print(request.session.get_expiry_age())

    elif request.method=='POST':
        username = request.POST.get("username"," ")
        password = request.POST.get("password"," ")
        obj = Admin.objects.filter(username=username,password=password)
        context = {'error':" ", "code" : 202}
        print(obj)
        if 'action' in request.POST:
            action=request.POST.get('action')
            print(action)
        if not obj:
            adminName=None
            context['error'] = "Username or password is incorrect. Please try again!";
            context['code'] = 422
            return render(request, "systemAdmin/admin-login.html", context)
        else:
            context['code '] = 202
            adminID=obj[0].id
            adminName=username
            request.session['adminName']=adminName
            request.session['adminID']=adminID

    return render(request, "systemAdmin/admin-login.html", {'username': adminName,
                                                                    'name': name, 
                                                                    'action': loadPage, 
                                                                })


def admin_change_password_view(request):
   return render(request,"systemAdmin/admin-change-password.html")

def admin_update_password_view(request):
    admin = Admin.objects.get(id=request.user.id)
    password = request.POST.get("password"," ")
    admin.password = password
    admin.save()
    return render(request,"systemAdmin/admin-change-password.html")

class CreateWorkHoursView(CreateView):
    template_name='systemAdmin/create-workhours.html'
    form_class=WorkingHoursForm
    queryset=Shifts.objects.all()

class UpdateWorkHoursView(UpdateView):
    template_name='systemAdmin/create-workhours.html'
    form_class=WorkingHoursForm
    queryset=Shifts.objects.all()

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

class WorkHoursListView(ListView):
    # we can reference diffrent template names as well
    # one way is to do this if the templates were inside article foler
    # template_name='articles/article_list.html'
    template_name='systemAdmin/list-workhours.html'
    queryset=Shifts.objects.all()

class WorkHoursUpdateView(UpdateView):
    template_name='systemAdmin/workhours-create.html'
    form_class=WorkingHoursForm
    queryset=Shifts.objects.all()

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


class WorkHoursDeleteView(DeleteView):
    template_name='systemAdmin/workhours-delete.html'
    
    queryset=Shifts.objects.all()

    def get_success_url(self):
        return reverse("systemAdmin:list-workhours")

def my_notifications_view(request):
    if 'adminName' in request.session:
        counsellors=Counsellor.objects.all()
        appointments=Appointment.objects.all()
        clients=Client.objects.all()
        context = {
            'appointments': appointments,
            'counsellors' : counsellors,
            'clients'     : clients,
        }
        return render(request,'systemAdmin/my-notifications.html', context)

    else:
        return redirect('systemAdmin:counsellor-logIn')

def all_appointments_view(request):
    if 'adminName' in request.session:
        appointments=Appointment.objects.all()
        context = {
            'appointments': appointments
        }
        return render(request,'systemAdmin/all-appointments.html', context)

    else:
        return redirect('systemAdmin:admin-logIn')

class DeleteAppointmentsView(DeleteView):
    template_name='systemAdmin/delete-appointment.html'
    
    queryset=Appointment.objects.all()

    def get_success_url(self):
        return reverse("systemAdmin:all-appointments")

class CreateCounsellorView(CreateView):
    template_name='systemAdmin/create-counsellor.html'
    form_class=CounsellorForm
    queryset=Counsellor.objects.all()

class CreateClientView(CreateView):
    template_name='systemAdmin/create-client.html'
    form_class=ClientForm
    queryset=Client.objects.all()