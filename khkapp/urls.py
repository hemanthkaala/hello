from django.urls import path
from . import views

urlpatterns = [
    path("cal/",views.cal,name="cal"),
    path("add/",views.add,name="add"),
    path('sub/',views.sub,name="sub"),
    path('image/',views.image,name="image"),
    path('persion/',views.persion,name="persion"),
    path('khkapp/',views.index,name="index"),
]