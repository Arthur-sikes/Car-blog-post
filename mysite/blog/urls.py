from django.urls import path,include
from django.contrib import admin
from . import views

app_name = 'blog'
urlpatterns = [ path('',views.post_list,name='post_list') , 
path('<single_slug>',views.single_slug,name='single_slug'),
#path('admin/',admin.site.urls)
]