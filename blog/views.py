from django.shortcuts import render,get_object_or_404
from .models import GonderiModel

def gonderilistele(request): # => Function Based View
    gonderiler = GonderiModel.objects.all() # verilerin alınması
    return render(request,"blog/listele.html",{"gonderis":gonderiler})
    #             istek,templateadres,modeldengelenbilgi



def gonderidetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/detay.html",{"gonderi":gonderi})