from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')



def editstudent(request):
    return render(request,'editstudent.html')


def deletestudent(request):
    return render(request,'deletestudent.html')

def showstudent(request):
    student={
        "name":"adel",
        "mark":[90,99,65,59],
        "eachsub":{"datamining":77,
        "desing":55,
        "asas":99}}
    return render(request,'showstudent.html',student)

def editstudent(request):
    name={"fname":"azhar"}
    return render(request,'editstudent.html',name) 



def index(request):
    name={"fname":"azhar"}
    return render(request,'index.html',name)           