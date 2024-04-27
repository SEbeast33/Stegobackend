from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.PostView.as_view(), name= 'posts_list'),
    # path('video/', views.VideoView.as_view(), name= 'posts_list'),
    path('decode/', views.PostDecodeView.as_view(), name= 'posts_list'),
     path('decodewithlink/', views.DecryptWithLinkView.as_view(), name= 'posts_list'),
]