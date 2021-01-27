from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

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


def XorCipher ( data ,pas) :
    key="K"
    for i in range ( len ( data ) ) :
        data = data [ :i ] + chr ( ord ( data [ i ] ) ^ ord ( key ) ) + data [ i + 1 : ]

    return data

def pnSequence ( data ) :
    data=data.encode()
    state=[0,0,0,1,0,1,0,1,0,1,1]
    poly = [ 2 , 2 , 3 , 4 , 2 ]
    from pylfsr import LFSR
    l = LFSR ( fpoly=poly , initstate=state )
    ciphertext=b""
    allseq = l.runFullCycle ( )
    seq = ""
    index = 0
    for x in allseq :
        seq += str ( x )
    for i in range ( len ( data ) ) :
        newseq = seq [ index :index + 8 ]

        ciphertext += bytes ( [ int ( data [ i ] ) ^ int ( newseq , 2 ) ] )
        index += 8


    return ciphertext


def Decrypt_Fibonacci(data,password):
    lenofpassword=len(password)

    rs=fibogen(lenofpassword)

    for i in rs:
        new = ""
        for ch in range(len(data)):
            if ch % 2 != 0:
                x = chr(ord(data[ch]) - i)
                new += x
            else:
                x=ord(data[ch])+i
                if x>110000:
                    x=abs(x-110000)
                x=chr(x)
                new += x

        data = new
    data=data[:len(data)-lenofpassword]


    return data[::-1]


def Decrypt_PN_Sequence(data):
    from pylfsr import LFSR
    state = [ 0 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 ]
    poly = [ 2 , 2 , 3 , 4 , 2 ]
    l = LFSR ( fpoly=poly , initstate=state )



    allseq = l.runFullCycle ( )
    seq =""
    # print("i am in function",type(data))
    import ast

    eval_expr = ast.literal_eval (data)
    ciphertext=eval_expr

    plaintext = b""
    seq_index = 0

    for x in allseq :
        seq += str ( x )



    for counter in range ( len ( ciphertext ) ) :
        ran_seq = seq [ seq_index : seq_index + 8 ]
        plaintext += bytes ( [ int ( ciphertext [ counter ] ) ^ int ( ran_seq , 2 ) ] )
        seq_index += 8
    # print ( plaintext.decode ( ) )

    return plaintext.decode()




def index(request):

    return render(request,"index.html")

def encryptionalgo(request):
    data=request.POST.get('plaintext')
    password=request.POST.get('password')[:5]

    splitted_data = split_string ( data )


    fi=fiboEncryption( splitted_data [ 0 ] , password )
    xo=XorCipher( splitted_data [ 1 ] ,password[-1] )
    pn=pnSequence(splitted_data[2])
    key=len(splitted_data[0])
    # message=fi+xo+pn

    context={'fi':fi,
             'xo':xo,
             'pn':pn,
             'key':key,
    }
    return render(request,"index.html",context)



def decryptionalgo(request):
    data=request.POST.get('ctext')
    password=request.POST.get('password')[:5]
    seg=request.POST.get('key')
    seg=int(seg)

    dfib=Decrypt_Fibonacci(data[:seg+len(password)],password)
    dxor=XorCipher(data[seg+len(password):seg+len(password)+seg],password[-1])
    dpn=Decrypt_PN_Sequence(data[seg+len(password)+seg:])
    # message=dfib+dxor+dpn
    context={'dfib':dfib,
             'dxor':dxor,
             'dpn':dpn}


    return render(request,"index.html",context)
    # return HttpResponse("This is decryption function test")