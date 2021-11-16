from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Counsellor

from .form import CounsellorForm

from django.http import HttpResponse

from availability.models import Shifts, Availability
from availability.forms import AvailabilityForm
from appointments.models import Appointment

from django.views.generic import(
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )


# Create your views here.
def counsellor_form_view(request):
    form = CounsellorForm(request.POST or None)
    errors = "";
    if form.is_valid():
        form.save()
        errors = form.errors
        form = CounsellorForm()
        return redirect('counsellor:counsellor-login')

    context = {
        'form': form,
    }
    context['some_string'] = errors

    return render(request, "counsellor/counsellor_form.html", {'form': form,'error':errors})

def counsellor_details_view(request):
    obj = Counsellor.objects.all()
    context = {
        'counsellor_list': obj,
    }
    return render(request, "counsellor/details.html", context)

def counsellor_details_with_availability_view(request):
    obj = Counsellor.objects.all()
    context = {
        'counsellor_list': obj,
    }
    return render(request, "counsellor/counsellor-details.html", context)

def counsellor_login_view(request):
    counsellorName=None
    name="User"
    counsellorID=None
    loadPage=None
    if request.method=='GET':
        if 'action' in request.GET:
            action=request.GET.get('action')
            if action=='logout':
                if request.session.has_key('counsellorName'):
                    request.session.flush()
                return redirect('counsellor:counsellor-login')

        if 'counsellorName' in request.session:
            counsellorName=request.session['counsellorName']
            counsellorID=request.session['counsellorID']
            name        = Counsellor.objects.get(id=counsellorID).name
            print(request.session.get_expiry_age())

    elif request.method=='POST':
        username = request.POST.get("username"," ")
        password = request.POST.get("password"," ")
        obj = Counsellor.objects.filter(username=username,password=password)
        context = {'error':" ", "code" : 202}
        print(obj)
        if 'action' in request.POST:
            action=request.POST.get('action')
            print(action)
        if not obj:
            username=None
            context['error'] = "Username or password is incorrect. Please try again!";
            context['code'] = 422
            return render(request, "counsellor/counsellor-login.html", context)
        else:
            context['code '] = 202
            name=obj[0].name
            counsellorID=obj[0].id
            counsellorName=username
            request.session['counsellorName']=counsellorName
            request.session['counsellorID']=counsellorID

    return render(request, "counsellor/counsellor-login.html", {'username': counsellorName,
                                                                    'name': name, 
                                                                    'action': loadPage, 
                                                                })
#We do not need this view as we are rendering this page from 
#login view using if else condition in our template
"""def counsellor_main_view(request):
    username = request.POST.get("username"," ")
    password = request.POST.get("password"," ")
    obj = Counsellor.objects.filter(username=username,password=password)
    context = {'error':" ", "code" : 202}
    print(obj)
    if not obj:
        context['error'] = "Username or password is incorrect. Please try again!";
        context['code'] = 422
        return render(request, "counsellor/counsellor-login.html", context)
    else:
        context['code '] = 202
        context['name']=obj[0].name
        return render(request, "counsellor/counsellor-main.html", context) """

def all_counsellor_list_view(request):
    obj = Counsellor.objects.all()
    context={
        'all_counsellors':obj,
    }
    return render(request, 'counsellor/all-counsellor-list.html',context)

def edit_counsellor_view(request, id):
    counsellor = Counsellor.objects.get(id=id)
    return render(request, "counsellor/edit-counsellor.html", {'counsellor':counsellor})

def update_counsellor_view(request,id):
    print(id)
    counsellor=Counsellor.objects.get(id=id)
    form= CounsellorForm(request.POST or None, instance=counsellor)
    errors = "";
    if form.is_valid():
        form.save()
    return redirect("counsellor:all-counsellor-list")

def delete_counsellor_view(request,id):
    counsellor = Counsellor.objects.get(id=id)
    counsellor.delete()
    return redirect("counsellor:all-counsellor-list")

def my_availability_view(request):
    if 'counsellorName' in request.session:
        user_id=request.session['counsellorID']
        print(user_id)

        # get availability dates
        availabilityList=Availability.objects.filter(counsellor_id=user_id)

        # get availability shifts
        shifts= Shifts.objects.all()


        if request.method == 'POST':
            date = request.POST.get("availableDate"," ")

            #get the counsellor object
            counsellor=Counsellor.objects.get(id=user_id)

            #create availability object
            availability=Availability(availableDate=date, counsellor=counsellor)

            #save availability
            availability.save()

            # get new availability list
            availabilityList=Availability.objects.filter(counsellor_id=user_id)

        context={
            'availabilityList': availabilityList,
            'shifts'          : shifts,
        }

        return render(request,"counsellor/my-availability.html",context)
    else:
        return redirect('counsellor:counsellor-login')


def give_availability_view(request):
    if 'counsellorName' in request.session:
        context = {'error':" ", "code" : 202}
        return render(request, 'counsellor/give-availability.html', context)

    else:
        return redirect('counsellor:counsellor-login')


def show_availability_view(request, id):
    if request.method=='POST':
        print('POST detected at show availability')
        bookingDate=request.POST.get('bookingDate')
        print("This is bookingDate"+bookingDate)

    availabilityList=Availability.objects.filter(counsellor_id=id)
    counsellorName = Counsellor.objects.get(id=id).name
    shifts=Shifts.objects.all()

    context={
        'availabilityList': availabilityList,
        'shifts'          : shifts,
        'counsellor_id'   : id,
        'counsellorName': counsellorName,
    }
    return render(request, "counsellor/show-availability.html",context)

def my_appointments_view(request):
    if 'counsellorName' in request.session:
        counsellor_id=request.session['counsellorID']
        appointments=Appointment.objects.filter(counsellor_id=counsellor_id)
        context = {
            'appointments': appointments
        }
        return render(request,'counsellor/my-appointments.html', context)

    else:
        return redirect('counsellor:counsellor-login')

def my_clients_view(request):
    if 'counsellorName' in request.session:
        counsellor_id=request.session['counsellorID']
        appointments=Appointment.objects.filter(counsellor_id=counsellor_id)
        clients=[]
        for appoinment in appointments:
            if appoinment.client.name not in clients:
                clients.append(appoinment.client.name)

        context = {
            'clients': clients
        }
        return render(request,'counsellor/my-clients.html', context)

    else:
        return redirect('counsellor:counsellor-login')


class DeleteAppointmentView(DeleteView):
    template_name='counsellor/delete-appointment.html'
    
    queryset=Appointment.objects.all()

    def get_success_url(self):
        return reverse("counsellor:my-appointments")

def my_notifications_view(request):
    if 'counsellorName' in request.session:
        counsellor_id=request.session['counsellorID']
        appointments=Appointment.objects.filter(counsellor_id=counsellor_id)
        context = {
            'appointments': appointments
        }
        return render(request,'counsellor/my-notifications.html', context)

    else:
        return redirect('counsellor:counsellor-login')

def my_profile_view(request):
    if 'counsellorName' in request.session:
        counsellor_id=request.session['counsellorID']
        counsellor=Counsellor.objects.get(id=counsellor_id)
        context = {
            'counsellor': counsellor
        }
        return render(request,'counsellor/my-profile.html', context)

    else:
        return redirect('counsellor:counsellor-login')
