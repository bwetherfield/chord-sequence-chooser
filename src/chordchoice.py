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
first_chord = chord_I
cursor = first_chord
chord_iii = ChordNode(3, "iii", chord.Chord(['E', 'G', 'B']))
chord_vi = ChordNode(6, "vi", chord.Chord(['A', 'C', 'E']))
chord_IV = ChordNode(4, "IV", chord.Chord(['F', 'A', 'C']))
chord_ii = ChordNode(2, "ii", chord.Chord(['D', 'F', 'A']))
chord_V = ChordNode(5, "V", chord.Chord(['G', 'B', 'D']))
chord_I.add_follow_option(chord_iii)
chord_iii.add_follow_option(chord_vi)
chord_vi.add_follow_option(chord_IV)
chord_IV.add_follow_option(chord_ii)
chord_IV.add_follow_option(chord_V)
chord_ii.add_follow_option(chord_V)
chord_V.add_follow_option(chord_IV)
chord_V.add_follow_option(chord_I)
final_chord = chord_I
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
class GlobalFunction:

    def __init__(self, function, string):
        self.function = function
        self.string = string

    def __str__(self):
        return self.string

def undo():
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

    while True:
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
                else:
                    next_chord = user_input - 3
                    if next_chord < 0:
                        raise(IndexError('Negative Index'))
                    cursor = cursor.next_chords[next_chord]
                break
            except IndexError:
                print("Invalid index. Try again.")
            except ValueError:
                print("Must input an integer. Try again.")

    # print("You have reached the final chord: ", final_chord)
    # user_input = int(input("Choice: "))

