from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('computer-list', ComputerListView.as_view(), name='computer-list'),
    path('detail/<int:pk>', ComputerDetailView.as_view(), name='computer-detail'),
    path('delete/<int:pk>', ComputertDeleteView.as_view(), name='computer-delete'),
    path('create', ComputerCreateView.as_view(), name='create-computer'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add-review'),
    path('edit_review/<int:pk>', ReviewUpdateView.as_view(), name='edit-review'),
    path('category/', CategoryListView.as_view(), name='category'),
]


