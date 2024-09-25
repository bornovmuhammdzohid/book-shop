from django.shortcuts import render
from .models import (
    Car,
    Maxsulot,
    Category,
    Books,
    Janr
)

def asosiy_sahifa(request):   
    cars =  Car.objects.all()
    return render(request, "index.html", {"cars": cars})

def shop(request):
    categories = Category.objects.all()
    category = request.GET.get("category")
    lte = request.GET.get("lte")
    gte = request.GET.get("gte")
    search = request.GET.get("search")
    order = request.GET.get("order")
    if category:
        maxsulotlar = Maxsulot.objects.all().filter(category__nom=category)
    elif lte and gte:
        maxsulotlar = Maxsulot.objects.all().filter(narx__gte=gte, narx__lte=lte)
    elif lte:
        maxsulotlar = Maxsulot.objects.all().filter(narx__lte=lte)
    elif gte:
        maxsulotlar = Maxsulot.objects.all().filter(narx__gte=gte)
    elif search:
        maxsulotlar = Maxsulot.objects.all().filter(nom__icontains=search)
    elif order == "ascending":
        maxsulotlar = Maxsulot.objects.all().order_by("narx")
    elif order == 'descending':
        maxsulotlar = Maxsulot.objects.all().order_by("-narx")
    else:
        maxsulotlar = Maxsulot.objects.all() # bu bizga table ichidagi barcha malumotni oladi va `maxsulotlar` o'zgaruvchisiga tenglab beradi
    return render(request, "shop.html", {"maxsulotlar": maxsulotlar, "categories": categories, "category": category})


def booksPage(request):
    books = Books.objects.all()
    search = request.GET.get('search')
    ovner = request.GET.get('ovner')
    narx = request.GET.get('narx')
    janr = request.GET.get('janr')
    

    if search:
        kitoblar = Books.objects.all().filter(nom__icontains=search)
    elif ovner:
        kitoblar = Books.objects.all().filter(ovner__icontains=ovner)
    elif janr:
        kitoblar = Books.objects.all().filter(janr__janrlar__icontains=janr)
    elif narx:
        kitoblar = Books.objects.all().filter(narx=narx)
    else:
        kitoblar = books




    return render(request, 'books.html', {'kitoblar': kitoblar,'books': books   })