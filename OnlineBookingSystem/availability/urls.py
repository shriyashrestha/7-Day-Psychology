from django.urls import path

#putting everything related to a app to the same place is the best practice in django
#it makes the code cleaner, manageable, and makes it able to be released as a third party 
#resource if and when possible
from .views import(
    UpdateAvailabilityView,
    DeleteAvailabilityView,
)


app_name='availability'
urlpatterns=[
    path('<int:pk>/update-availability/', UpdateAvailabilityView.as_view(), name='update-availability'),
    path('<int:pk>/delete-availability/', DeleteAvailabilityView.as_view(), name='delete-availability'),
    ]