from django.urls import include, path

from rest_framework import routers

from uuid_generator.views import RandomGeneratorViewSet

router = routers.DefaultRouter()
router.register("uuids", RandomGeneratorViewSet, basename="uuids")
uuid_generator_patterns = router.urls
