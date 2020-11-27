from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={'Encrypteddata':data}
    return render(request,"index.html",context)

def encryptionalgo(request):
    # return render(request,"index.html")
    return HttpResponse("This is encryption function test")



def decryptionalgo(request):
    # return render(request,"index.html")
    return HttpResponse("This is decryption function test")