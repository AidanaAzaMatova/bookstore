from django.urls import path, include
from book_drf import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', views.ModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('get_books/', views.ListInfo.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('create_book/', views.ModelViewSet.as_view({'post': 'create'})),
    path('update_book/<int:pk>/', views.ModelViewSet.as_view({'post': 'update'}))
]
