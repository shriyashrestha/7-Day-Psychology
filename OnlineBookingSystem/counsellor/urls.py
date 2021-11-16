from django.urls import path

from .views import(
	counsellor_details_view,
	counsellor_details_with_availability_view,
	counsellor_form_view,
	counsellor_login_view,
    all_counsellor_list_view,
    edit_counsellor_view,
    update_counsellor_view,
    delete_counsellor_view,
    my_availability_view,
    give_availability_view,
    show_availability_view,
    my_clients_view,
    my_appointments_view,
    my_notifications_view,
    my_profile_view,
    DeleteAppointmentView,
)

app_name="counsellor"

urlpatterns=[
	path('', counsellor_details_view, name='counsellor-details'),
	path('counsellor-details/', counsellor_details_with_availability_view, name='counsellor-details-with-availability'),
    path('form/', counsellor_form_view, name='counsellor-form'),
    path('login/', counsellor_login_view, name='counsellor-login'),
    path('list/',all_counsellor_list_view, name='all-counsellor-list'),
    path('edit/<int:id>',edit_counsellor_view, name='edit-counsellor'),
    path('update/<int:id>',update_counsellor_view, name='update-counsellor'),
    path('delete/<int:id>',delete_counsellor_view, name='delete-counsellor'),
    path('give-availability/',give_availability_view, name='give-availability'),
    path('my-availabiltiy/',my_availability_view, name='my-availability'),
    path('show-availability/<int:id>',show_availability_view, name='show-availabiltiy'),
    path('my-clients/',my_clients_view, name='my-clients'),
    path('my-appointments/',my_appointments_view, name='my-appointments'),
    path('my-notifications/',my_notifications_view, name='my-notifications'),
    path('my-profile/',my_profile_view, name='my-profile'),
    path('<int:pk>/delete-appointments/',DeleteAppointmentView.as_view(), name='delete-appointments'),
]