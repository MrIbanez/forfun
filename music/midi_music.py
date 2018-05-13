"""Midi music parser"""
import mido

class MidiData:
    def __init__(self, filename, title):
        self.midi = mido.MidiFile(filename)
        pass

    def parse_file(self, filename):
        self.file_data
        pass

    def play_music(self):
        for msg in self.midi.play():
            port.send(msg)
