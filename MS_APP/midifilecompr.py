from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo
import json

NOTE_MAP = {
    'C': 0, 'C#': 1, 'D': 2, 'D#': 3,
    'E': 4, 'F': 5, 'F#': 6, 'G': 7,
    'G#': 8, 'A': 9, 'A#': 10, 'B': 11
}

def note_to_midi(note: str) -> int:
    name = note[:-1]
    octave = int(note[-1])
    return 12 * (octave + 1) + NOTE_MAP[name]

class MidiWorker:
    def __init__(self, midi_file: str):
        self.midi_file = midi_file
        self.mid = MidiFile(ticks_per_beat=480)
        self.track = MidiTrack()
        self.mid.tracks.append(self.track)

    def sec_to_ticks(self, sec: float, bpm: int) -> int:
        return int(sec * self.mid.ticks_per_beat * bpm / 60)

    def build_track(self, notes: list, bpm: int = 120):
        self.track.clear()
        events = []

        self.track.append(Message('program_change', program=0, time=0))

        self.track.append(
            MetaMessage('set_tempo', tempo=bpm2tempo(bpm), time=0)
        )

        for n in notes:
            pitch = note_to_midi(n['note'])
            start = self.sec_to_ticks(n['start'], bpm)
            end = self.sec_to_ticks(n['start'] + n['duration'], bpm)

            events.append((start, Message('note_on', note=pitch, velocity=64)))
            events.append((end, Message('note_off', note=pitch, velocity=64)))

        events.sort(key=lambda x: x[0])

        last_time = 0
        for abs_time, msg in events:
            msg.time = abs_time - last_time
            self.track.append(msg)
            last_time = abs_time

        self.track.append(MetaMessage('end_of_track', time=0))

    def save(self):
        self.mid.save(self.midi_file)

from django.http import JsonResponse

def SaveTrackView(request):
    data = json.loads(request.body)

    midi_worker = MidiWorker('nazvanie.mid')
    midi_worker.build_track(
        data['notes'],
        bpm=data.get('bpm', 120)
    )
    midi_worker.save()

    return JsonResponse({'status': 'ok'})
