from django.urls import path
from . import views

app_name = "spider"

urlpatterns = [
    path('baidu-search/', views.BaiduSearchSpiderView.as_view(), name="baidu_spider"),
    path('google-search/', views.GoogleSearchSpiderView.as_view(), name="google_spider"),
    path('td-search/', views.TideFingerSearchSpiderView.as_view(), name="td_spider"),
    path('chinaz-search/', views.ChinaZPingSpiderView.as_view(), name="chinaz-search"),
]
