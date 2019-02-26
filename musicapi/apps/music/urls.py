from django.urls import path
from .views import ListSongsView,CreateSongsView,DeleteSongsView


urlpatterns = [
    path('songs/create', CreateSongsView.as_view(), name="create"),
    path('songs/<pk>/delete', DeleteSongsView.as_view(), name="songs-all"),
    path('songs', ListSongsView.as_view(), name="songs-all"),
]