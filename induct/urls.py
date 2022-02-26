from django.urls import path
from .views import home,list_view
from . import views
urlpatterns=[
    path('display/', views.showdata, name="induct-list"),
    # path('display/',views.showdatas,name="induct-list2"),
    path('',home,name='home'),
]