from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoriesList, ProductViewSet, CommentCreate, CommentViewSet


router = DefaultRouter()
router.register('', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoriesList.as_view()),
    path('comments/create/', CommentCreate.as_view()),
    path('comments/<int:pk>/', CommentViewSet.as_view({
        "get": "retrieve",
        "patch": "partial_update",
        "put": "update",
        "delete": "destroy"
    })),
    # path('rating/select/', include(router.urls)),
]

