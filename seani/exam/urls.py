from django.urls import path

from . import views

app_name='exam'
urlpatterns = [
    path('create/',views.create,name='create'),
    path('module/<int:m_id>/question/',views.question,name='question'),
    path('module/<int:m_id>/question/<int:q_id>/',views.question,name='question'),
    path('',views.home,name='home'),
]