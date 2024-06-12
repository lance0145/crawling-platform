from django.urls import path
from .views import CreativeWorkListCreate, CreativeWorkDetail

urlpatterns = [
    path('works/', CreativeWorkListCreate.as_view(), name='creative-work-list-create'),
    path('works/<int:pk>/', CreativeWorkDetail.as_view(), name='creative-work-detail'),
]
