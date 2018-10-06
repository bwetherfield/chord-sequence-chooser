#!/usr/bin/env python3

class ChordNode:

    def __init__(self, scale_degree, string_representation):
        self.scale_degree = scale_degree
        self.string_representation = string_representation
        self.next_chords = []

    def add_follow_option(self, chord):
        self.next_chords.append(chord)

    def __str__(self):
        return self.string_representation

if __name__ == "__main__":

    chord_I = ChordNode(1, "I")
    chord_iii = ChordNode(3, "iii")
    chord_I.add_follow_option(chord_iii)

    print("Choose your own harmonic adventure...")
    print(chord_I)
