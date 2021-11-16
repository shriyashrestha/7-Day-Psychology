from django.shortcuts import render, redirect

from .models import Client
from counsellor.models import Counsellor
from appointments.models import Appointment
from django.contrib import messages
from django.urls import reverse

from appointments.models import Appointment
from availability.models import Availability, Shifts

from .form import ClientForm
from django.core.mail import send_mail

from django.views.generic import(
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )


# Create your views here.
def client_initial_view(request):
    return render(request, "client/index.html")


def client_login_view(request):
    clientName=None
    name="User"
    clientID=None
    loadPage=None
    if request.method=='GET':
        if 'action' in request.GET:
            action=request.GET.get('action')
            if action=='logout':
                if request.session.has_key('clientName'):
                    request.session.flush()
                return redirect('client:client-login')

        if 'clientName' in request.session:
            username=request.session['clientName']
            clientName=username
            clientID= request.session['clientID']
            name=Client.objects.get(id=clientID).name
            print(request.session.get_expiry_age())

    elif request.method=='POST':
        username = request.POST.get("username"," ")
        password = request.POST.get("password"," ")
        obj = Client.objects.filter(username=username,password=password)
        context = {'error':" ", "code" : 202}
        print(obj)
        if 'clientName' in request.POST:
            action=request.POST.get('action')
            print(action)
        if not obj:
            username=None
            context['error'] = "Username or password is incorrect. Please try again!";
            context['code'] = 422
            return render(request, "client/client-login.html", context)
        else:
            context['code '] = 202
            name=obj[0].name
            clientID=obj[0].id
            clientName=username
            request.session['clientName']=clientName
            request.session['clientID']=clientID

    return render(request, "client/client-login.html", {'username': clientName,
                                                                    'name': name, 
                                                                    'action': loadPage, 
                                                                })


def client_form_view(request):
    form = ClientForm(request.POST or None)
    errors = "";
    if form.is_valid():
        form.save()
        errors = form.errors
        form = ClientForm()
        return redirect('client:client-login')

    context = {
        'form': form,
    }
    context['some_string'] = errors

    return render(request, "client/client-form.html", {'form': form, 'error': errors})

def all_client_list_view(request):
    obj = Client.objects.all()
    context={
        'all_clients':obj,
    }
    return render(request, 'client/all-client-list.html',context)

def edit_client_view(request, id):
    client = Client.objects.get(id=id)
    return render(request, "client/edit-client.html", {'client':client})

def update_client_view(request,id):
    print(id)
    client = Client.objects.get(id=id)
    form= ClientForm(request.POST or None, instance=client)
    errors = "";
    if form.is_valid():
        form.save()
    return redirect("client:all-client-list")

def delete_client_view(request,id):
     client = Client.objects.get(id=id)
     client.delete()
     return redirect("client:all-client-list")

def create_appointment_view(request):
    if 'clientName' in request.session:
        if request.method=='GET':
            if 'counsellorID' in request.GET:
                counsellor_id=request.GET.get('counsellorID')
            if 'workhoursFrom' in request.GET:
                workhoursFrom=request.GET.get('workhoursFrom')
            if 'workhoursTo' in request.GET:
                workhoursTo=request.GET.get('workhoursTo')
                bookingTime=workhoursFrom+" To "+workhoursTo
                print(bookingTime)

            if 'bookingDate' in request.GET:
                bookingDate=request.GET.get('bookingDate')
                print(bookingDate)
        client_id=request.session['clientID']
        counsellor=Counsellor.objects.get(id=counsellor_id)
        client=Client.objects.get(id=client_id)
        appointment=Appointment(appointmentDate=bookingDate, appointmentTime=bookingTime, 
            counsellor=counsellor, client=client)
        appointment.save()

        #sending confirmation email
        send_mail(
            '7Day Psychology Center',
            'Hi '+client.name+", you have an appointment with "+counsellor.name+" scheduled on "+
            bookingDate+" at "+bookingTime,
            'bdipendra01@gmail.com',
            ['bhandaridipendra94@gmail.com'],
            fail_silently=False,
        )

        messages.info(request, "Your appointment with "+counsellor.name+" has been booked successfully.")
        context = {
            'message': "Appointment booked!"
        }
        return redirect('client:my-appointment')

    else:
        return redirect('client:client-login')


def my_appointments_view(request):
    if 'clientName' in request.session:
        client_id=request.session['clientID']
        appointments=Appointment.objects.filter(client_id=client_id)
        context = {
            'appointments': appointments
        }
        return render(request,'client/my-appointments.html', context)

    else:
        return redirect('client:client-login')

def my_counsellors_view(request):
    if 'clientName' in request.session:
        client_id=request.session['clientID']
        appointments=Appointment.objects.filter(client_id=client_id)
        counsellors=[]
        for appoinment in appointments:
            if appoinment.counsellor.name not in counsellors:
                counsellors.append(appoinment.counsellor.name)

        context = {
            'counsellors': counsellors
        }
        return render(request,'client/my-counsellors.html', context)

    else:
        return redirect('client:client-login')


class DeleteAppointmentView(DeleteView):
    template_name='client/delete-appointment.html'
    
    queryset=Appointment.objects.all()

    def get_success_url(self):
        return reverse("client:my-appointment")

def my_notifications_view(request):
    if 'clientName' in request.session:
        client_id=request.session['clientID']
        appointments=Appointment.objects.filter(client_id=client_id)
        context = {
            'appointments': appointments
        }
        return render(request,'client/my-notifications.html', context)

    else:
        return redirect('client:client-login')

def my_profile_view(request):
    if 'clientName' in request.session:
        client_id=request.session['clientID']
        client=Client.objects.get(id=client_id)
        context = {
            'client': client
        }
        return render(request,'client/my-profile.html', context)

    else:
        return redirect('client:client-login')

def  reschedule_appointment_view(request, pk):
    if 'clientName' in request.session:
        client_id=request.session['clientID']
        appointment_id=pk
        appointment=Appointment.objects.get(id=appointment_id)
        counsellor_id=appointment.counsellor.id
        availability=Availability.objects.filter(counsellor_id=counsellor_id)
        shifts=Shifts.objects.all()
        context = {
            'appointment': appointment,
            'availability': availability,
            'shifts': shifts,
        }

        if request.method=='POST':
            bookingDate=request.POST.get('booking_date')
            bookingTime=request.POST.get('booking_time')
            print(bookingDate+"and"+bookingTime)
            appointment.appointmentDate=bookingDate
            appointment.appointmentTime=bookingTime
            appointment.save()
            return redirect('client:my-appointment')



        return render(request,'client/reschedule-appointment.html', context)

    else:
        return redirect('client:client-login')