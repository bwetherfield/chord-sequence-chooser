#!/usr/bin/env python3

from music21 import *

mode = key.Key('C', 'ionian')
pitches = mode.pitches
chords = []
numerals = []
for index, degree in enumerate(pitches):
    chord = chord.Chord[
        degree,
        pitches[(index + 2) % 7],
        pitches[(index + 4) % 7
               ]
    chords.append(chord)
    numerals.append(roman.romanNumeralFromChord(chord, mode))

class ChordNode:

    def __init__(self, scale_degree, string_representation, music21_chord):
        self.scale_degree = scale_degree
        self.string_representation = string_representation
        self.next_chords = []
        self.internal_chord = music21_chord

    def add_follow_option(self, chord):
        self.next_chords.append(chord)

    def add_follow_options(self, chords):
        self.next_chords = self.next_chords + chords

    def __str__(self):
        return self.string_representation

chord_I = ChordNode(1, "I", chord.Chord(['C', 'E', 'G']))
first_chord = chord_I
sequence = [first_chord]
chord_iii = ChordNode(3, "iii", chord.Chord(['E', 'G', 'B']))
chord_vi = ChordNode(6, "vi", chord.Chord(['A', 'C', 'E']))
chord_IV = ChordNode(4, "IV", chord.Chord(['F', 'A', 'C']))
chord_ii = ChordNode(2, "ii", chord.Chord(['D', 'F', 'A']))
chord_V = ChordNode(5, "V", chord.Chord(['G', 'B', 'D']))
chord_viio = ChordNode(7, "viio", chord.Chord(['B', 'D', 'F']))
chord_I_2 = ChordNode(1, "I", chord.Chord(['C', 'E', 'G']))
final_chord = chord_I_2
internal_chords = [
    chord_iii,
    chord_vi,
    chord_IV,
    chord_ii,
    chord_V,
    chord_viio,
]
cadential_progressions = {
    chord_V: [chord_vi, chord_IV]
}
chord_I.add_follow_option(chord_I)
chord_I.add_follow_options(internal_chords)
final_chord.add_follow_option(final_chord)
for index, chord in enumerate(internal_chords):
    chord.add_follow_option(chord)
    chord.add_follow_options(internal_chords[index + 1:])
    chord.add_follow_option(final_chord)
for key in cadential_progressions:
    key.add_follow_options(cadential_progressions[key])
network_diagram = """
                        +-------+---------------+
                        |       |               |
                        |       |               |
                        v       v               |          o
        I      iii      vi      IV      ii      V       vii     I
        |       ^       ^       ^       ^       ^        ^      ^
        |       |       |       |       |       |        |      |
        v       v       v       v       v       v        v      |
         ------> ------> ------> ------> ------> -------> ----->
        """

class GlobalFunction:

    def __init__(self, function, string):
        self.function = function
        self.string = string

    def execute(self):
        self.function()

    def __str__(self):
        return self.string

def undo():
    if len(sequence) > 1:
        sequence.pop()

def show_sequence():
    print("Sequence: ", ", ".join(str(x) for x in sequence))

def play_sequence():
    sequence_stream = stream.Stream()
    for i,num in consolidate_duplicates():
        i.internal_chord.duration.quarterLength = num
        sequence_stream.append(i.internal_chord)
    sequence_stream.show('midi')

def show_notation():
    score = stream.Score()
    score.insert(0, metadata.Metadata())
    score.metadata.title = 'My Harmonic Adventure'
    score.metadata.composer = ''
    sequence_stream = stream.Part()
    for i,num in consolidate_duplicates():
        i.internal_chord.duration.quarterLength = num
        sequence_stream.append(i.internal_chord)
    score.append(sequence_stream)
    score.show()

def consolidate_duplicates():
    temp = sequence[0]
    temp_index = 0
    consolidated = []
    for i,c in enumerate(sequence):
        if c != temp:
            consolidated.append((temp, i - temp_index))
            temp = c
            temp_index = i
    consolidated.append((temp, len(sequence) - temp_index))
    return consolidated

def show_global_commands():
    print("Global commands:",
          "\n".join(((i != 0) * " " * (len("Global commands:") + 1))
                                         + "({}) {}".format(str(i), str(x))
                                      for i,x in enumerate(global_functions)))

def show_chord_network():
    print(network_diagram)

wrapped_undo = GlobalFunction(undo, "Undo")
wrapped_show_sequence = GlobalFunction(show_sequence, "Show sequence")
wrapped_play_sequence = GlobalFunction(play_sequence, "Play sequence")
wrapped_show_notation = GlobalFunction(show_notation, "Show notation")
wrapped_show_global_commands = GlobalFunction(show_global_commands,
                                              "Show Global Commands")
wrapped_show_chord_network = GlobalFunction(show_chord_network,
                                            "Show Chord Network Diagram")

global_functions = [
    wrapped_show_chord_network,
    wrapped_show_global_commands,
    wrapped_undo,
    # wrapped_show_sequence,
    wrapped_play_sequence,
    wrapped_show_notation
]

def main_sequence():
    print("Choose your own harmonic adventure...")
    show_chord_network()
    show_global_commands()

    while True:
        current = sequence[-1]
        show_sequence()
        print("Next option(s): ",
              " ".join("({}) {}"
                       .format(str(i+len(global_functions)), str(x))
                       for i,x in enumerate(current.next_chords)))
        while True:
            try:
                user_input = int(input(">>> "))
                if user_input < 0:
                    raise(IndexError('Negative Index'))
                elif user_input < len(global_functions):
                    global_functions[user_input].execute()
                else:
                    sequence.append(
                        (global_functions + current.next_chords)[user_input]
                    )
                break
            except IndexError:
                print("Invalid index. Try again.")
            except ValueError:
                print("Must input an integer. Try again.")

if __name__ == "__main__":
    main_sequence()
