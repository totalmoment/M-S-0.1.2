import MS_APP.views as views
from django.urls import path

urlpatterns = [
    path('', views.SequencerView, name='sequencer'),
    path('sequences/', views.SequencesListView, name='sequences'),
    path('profile/<int:id>/', views.ProfileView, name='profile'),
    path('sequence/<int:id>/', views.SequencerView, name='sequencer_with_id'),
    path('pagination/', views.PaginationView, name='pagination'),
]
