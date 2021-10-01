from django.http import HttpResponse
from django.shortcuts import render


def showTeacherPage(request):
    response=HttpResponse("I am a teacher")
    return response

def showTeacherInfoPage(request):
    return render(request, 'Teacher/teacherInfo.html')
