from django.urls import path

from board.views import index


app_name = "board"

urlpatterns = [
    path("", index, name="index")
]
