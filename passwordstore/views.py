from django.shortcuts import render,redirect
from .forms import PasswordstoreForm
from .models import Passwordstore
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = PasswordstoreForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PasswordstoreForm()
    app_and_passwords = Passwordstore.objects.all().order_by('-id')
    context={
        'app_and_passwords':app_and_passwords,
        'form' : form
        }
    return render(request,'passwordstore/home.html',context)


def ajax_newcreate(request):
    data ={}
    form = PasswordstoreForm(request.POST)
    if form.is_valid():
        form.save()
    app_and_passwords = Passwordstore.objects.all()
    data['posts']=render_to_string('passwordstore/fly.html',{'app_and_passwords':app_and_passwords},request)
    return JsonResponse(data)

def ajax_delete_newcustomer(request):
    data={}
    id = request.GET.get('pk')
    post = Passwordstore.objects.get(id=id)
    post.delete()
    app_and_passwords = Passwordstore.objects.all()
    data['posts'] = render_to_string('passwordstore/fly.html',{'app_and_passwords':app_and_passwords},request)
    return JsonResponse(data)


def ajax_edit_customer(request):
    data={}
    id = request.GET.get('pk')
    customer = Passwordstore.objects.get(id=id)
    customer.save()
    app_and_passwords = Passwordstore.objects.all()
    data['posts'] = render_to_string('passwordstore/fly.html',{'app_and_passwords':app_and_passwords},request)
    return JsonResponse(data)

def editpassword(request,pk):
    app_password = Passwordstore.objects.get(id=pk)
    if request.method == 'POST':
        post_form = PasswordstoreForm(request.POST,instance = app_password)
        if post_form.is_valid():
            post_form.save()
            return redirect('passwordstore:index')
    else:
        post_form = PasswordstoreForm(instance=app_password)
    context = {
        'post_form':post_form
        }
    return render(request,'passwordstore/updatepass.html',context)


def add_pass(request):
    if request.method=='POST':
        appname = request.POST['appname']
        app_password = request.POST['app_password']
        print(appname)
        print(app_password)
        newpass = Passwordstore.objects.create(app_name=appname,password_field=app_password)
        newpass.save()
        return redirect('passwordstore:index')