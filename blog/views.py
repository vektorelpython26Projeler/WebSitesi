from django.shortcuts import render
from .models import GonderiModel

def gonderilistele(request): # => Function Based View
    gonderiler = GonderiModel.objects.all() # verilerin alınması
    return render(request,"blog/listele.html",{"gonderis":gonderiler})
    #             istek,templateadres,modeldengelenbilgi

