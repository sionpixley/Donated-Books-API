from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import Api.views as views


urlpatterns = [
    path("CreateBook/", views.CreateBook),
    path("DeleteBookById/<int:id>/", views.DeleteBookById),
    path("GetBook/<str:title>/<str:authorFirstName>/<str:authorLastName>/", views.GetBook),
    path("GetBookById/<int:id>/", views.GetBookById),
    path("GetAllBooks/", views.GetAllBooks),
    path("EditBookById/<int:id>/<str:property>/<str:newData>/", views.EditBookById),
    path("GetSumOfAllBookPrices/", views.GetSumOfAllBookPrices),
    path("CreateFile/", views.CreateFile)
]

urlpatterns = format_suffix_patterns(urlpatterns)
