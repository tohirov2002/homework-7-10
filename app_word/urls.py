from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import OriginListView, CategoryListView, WordListView

router = DefaultRouter()
router.register(r'origin', OriginListView)
router.register(r'category', CategoryListView)
router.register(r'word', WordListView)

urlpatterns = router.urls
