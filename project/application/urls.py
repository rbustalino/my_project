
from django.urls import path
from . import views
from application.views import contactpg

app_name = 'application'

urlpatterns = [
    path('functionv',views.contactpage, name = 'contactpage'),
    path('classv/<int:id>',contactpg.as_view(), name = 'contactpg')

]
