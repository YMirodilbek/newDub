from django.db import models
# Create your models here.

class PdfBurj(models.Model):
    text = models.TextField()
    
class PdfTxt(models.Model):
    rasm = models.ImageField(upload_to='media/')


    


class Home(models.Model):
    nomi1 = models.CharField(max_length=100)
    nomi2 = models.CharField(max_length=100)
    text = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.nomi1
    
class Services(models.Model):
    nom1 = models.CharField(max_length=100)
    nom2 = models.CharField(max_length=150) 
    text = models.TextField()
    button = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom1
#verbose_name = ""
class Card(models.Model):
    emad = models.CharField(max_length=200 )
    estate = models.CharField(max_length=200)
    text = models.TextField()
    cap = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.emad

class Legal(models.Model):
    nomi = models.CharField(max_length=200)
    nom1 = models.CharField(max_length=100)
    nom2= models.CharField(max_length=100)
    nom3 = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi
    

class Boshqsmi(models.Model):
    rasm = models.ImageField(upload_to='media/')


class SMS(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Projecti_Home(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title
    

class Project_Kard(models.Model):
    rnomi1 = models.CharField(max_length=300)
    rnomi2 = models.CharField(max_length=400)
    rasm = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=500)
    nomi2 = models.CharField(max_length=600)
    url = models.CharField(max_length=300)
    
    def __str__(self):
        return self.rnomi1
    
class Header(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)

    def __str__(self):
        return self.title1


class Header_Project(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)

    def __str__(self):
        return self.title1

class Project_Matn(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Project_Matn1(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Header_News(models.Model):
    title1 = models.CharField(max_length=300)
    title2 = models.CharField(max_length=300)
    title3 = models.CharField(max_length=300)
    title4 = models.CharField(max_length=300)

    def __str__(self):
        return self.title1

class Words_News(models.Model):
    title1 = models.CharField(max_length=300)
    text1 = models.TextField()
    title2 = models.CharField(max_length=300)
    text2 = models.TextField()
    title3 = models.CharField(max_length=300)
    text3 = models.TextField()

class News_Butondi_Tepasdagi_matn(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)


class Portfolio(models.Model):
    rasm = models.ImageField(upload_to='media/')

class PdfHome(models.Model):
    nomi1 = models.CharField(max_length=200)
    nomi2 = models.CharField(max_length=299)
    nomi3 = models.CharField(max_length=299)
    baytxt = models.CharField(max_length=300)
    baground_Rasm = models.ImageField(upload_to='media/')
    rasm1 = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.nomi1
    
class PdfHome2(models.Model):
    ism_famlya = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to='media/')
    manzil = models.CharField(max_length=300)
    ikonka1 = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=399)
    tell_raqami = models.IntegerField()
    nomi3 = models.CharField(max_length=400)
    email_nomi = models.CharField(max_length=400)
    nomi4 = models.CharField(max_length=500)
    website_nomi = models.CharField(max_length=500)
    nomi5 = models.CharField(max_length=400)
    instagarm_nomi = models.CharField(max_length=500)
    ikonka_nomi2 = models.CharField(max_length=600)
    ikonka_nomi3 = models.CharField(max_length=600)
    
    def __str__(self):
        return self.ism_famlya
    
    

    

class PdfImg(models.Model):
    img = models.ImageField(upload_to="media/")
    img2 = models.ImageField(upload_to="media/")
    img3 = models.ImageField(upload_to="media/")
    img4 = models.ImageField(upload_to="media/")
    img5 = models.ImageField(upload_to="media/")
    img6 = models.ImageField(upload_to="media/")
    img7 = models.ImageField(upload_to="media/")
    img8 = models.ImageField(upload_to="media/")
    img9 = models.ImageField(upload_to="media/")
    img10 = models.ImageField(upload_to="media/")
    
class PdfCard(models.Model):
    nomi = models.CharField(max_length=300)
    text = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.nomi
    
class PdfCard7(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
class PdfCard8(models.Model):
    nomi1 = models.CharField(max_length=300)
    nomi2 = models.CharField(max_length=300)
    rasm = models.ImageField(upload_to="media/")
    text1 = models.TextField()
    text2 = models.TextField()
    
    def __str__(self):
        return self.nomi1
    
class PdfPast(models.Model):
    rasm1 = models.ImageField(upload_to="media/")    
    rasm2 = models.ImageField(upload_to="media/")



    



class DetailImage(models.Model):
    img = models.ImageField(upload_to = "media/")
    
    


class Person(models.Model): 
    name = models.CharField(max_length=120) 
    staff = models.CharField(max_length=90) 
    phone = models.CharField(max_length=20) 
    email = models.EmailField() 
    company = models.CharField(max_length=90) 
    img = models.ImageField(upload_to='media/')
    verified = models.ImageField(upload_to="media/")
 
 
    def __str__(self): 
        return self.name 
 
 
class Rooms(models.Model): 
    img = models.ImageField(upload_to='media/') 
    types = models.CharField(max_length=200) 
    bedroom = models.CharField(max_length=40) 
    price = models.CharField(max_length=90) 
    kv = models.CharField(max_length=90) 
    
 
    def __str__(self): 
        return self.types
    
class Room_luxury(models.Model): 
    img = models.ImageField(upload_to='media/') 
    types = models.CharField(max_length=200) 
    bedroom = models.CharField(max_length=40) 
    price = models.CharField(max_length=90) 
    kv = models.CharField(max_length=90) 
    
 
    def __str__(self): 
        return self.types
 
class Service(models.Model): 
    img = models.ImageField(upload_to='media/') 
    title = models.CharField(max_length=90) 
    text = models.CharField(max_length=200) 
    
    def __str__(self): 
        return self.title



class Text(models.Model):
    title = models.CharField(max_length=90) 
    text = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
    


class Department(models.Model):
    title = models.CharField(max_length=90)
    text = models.TextField()
    img = models.ImageField(upload_to='media/')
    mainimg = models.ImageField(upload_to='media/')
    icon = models.ImageField(upload_to='media/')
    room = models.ManyToManyField(Rooms)
    room_luxury = models.ManyToManyField(Room_luxury)
    service = models.ManyToManyField(Service)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    images = models.ManyToManyField(DetailImage)
    textmain = models.TextField()
    texttitle =models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
    

