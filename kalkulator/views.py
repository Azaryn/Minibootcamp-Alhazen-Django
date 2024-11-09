from django.shortcuts import render, HttpResponse

# Create your views here.

def tambah(request, num1, num2):
    context = dict(
        title = 'Kalkulator Tambah',
        num1 = num1,
        num2 = num2,
        result = f"{num1} + {num2} = {num1+num2}",
    )
    return render(request, 'kalkulator/index.html', context)

def kurang(request, num1, num2):
    context = dict(
        title = 'Kalkulator Kurang',
        num1 = num1,
        num2 = num2,
        result = f"{num1} - {num2} = {num1-num2}",
    )
    return render(request, 'kalkulator/index.html', context)

def kali(request, num1, num2):
    context = dict(
        title = 'Kalkulator Kali',
        num1 = num1,
        num2 = num2,
        result = f"{num1} x {num2} = {num1*num2}",
    )
    return render(request, 'kalkulator/index.html', context)

def bagi(request, num1, num2):
    context = dict(
        title = 'Kalkulator Bagi',
        num1 = num1,
        num2 = num2,
        result = f"{num1} : {num2} = {num1/num2}",
    )
    return render(request, 'kalkulator/index.html', context)

def pangkat(request, num1, num2):
    context = dict(
        title = 'Kalkulator Eksponen',
        num1 = num1,
        num2 = num2,
        result = f"{num1} ^ {num2} = {num1 ** num2}",
    )
    return render(request, 'kalkulator/index.html', context)