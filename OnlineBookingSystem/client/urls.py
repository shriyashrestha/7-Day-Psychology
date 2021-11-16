from django.urls import path

#putting everything related to a app to the same place is the best practice in django
#it makes the code cleaner, manageable, and makes it able to be released as a third party 
#resource if and when possible
from .views import(
	client_login_view,
    client_form_view,
    all_client_list_view,
    edit_client_view,
    update_client_view,
    delete_client_view,
    create_appointment_view,
    my_appointments_view,
    my_notifications_view,
    my_counsellors_view,
    DeleteAppointmentView,
    my_profile_view,
    reschedule_appointment_view,
)

app_name="client"

urlpatterns=[
	path('login/', client_login_view, name='client-login'),
    path('form/', client_form_view, name='client-form'),
    path('list/',all_client_list_view, name='all-client-list'),
    path('edit/<int:id>',edit_client_view, name='edit-client'),
    path('update/<int:id>',update_client_view, name='update-client'),
    path('delete/<int:id>',delete_client_view, name='delete-client'),
    path('create-appointment/', create_appointment_view, name='create-appointment'),
    path('my-appointment/', my_appointments_view, name='my-appointment'),
    path('my-notifications/', my_notifications_view, name='my-notifications'),
    path('my-profile/', my_profile_view, name='my-profile'),
    path('my-counsellors/', my_counsellors_view, name='my-counsellors'),
    path('<int:pk>/reschedule-appointment/', reschedule_appointment_view, name='reschedule-appointment'),
    path('<int:pk>/delete-appointment/', DeleteAppointmentView.as_view(), name='delete-appointment'),
]