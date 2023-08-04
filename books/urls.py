from django.urls import path
from .views import BookListApi

urlpatterns=[
    path("",BookListApi.as_view())
]