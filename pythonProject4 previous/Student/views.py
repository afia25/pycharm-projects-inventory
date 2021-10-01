
from django.http import HttpResponse
from django.shortcuts import render

def showStudentPage(request):
    response = HttpResponse("I am a student")
    return response


def showStudentInfoPage(request):
    return render(request, 'Student/studentInfo.html')
    # return HttpResponse("My name is Afia")

def showMyPage(request):
    response = HttpResponse("My page")
    return response
