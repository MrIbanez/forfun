# import midi_music
from midi_music import MidiData

temp = MidiData('The_Animals_-_House_of_the_Rising_Sun.mid')
# temp.play_music()

for msg in temp.midi.play():
    print(msg)