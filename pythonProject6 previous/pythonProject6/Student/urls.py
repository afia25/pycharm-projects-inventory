from django.urls import path,include

#from Student import views as stuviews
from . import views
urlpatterns = [
    path('',views.showStudentPage),
    path('my/',views.showMyPage),
    path('Info/',views.showStudentInfoPage)

]