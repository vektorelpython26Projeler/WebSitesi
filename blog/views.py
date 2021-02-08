from django.shortcuts import render,get_object_or_404,redirect
from .models import GonderiModel
from .forms import GonderiForm

def gonderilistele(request): # => Function Based View
    gonderiler = GonderiModel.objects.all() # verilerin alınması
    return render(request,"blog/listele.html",{"gonderis":gonderiler})
    #             istek,templateadres,modeldengelenbilgi



def gonderidetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/detay.html",{"gonderi":gonderi})


# def yenigonderi(request):
#     form = GonderiForm()
#     return render(request,"blog/yenigonderi.html",{"form":form})
from django.utils import timezone
def yenigonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        gonderi = form.save(commit=False)
        gonderi.yayimzaman = timezone.now()
        gonderi.save()
        return redirect("gonderidetay",pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,"blog/yenigonderi.html",{"form":form})

def gonderiduzenle(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        gonderi = form.save(commit=False)
        gonderi.yayimzaman = timezone.now()
        gonderi.save()
        return redirect("gonderidetay",pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,"blog/yenigonderi.html",{"form":form})



