from django.urls import path,include


from . import views
urlpatterns = [
    path('',views.showTeacherPage),

    path('Info/',views.showTeacherInfoPage)

]