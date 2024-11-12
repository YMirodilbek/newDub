from modeltranslation.translator import register,TranslationOptions,translator
from .models import *

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields=("nomi1","nomi2","text")
    
@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields=("nom1","nom2","text","button")
    
@register(Card)
class CardTranslationOptions(TranslationOptions):
    fields=("emad","estate","text","cap")
    
@register(Legal)
class LegalTranslationOptions(TranslationOptions):
    fields=("nomi","nom1","nom2","nom3","text1","text2","text3")

@register(Header)
class HeaderTranslationOptions(TranslationOptions):
    fields=("title1","title2","title3","title4")

@register(Header_Project)
class Header_ProjectTranslationOptions(TranslationOptions):
    fields=("title1","title2","title3","title4")


@register(Project_Kard)
class Project_KardTranslationOptions(TranslationOptions):
    fields=('rnomi1','rnomi2','nomi1','nomi2')

@register(Project_Matn)
class Project_MatnTranslationOptions(TranslationOptions):
    fields=('title','text')

@register(Project_Matn1)
class Project_Matn1TranslationOptions(TranslationOptions):
    fields=('title','text')
