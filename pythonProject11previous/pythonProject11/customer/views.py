

from django.shortcuts import render


#from django.contrib.auth.forms
def base(request):
    return render(request, 'customer/base.html')

def profile(request):
    return render(request,'customer/profile.html')

def register(request):
    pass
    #form=UserRegistrationForm()
    #context={
        #'form':form
    #}
    #return render(request,'customer/register.html',context)
