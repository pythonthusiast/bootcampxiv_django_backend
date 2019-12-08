from django.conf.urls import url
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from upwork.views import JobViewSet

schema_view = get_swagger_view(title='Upwork API')


router = routers.DefaultRouter()
router.register('job', JobViewSet)
urlpatterns = [
    url('docs/', schema_view)
]
urlpatterns += router.urls