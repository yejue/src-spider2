from django.urls import path
from apps.spider.views import BtAndVulBoxDataViewSet
from libs.routers import SimpleRouter

app_name = "apiv1"

simple_router = SimpleRouter()
simple_router.register(BtAndVulBoxDataViewSet)  # 注册补天盒子视图集

urlpatterns = [
]

urlpatterns += simple_router.get_urls()
