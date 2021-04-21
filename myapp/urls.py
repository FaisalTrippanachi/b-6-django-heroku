
from django.urls import path,include
from . import views

urlpatterns = [
  path('test1',views.TestFun1,name = "test1"),
  path('test2',views.TestFun2,name = "test2"),
  path('test3',views.TestFun3,name = "test3")
]
