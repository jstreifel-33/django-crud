from django.urls import path

from snacks.views import SnackCreateView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView

urlpatterns = [
    path('', SnackListView.as_view(), name='snacks_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete')
]