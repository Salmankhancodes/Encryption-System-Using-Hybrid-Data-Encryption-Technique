from django.contrib import admin
from django.urls import path,include
from Encryption_App import views

urlpatterns = [
    path("",views.index, name="index"),
    path("encryption",views.encryptionalgo, name="encryption"),
    path("decryption",views.decryptionalgo, name="decryption"),
]
