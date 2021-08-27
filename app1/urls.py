from django.urls import path
from .import views


urlpatterns = [
    path('test',views.testfun,name="test"),
    path('html',views.fn2,name="html")

]
