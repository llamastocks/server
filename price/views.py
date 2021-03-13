from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from price.models import BVL,calculator

def index(request):
    return render(request,'index.html')

def simulator(request):
    return render(request,'simulator.html')

def donations(request):
    return render(request,'donations.html')

def addticker(request):
    form=calculator()
    result=""
    minCAV=5
    fg=.000075
    smv=.000135
    IBGC=["ALICORC1","ALICORI1","BBVAC1","CPACASC1","CPAC",
    "BUENAVC1","BVN","ENGIEC1","FERREYC1","INRETC1","IFS","RIMSEGC1"
    ]
    


    if request.method=="POST":
        form=calculator(request.POST)
        if form.is_valid():
            stock=form.cleaned_data['stock']
            capital=form.cleaned_data['capital']
            p=form.cleaned_data['p']
            sab=form.cleaned_data['sab']
            minSAB=form.cleaned_data['minSAB']
            

            if stock in IBGC:
                cavali=.00004095
            else:
                cavali=.0004095

            if stock in IBGC:
                bvl=.000021
            else:
                bvl=.00021

            caso1=(capital*p*sab)/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab+1.18*cavali))
            caso2=(capital*p*cavali)/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab+1.18*cavali))

            if (caso1>minSAB and caso2>minCAV):
                acciones=capital/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab+1.18*cavali))
                acciones=round(acciones-0.5)
                print(acciones)

            caso3=(sab*p*(capital-1.18*(minSAB)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*cavali))
            caso4=(cavali*p*(capital-1.18*(minSAB)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*cavali))

            if (caso3<minSAB and caso4>minCAV):
                acciones=(capital-1.18*minSAB)/(p*(1+1.18*bvl+1.18*fg+smv+1.18*cavali))
                acciones=round(acciones-0.5)
                print(acciones)

            caso5=(sab*p*(capital-1.18*(minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab))
            caso6=(cavali*p*(capital-1.18*(minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab))

            if (caso5>minSAB and caso6<minCAV):
                acciones=(capital-1.18*(minCAV))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab))
                acciones=round(acciones-0.5)
                print(acciones)

            caso7=(sab*p*(capital-1.18*(minSAB+minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv))
            caso8=(cavali*p*(capital-1.18*(minSAB+minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv))

            if (caso7<minSAB and caso8<minCAV):
                acciones=(capital-1.18*(minSAB+minCAV))/(p*(1+1.18*bvl+1.18*fg+smv))
                acciones=round(acciones-0.5)
                print(acciones)

            result="Vas a comprar "+str(acciones)+" acciones de "+stock
            form=calculator()
            
            
    
    return render(request,'simulator.html',{'form':form,"result":result})
