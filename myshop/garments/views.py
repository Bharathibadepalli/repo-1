from django.shortcuts import render

from garments.models import Formalshirts,CasualShirt,Pants
from garments.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def formal_shirt(request):
   lst=Formalshirts.objects.all()
   return render(request,'formal_shirt.html',{'lst':lst})

def casual_shirt(request):
    lst=CasualShirt.objects.all()
    return render(request,'casual_shirt.html',{'lst':lst})

def Pant(request):
    lst=Pants.objects.all()
    return render(request,'pant.html',{'lst':lst})

def contactus(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        subject='Hello from my garments shop'
        message='your message:'+request.POST.get('message')+"we will get back soon"
        from_email=settings.EMAIL_HOST_USER
        user_email=request.POST.get('conatct_email')
        to_list=[user_email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou') 





    return render(request,'contact.html',{'form':form})

def thankyou(request):
    response=HttpResponse()
    response.write('<h2> Thank for contactus<br> wejut sent mail</h2>')
    return response


lst=[]
price=[]
def cart(request,id):
    item=get_object_or_404(Formalshirts,pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'total_price':sum(price)})
    


