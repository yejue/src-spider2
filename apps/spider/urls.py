from django.urls import path
from . import views

app_name = "spider"

urlpatterns = [
    path('baidu-search/', views.BaiduSearchSpiderView.as_view(), name="baidu_spider"),
    path('google-search/', views.GoogleSearchSpiderView.as_view(), name="google_spider"),
]
