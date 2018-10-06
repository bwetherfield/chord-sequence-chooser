#!/usr/bin/env python3

class Chord:

    def __init__(self, scale_degree, string_representation):
        self.scale_degree = scale_degree
        self.string_representation = string_representation
        self.next_chords = []

    def add_follow_option(self, chord):
        next_chords.append(chord)

    def __str__(self):
        return string_representation

if __name__ == "__main__":

    chord_I = Chord(1, "I")
    chord_iii = Chord(3, "iii")
    chord_I.add_follow_option(chord_iii)

    print("Choose your own harmonic adventure...")
