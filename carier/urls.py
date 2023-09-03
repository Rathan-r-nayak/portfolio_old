from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",views.default,name="default"),
    path("home/",views.home),
    path("about/",views.about,name="bio"),
    path("contact/",views.contact),
    path("form/",views.form,name="form"),
    path("form/action",views.formdata),
    path("deletefeed/<int:id>",views.deletedata),
]
