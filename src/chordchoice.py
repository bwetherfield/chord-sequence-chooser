#!/usr/bin/env python3

from contextlib import contextmanager
import sys, os

from music21 import *

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

sequence = []
chord_I = ChordNode(1, "I", chord.Chord(['C', 'E', 'G']))
cursor = chord_I
chord_iii = ChordNode(3, "iii", chord.Chord(['E', 'G', 'B']))
chord_I.add_follow_option(chord_iii)
chord_iii.add_follow_option(chord_I)
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

def undo():
    if length(sequence) <= 1:
        cursor = chord_1
    else:
        cursor = sequence.pop()

def show_sequence():
    print("Sequence: ", ", ".join(str(x) for x in sequence))

def play_sequence():
    sequence_stream = stream.Stream()
    for i in sequence:
        sequence_stream.append(i.internal_chord)
    sequence_stream.show('midi')

if __name__ == "__main__":

    print("Choose your own harmonic adventure...")
    print(network_diagram)
    print("Global commands", "(0) Play sequence", "(1) View sequence",
              "(2) Undo")

    first_pass = True
    while first_pass or cursor != chord_I:
        sequence.append(cursor)
        print("Current chord: ", cursor)
        print("Next option(s): ", " ".join("({}) {}".format(str(i+3), str(x)) for i,x
                                         in enumerate(cursor.next_chords)))
        while True:
            try:
                user_input = int(input("Choice: "))
                if user_input == 0:
                    play_sequence()
                elif user_input == 1:
                    show_sequence()
                elif user_input == 2:
                    undo()
                    if len(sequence) <= 1:
                        first_pass = True
                else:
                    next_chord = user_input - 3
                    if next_chord < 0:
                        raise(IndexError('Negative Index'))
                    cursor = cursor.next_chords[next_chord]
                    first_pass = False
                break
            except IndexError:
                print("Invalid index. Try again.")
            except ValueError:
                print("Must input an integer. Try again.")


