from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostView, ContentView, BannerView, IstoryView, CategoryView, GenreView, TagView, CommentView

router = DefaultRouter()
router.register("post", PostView, basename="post")
router.register("content", ContentView, basename="content")
router.register("banner", BannerView, basename="banner")
router.register("istory", IstoryView, basename="istory")
router.register("category", CategoryView, basename="category")
router.register("genre", GenreView, basename="genre")
router.register("tag", TagView, basename="tag")
router.register("comment", CommentView, basename="comment")


urlpatterns = [
    path("", include(router.urls)),
]
