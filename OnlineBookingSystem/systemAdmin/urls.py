from django.urls import path

#putting everything related to a app to the same place is the best practice in django
#it makes the code cleaner, manageable, and makes it able to be released as a third party 
#resource if and when possible
from .views import(
	admin_login_view,
    admin_change_password_view,
    admin_update_password_view,
    CreateWorkHoursView,
    UpdateWorkHoursView,
    WorkHoursListView,
    WorkHoursUpdateView,
    WorkHoursDeleteView,
    my_notifications_view,
    all_appointments_view,
    DeleteAppointmentsView,
    CreateCounsellorView,
    CreateClientView,
)


app_name='systemAdmin'
urlpatterns=[
	path('logIn/',admin_login_view,name='admin-logIn'),
    path('change-password/', admin_change_password_view, name='admin-change-password'),
    path('update-password/', admin_update_password_view, name='admin-update-password'),
    path('create-workhours/', CreateWorkHoursView.as_view(), name='create-workhours'),
    path('<int:pk>/update-workhours/', UpdateWorkHoursView.as_view(), name='update-workhours'),
    path('list-workhours/', WorkHoursListView.as_view(), name='list-workhours'),
    path('<int:pk>/update-workhours/', WorkHoursUpdateView.as_view(), name='update-workhours'),
    path('<int:pk>/delete-workhours/', WorkHoursDeleteView.as_view(), name='delete-workhours'),
    path('my-notifications/', my_notifications_view, name='my-notifications'),
    path('all-appointments/', all_appointments_view, name='all-appointments'),
    path('create-counsellor/', CreateCounsellorView.as_view(), name='create-counsellor'),
    path('create-client/', CreateClientView.as_view(), name='create-client'),
    path('<int:pk>/delete-appointments/', DeleteAppointmentsView.as_view(), name='delete-appointments'),
   
]