"""Midi music parser"""
import mido

class MidiData:
    def __init__(self, filename, title='Unnamed'):
        self.midi = mido.MidiFile(filename)
        self.title = title

        self.port = mido.open_output()

    def play_music(self):
        for msg in self.midi.play():
            self.port.send(msg)
