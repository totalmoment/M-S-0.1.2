import MS_APP.views as views
from django.urls import path

urlpatterns = [
    path('', views.SequencerView, name='sequencer'),
    path('sequences/<int:id>/', views.SequencesListView, name='sequences'),
    path('profile/<int:id>/', views.ProfileView, name='profile'),
    path('sequence/<int:id>/', views.SequencerView, name='sequencer_with_id'),
    path('edit_track/<int:id>/', views.EditTrackView, name='edit_track'),
    path('info/<int:id>/', views.InfoView, name='track_info'),
    path('pagination/', views.PaginationView, name='pagination'),
]
