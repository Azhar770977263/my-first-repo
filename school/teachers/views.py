from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def showteacher(request):
    return render(request,'showteacher.html')



def deleteteacher(request):
    return render(request,'deleteteacher.html')

def editteacher(request):
    teachers={
        "total":567,
        "marks":[90,99,65,59],
        "eachsub":{"datamining":77,
        "desing":55,
        "asas":99}}
    return render(request,'editteacher.html',teachers)

        
