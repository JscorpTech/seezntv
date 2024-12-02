from django.urls import path

from core.apps.content import views

urlpatterns = [
    path("contents/", views.ContentListView.as_view()),
    path("contents/<int:pk>/", views.ContentRetrieve.as_view()),
    path("contents/genre/", views.GenresListAPIView.as_view()),
    path("contents/category/", views.CategoryListAPIView.as_view()),
    path("contents/istoy/", views.IstoryListAPIView.as_view()),
]
