from django.urls import path
from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemDeleteView,
    ItemListView,
    ItemUpdateView,
)

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='delete'),
]