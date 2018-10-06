#!/usr/bin/env python3

from contextlib import contextmanager
import sys, os

from music21 import chord as chord

class ChordNode:

    def __init__(self, scale_degree, string_representation, music21_chord):
        self.scale_degree = scale_degree
        self.string_representation = string_representation
        self.next_chords = []
        self.internal_chord = music21_chord

    def add_follow_option(self, chord):
        self.next_chords.append(chord)

    def __str__(self):
        return self.string_representation

if __name__ == "__main__":

    chord_I = ChordNode(1, "I", chord.Chord(['C', 'E', 'G']))
    chord_iii = ChordNode(3, "iii", chord.Chord(['E', 'G', 'B']))
    chord_I.add_follow_option(chord_iii)

    cursor = chord_I

    print("Choose your own harmonic adventure...")
    print("\n")
    print("Current chord: ", cursor)
    print("Next options: ", " ".join(index, string for (index, string) in
                                     enumerate(cursor.next_chords)))
    print(chord_I)
