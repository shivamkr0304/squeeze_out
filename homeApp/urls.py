from django.contrib import admin
from django.urls import path,re_path
from homeApp import views
from django.views.generic import TemplateView

urlpatterns = [
    path("",views.index),
    path("feedback/",views.feedback),
    #path("emoji.html",views.emoji,name="emoji"),
    #path("login.html",views.loginsystem,name="login"),
    path('login/',views.logIN),
    path('logout/',views.logOUT),
    re_path(r'^testgame/$', TemplateView.as_view(template_name="emoji.html"), name='testgame'),
    path('update_feedback/<roll>',views.update_feedback)
]