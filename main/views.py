from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.views.generic.detail import DetailView

def Index(request):
    context={
        'home':Home.objects.first(),
        'servic':Services.objects.first(),
        'card':Card.objects.all(),
        'legal':Legal.objects.first(),
        'card1':Card.objects.all(),
        'boshqsmi':Boshqsmi.objects.first(),
        "header":Header.objects.first(),
        "portfoilo":Portfolio.objects.all(),
    }
    return render(request,"index.html",context)

def Contact(request):
    return render(request,"contact.html")

def SMS(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        SMS.objects.create(name=name,email=email,text=text)
        messages.success(request,"SMS keldi szga")
        return redirect('/')
    
def Project(request):
    a={
        'projecti_Home':Projecti_Home.objects.first(),
        'projectkard':Project_Kard.objects.all(),
        'header_Project':Header_Project.objects.first(),
        'project_Matn':Project_Matn.objects.first(),
        'project_Matn1':Project_Matn1.objects.first(),
        'department':Department.objects.all()
    }
    return render(request,"project.html",a)


def Pdf6(request):
    context = {
        'PdfHome':PdfHome.objects.first(),
        'PdfHome2':PdfHome2.objects.first(),
        'pdfimg':PdfImg.objects.first(),
        'pdfcard':PdfCard.objects.all(),
        'pdfcard7':PdfCard7.objects.all(),
        'pdfcard8':PdfCard8.objects.all(),
        'pdfpast':PdfPast.objects.first(),
    }
    return render(request,"pdf6.html",context)

class DepartmentDetail(DetailView): 
    model = Department 
    template_name = 'detail.html' 
    context_object_name = 'department' 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
 
        # You can add additional context if needed, for example: 
        context['person'] = self.object.person
        context['room'] = self.object.room.all() 
        context['room_luxury'] = self.object.room_luxury.all()  
        context['service'] = self.object.service.all() 
        context['images'] = self.object.images.all()[:2]
        context['images1'] = self.object.images.all()[2:4]
        context['img'] = self.object.images.all()[4]
        context['img2'] = self.object.images.all()[5]
        context['back'] = self.object.images.all()[3]
        
        
   

        
         
 
 
         
        return context