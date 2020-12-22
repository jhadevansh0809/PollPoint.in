from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.PollListView.as_view(),name='home'),
    path('poll/create/',views.PollCreateView.as_view(),name='create_poll'),
    path('poll/<poll_id>/vote',views.Vote,name='vote'),
    path('poll/<int:pk>/result',views.PollResultDetailView.as_view(),name='result'),
]