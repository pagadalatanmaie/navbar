from django.shortcuts import render

# Create your views here.
def fun(request):
    return render(request,'main.html ')
def navbar_01(request):
    return render(request,'courses.html')
def navbar_02(request):
    return render(request,'profile.html')
def navbar_03(request):
    return render(request,'logout.html')

def list1(request):
    list_01=['tanmaie','21']
    list_02=['vaishu',21]
    return render(request,'list_01.html',context={'a':list_01,'b':list_02})