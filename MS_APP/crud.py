import MS_APP.models as models

def create_track(title, artist, note_num, duration, author, dere_st=1, privaty_ch=2):
    new_track = models.Track(
        title=title,
        artist=artist,
        note_num=note_num,
        duration=duration,
        author=author,
        dere_st=dere_st,
        privaty_ch=privaty_ch
    )
    new_track.save()
    return new_track

def get_all_tracks():
    return models.Track.objects.all()

# .get(FILTER) - получить 1 запись по фильтру
# .filter(FILTER) - получить набор записей по фильтру

def get_track_by_id(track_id):
    return models.Track.objects.get(id=track_id)

def get_tracks_by_author(author):
    return models.Track.objects.filter(author=author)

def update_track(track_id, title=None, likes=None, privaty_ch=None, dere_st=None):
    track = get_track_by_id(track_id)
    
    if title is not None:
        track.title = title
        
    if likes is not None:
        track.likes = likes
        
    if privaty_ch is not None:
        track.privaty_ch = privaty_ch
        
    if dere_st is not None:
        track.dere_st = dere_st
        
    track.save()
    return track

def delete_track(track_id):
    track = get_track_by_id(track_id)
    track.delete()
    return track