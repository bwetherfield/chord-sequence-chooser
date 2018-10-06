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
    chord_iii.add_follow_option(chord_I)

    cursor = chord_I

    network_diagram = """
			                +-------+---------------+
			                |       |               |
			                |       |               |
			                v       v               |
			I ---->iii ---> vi ---> IV ---> ii ---> V ----> I
			                        |               ^
			                        |               |
			                        |               |
			                        +---------------+
			"""

    print("Choose your own harmonic adventure...")
    print(network_diagram)
    print("Current chord: ", cursor)
    print("Next options: ", " ".join([str(x) for x in cursor.next_chords]))

    first_pass = True
    while first_pass or cursor != chord_I:
        print("Current chord: ", cursor)
        print("Next options: ", " ".join([str(x) for x in cursor.next_chords]))
        with next_chord = input("Choice: "):
            cursor = cursor.next_chords[next_chord])

