from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Track, Comment
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
def SequencerView(request):
    if request.method == 'GET':
        return render(request, 'piano_roll.html', context={"range": range(8,-1, -1), "notes": ["B", "A#", "A", "G#", "G", "F#", "F", "E", "D#", "D", "C#", "C" ]})
    if request.method == 'POST':
        print(request.body)
        return HttpResponse(status=200, content='{"status":"success"}', content_type='application/json')
def SequencesListView(request, id):
    if request.method == 'GET':
        track = Track.objects.get(id=id)
        return render(request, 'sequences.html')
    if request.method == 'POST':
        pass
def ProfileView(request, id):
    if request.method == 'GET':
        request.user
        track_list = Track.objects.filter(author = User.objects.get(id=id)).order_by('-created_at')
        paginator = Paginator(track_list, 10)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'profile.html', {'id': id, 'page_obj': page_obj})
    if request.method == 'POST':
        pass
def LoginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        pass
def RegisterView(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        pass
def SequencerWithIDView(request, id):
    if request.method == 'GET':
        return render(request, 'info.html', {'id': id})
    if request.method == 'POST':
        pass    

def PaginationView(request):
    if request.method == 'GET':
        track_list = Track.objects.all().order_by('-created_at')
        paginator = Paginator(track_list, 3)  # Show 10 tracks per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'sequences.html', {'page_obj': page_obj})
    if request.method == 'POST':
        pass
def EditTrackView(request, id):
    if request.method == 'GET':
        track = Track.objects.get(id=id)
        return render(request, 'edit_track.html', {'track': track})
    if request.method == 'POST':
        track = Track.objects.get(id=id)
        track.title = request.POST.get('title', track.title)
        track.description = request.POST.get('description', track.description)
        track.save()
        return redirect('profile', id=track.author.id)
def InfoView(request, id):
    if request.method == 'GET':
        track = Track.objects.get(id=id)
        comments = Comment.objects.filter(track=track).order_by('-created_at')
        return render(request, 'info.html', {'track': track, 'comments': comments})
    if request.method == 'POST':
        track = Track.objects.get(id=id)
        content = request.POST.get('content')
        Comment.objects.create(track=track, author=request.user, content=content)
        return redirect('track_info', id=id)