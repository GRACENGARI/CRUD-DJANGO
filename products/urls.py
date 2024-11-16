from django.urls import path
from .import views
app_name = 'products'
urlpatterns =[
    path('',views.home,name="home" ),
    path('insert/',views.insert,name='insert'),
    path('insert_data/',views.insert_data,name='insert_data'),
    path('view/',views.view_products,name='view'),


]