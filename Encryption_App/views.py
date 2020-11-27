from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fibogen ( lenofpassword ) :
    n = int ( lenofpassword )
    first = int ( 1 )
    next = int ( 1 )
    list = [ ]
    list.append ( first )
    list.append ( next )

    current = first + next
    for i in range ( lenofpassword ) :
        list.append ( current )
        first = next
        next = current
        current = first + next

    return list


def split_string ( string ) :
    li = [ ]
    l = len ( string )
    dif = l // 3
    li.append ( string [ :dif ] )
    li.append ( string [ dif :2 * dif ] )
    li.append ( string [ 2 * dif : ] )
    print ( li )
    return li


def fiboEncryption ( data , password ) :
    reversedtext = data [ : :-1 ]

    lenofpassword = len ( password )

    ciphertext = reversedtext + password

    rs = fibogen ( lenofpassword )

    for i in rs :
        new = ""
        for ch in range ( len ( ciphertext ) ) :

            if ch % 2 != 0 :
                x = chr ( ord ( ciphertext [ ch ] ) + i )

                new += x
            else :
                x = ord ( ciphertext [ ch ] ) - i
                if x < 0 :
                    x = abs ( 110000 + x )
                x = chr ( x )

                new += x

        ciphertext = new

    return ciphertext


def index(request):
    context={'Encrypteddata':data}
    return render(request,"index.html",context)

def encryptionalgo(request):
    # return render(request,"index.html")
    return HttpResponse("This is encryption function test")



def decryptionalgo(request):
    # return render(request,"index.html")
    return HttpResponse("This is decryption function test")