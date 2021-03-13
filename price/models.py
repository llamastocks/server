from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class stock(models.Model):
    ticker=models.CharField(max_length=10, primary_key=True)
    emisor=models.CharField(max_length=100, default="")


class contactForm(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)

class BVL(models.Model):
    stock=models.CharField(max_length=10)
    capital=models.IntegerField(default=None)
    p=models.FloatField(default=None)
    sab=models.FloatField(default=None)
    minSAB=models.FloatField(default=None)
    #minCAV=5
    #fg=.000075
    #smv=.000135
    #IBGC=["ALICORC1","ALICORI1","BBVAC1","CPACASC1","CPAC",
    #"BUENAVC1","BVN","ENGIEC1","FERREYC1","INRETC1","IFS","RIMSEGC1"
    #]

    #if stock in IBGC:
    #    cavali=.00004095
    #else:
    #    cavali=.0004095

    #if stock in IBGC:
    #    bvl=.000021
    #else:
    #    bvl=.00021


class calculator(ModelForm):
    class Meta:
        model=BVL
        fields=['capital','stock','p','sab','minSAB']
        labels={
            'capital':_('Monto a Invertir (S/)'),
            'stock':_('Ticker'),
            'p':_('Precio de Compra'),
            'sab':_('Comisión SAB (%)'),
            'minSAB':_('Comisión Mínima'),
        }


class TickerForm(ModelForm):
    class Meta:
        model=stock
        fields=['ticker']



    
    