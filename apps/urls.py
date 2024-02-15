from django.urls import path

from apps.views import person, delete_person

urlpatterns = [
    path('', person, name='person'),
    path('delete-person/<int:pk>', delete_person, name='delete_person'),
]
