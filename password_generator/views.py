from django.shortcuts import render,redirect
import string
import random

# Create your views here.

def password_gen(length,options):
    print(length)
    print(options)
    password = []
    password_new=""
    if '1' in options and '2' not in options and '3' not in options and '4' not in options:
        #print('only lower case')
        for i in range(length):
            password.append(random.choice(string.ascii_letters).lower())
    elif '1' in options and '2' in options and '3' not in options and '4' not in options:
        #print('lower case + uper case')
        for i in range(length):
            password.append(random.choice(string.ascii_lowercase+string.ascii_uppercase))
    elif '1' in options and '2' in options and '3' in options and '4' not in options:
        #print('lower case + uper case +number')
        for i in range(length):
            password.append(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits))
    elif '1' in options and '2' in options and '3' in options and '4'  in options:
        #print('lower case + uper case +number + special')
        for i in range(length):
            password.append(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation))
    elif '1' in options and '2' not in options and '3' in options and '4' not in options:
        #print('lower case + number')
        for i in range(length):
            password.append(random.choice(string.ascii_lowercase+string.digits))
    elif '1' in options and '2' not in options and '3' not in options and '4' in options:
        #print('lower case + special')
        for i in range(length):
            password.append(random.choice(string.ascii_lowercase+string.punctuation))
    elif '1' in options and '2' not in options and '3' in options and '4' in options:
        #print('lower case + number + special')
        for i in range(length):
            password.append(random.choice(string.ascii_lowercase+string.digits+string.punctuation))
     

    #uper case scenarios
    elif '1' not in options and '2' in options and '3' not in options and '4' not in options:
        #print('only upper case')
        for i in range(length):
            password.append(random.choice(string.ascii_letters))
    elif '1' not in options and '2' in options and '3' in options and '4' not in options:
        #print('upper case+ number')
        for i in range(length):
            password.append(random.choice(string.ascii_letters+string.digits))
    elif '1' not in options and '2' in options and '3' not in options and '4' in options:
        #print('upper case+special')
        for i in range(length):
            password.append(random.choice(string.ascii_letters+string.punctuation))
    elif '1' not in options and '2' in options and '3' not in options and '4' not in options:
        #print('upper case+number+spceial')
        for i in range(length):
            password.append(random.choice(string.ascii_letters+string.digits+string.punctuation))

    #number scenarios
    elif '1' not in options and '2' not in options and '3' in options and '4' not in options:
        #print('only numbers')
        for i in range(length):
            password.append(random.choice(string.digits))
    elif '1' not in options and '2' not in options and '3' in options and '4' in options:
        #print('numbers + special')
        for i in range(length):
            password.append(random.choice(string.digits+string.punctuation))
    
    # special charcter scenarios
    elif '1' not in options and '2' not in options and '3' not in options and '4' in options:
        #print('only special')
        for i in range(length):
            password.append(random.choice(string.punctuation)) 
    
    for i in password:
        password_new = password_new+i
    print(password_new)
    return password_new

def home(request):
    if request.method == 'POST':
        
        if request.POST.get('password_length'):
            password_len = int(request.POST['password_length'])
            options=[]
            option1=request.POST.get('lower_case',0) 
            option2=request.POST.get('upper_case',0) 
            option3=request.POST.get('number',0) 
            option4=request.POST.get('special_char',0)
            options.append(option1)
            options.append(option2)
            options.append(option3)
            options.append(option4)
            password = password_gen(password_len,options)
            if password == "":
                context={
                'message':'Please select at least one check box'     
                }
                return render(request,'password_generator/index.html',context) 
                   
            else:
                return render(request,'password_generator/index.html',{'password':password})
        else:
            context={
                'message':'Please select password length'     
                }
        return render(request,'password_generator/index.html',context) 

    context ={
        }
    return render(request,'password_generator/index.html',context) 

def add_pass(request):
    if request.method=='POST':
        appname = request.POST['appname']
        app_password = request.POST['app_password']
        print(appname)
        print(app_password)
        return redirect('password_generator:index')
