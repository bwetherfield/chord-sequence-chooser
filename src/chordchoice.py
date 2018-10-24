#!/usr/bin/env python3

from music21 import *

class State:

    def __init__(self, sequence = None, chord_nodes = None, key = None):
        self.sequence = sequence
        self.chord_nodes = chord_nodes
        self.key = key

class ChordNode:

    def __init__(self, music21_numeral, music21_chord):
        self._numeral = music21_numeral
        self._internal_chord = music21_chord
        self.next_chords = []
        self.out_routes = []

    @property
    def internal_chord(self):
        return chord.Chord(self._internal_chord)

    @property
    def numeral(self):
        return roman.RomanNumeral(self._numeral.figure)

    def add_out_route(self, chordNode):
        self.out_routes.append(chordNode)
        self.add_follow_option(chordNode)

    def add_out_routes(self, chord_nodes):
        self.out_routes = self.out_routes + chord_nodes
        self.add_follow_options(chord_nodes)

    def add_follow_option(self, chordNode):
        self.next_chords.append(chordNode)

    def add_follow_options(self, chord_nodes):
        self.next_chords = self.next_chords + chord_nodes

    def __str__(self):
        return self.numeral.figure


class GlobalFunction:

    def __init__(self, function, string):
        self.function = function
        self.string = string

    def execute(self, state):
        self.function(state)

    def __str__(self):
        return self.string

def undo(state):
    if len(state.sequence) > 1:
        state.sequence.pop()

def show_sequence(state):
    print("Sequence: ", ", ".join(str(x) for x in state.sequence))

def play_sequence(state):
    sequence_stream = stream.Stream()
    for i,num in consolidate_duplicates(state.sequence):
        i.internal_chord.duration.quarterLength = num
        sequence_stream.append(i.internal_chord)
    sequence_stream.show('midi')

def show_notation(state):
    score = stream.Score()
    score.insert(0, metadata.Metadata())
    score.metadata.title = 'My Harmonic Adventure'
    score.metadata.composer = ''
    sequence_stream = stream.Part()
    sequence_stream.append(state.key)
    for i,num in consolidate_duplicates(state.sequence):
        i.internal_chord.duration.quarterLength = num
        sequence_stream.append(i.internal_chord)
    score.append(sequence_stream)
    score.show()

def consolidate_duplicates(sequence):
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

def show_global_commands(state):
    print("Global commands:",
          "\n".join(((i != 0) * " " * (len("Global commands:") + 1))
                                         + "({}) {}".format(str(i), str(x))
                                      for i,x in enumerate(global_functions)))

def show_chord_network(state):
    print("In forming your harmonic sequence...")
    print("Any jump left to right (or repetition) is permitted:")
    print('')
    print("".join(str(i).ljust(8) for i in state.chord_nodes))
    print('')
    print("The following right to left jumps are permitted:")
    print('')
    for i in state.chord_nodes:
        if i.out_routes != []:
            print(str(i), ":", ", ".join(str(j) for j in i.out_routes))
    print('')

wrapped_undo = GlobalFunction(undo, "Undo")
wrapped_show_sequence = GlobalFunction(show_sequence, "Show sequence")
wrapped_play_sequence = GlobalFunction(play_sequence, "Play sequence")
wrapped_show_notation = GlobalFunction(show_notation, "Show notation")
wrapped_show_global_commands = GlobalFunction(show_global_commands,
                                              "Show Global Commands")
wrapped_show_chord_network = GlobalFunction(show_chord_network,
                                            "Show harmonic sequence structure")

global_functions = [
    wrapped_show_global_commands,
    wrapped_show_chord_network,
    wrapped_undo,
    wrapped_play_sequence,
    wrapped_show_notation,
]

def show_title():
    print("Choose your own harmonic adventure...")

def choose_tonic():
    tonics = [x.name for x in scale.ChromaticScale('g3').pitches]
    tonics.pop()
    print("Choose a tonic:")
    print(" ".join("({}) {}".format(i,x.replace('-','b')) for i,x in enumerate(tonics)))
    while True:
        try:
            user_input = int(input(">>> "))
            if user_input < 0:
                raise(IndexError('Negative Index'))
            else:
                tonic = tonics[user_input]
            break
        except IndexError:
            print("Invalid index. Try again.")
        except ValueError:
            print("Must input an integer. Try again.")
    print("You chose", str(tonic).replace('-','b'))
    return tonic

def choose_mode():
    modes = ['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian',
             'aeolian', 'locrian']
    print("Choose a mode:")
    print(" ".join("({}) {}".format(i,x) for i,x in enumerate(modes)))
    while True:
        try:
            user_input = int(input(">>> "))
            if user_input < 0:
                raise(IndexError('Negative Index'))
            else:
                mode_flavor = modes[user_input]
            break
        except IndexError:
            print("Invalid index. Try again.")
        except ValueError:
            print("Must input an integer. Try again.")
    print("You chose", mode_flavor)
    return mode_flavor

def set_key(tonic, mode_flavor):
    return key.Key(tonic, mode_flavor)

def show_key(chosen_mode):
    print("Your mode is", str(chosen_mode).replace('-','b'))

def get_chords_numerals(chosen_mode):
    pitches = chosen_mode.pitches
    pitches.pop()
    chord_nodes = []
    for index, degree in enumerate(pitches):
        tempChord = chord.Chord([
            degree,
            pitches[(index + 2) % 7],
            pitches[(index + 4) % 7]
        ])
        tempNumeral = roman.romanNumeralFromChord(tempChord, chosen_mode)
        chord_nodes.append(ChordNode(tempNumeral, tempChord))
    return chord_nodes

def reorder_chords(chord_nodes):
    indices = [0,2,5,3,1,4,6]
    reordered_chord_nodes = [chord_nodes[i] for i in indices]
    return reordered_chord_nodes

def populate_options(mode_flavor, chord_nodes):
    for index, chord_node in enumerate(chord_nodes):
        chord_node.add_follow_option(chord_node)
        chord_node.add_follow_options(chord_nodes[index+1:])
        if index != 0:
            chord_node.add_out_route(chord_nodes[0])
    if mode_flavor == 'ionian':
        chord_nodes[5].add_out_route(chord_nodes[2])
    elif mode_flavor == 'dorian':
        chord_nodes[5].add_out_routes([chord_nodes[1],chord_nodes[3]])
    elif mode_flavor == 'phrygian':
        chord_nodes[3].add_out_route(chord_nodes[1])
    elif mode_flavor == 'lydian':
        chord_nodes[4].add_out_route(chord_nodes[2])
        chord_nodes[5].add_out_route(chord_nodes[2])
    elif mode_flavor == 'mixolydian':
        chord_nodes[5].add_out_route(chord_nodes[2])
    elif mode_flavor == 'aeolian':
        chord_nodes[3].add_out_route(chord_nodes[2])
        chord_nodes[5].add_out_route(chord_nodes[2])
        chord_nodes[6].add_out_route(chord_nodes[2])
    elif mode_flavor == 'locrian':
        pass
    return chord_nodes



def main_sequence(key, chord_nodes):
    sequence = [chord_nodes[0]]
    # show_chord_network()
    show_global_commands(State())

    while True:
        current = sequence[-1]
        show_sequence(State(sequence = sequence))
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
                    global_functions[user_input].execute(State(
                        sequence = sequence,
                        chord_nodes = chord_nodes,
                        key = key
                    ))
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
    show_title()
    tonic = choose_tonic()
    mode_flavor = choose_mode()
    chosen_mode = set_key(tonic, mode_flavor)
    show_key(chosen_mode)
    chord_nodes = get_chords_numerals(chosen_mode)
    chord_nodes = reorder_chords(chord_nodes)
    chord_nodes = populate_options(mode_flavor, chord_nodes)
    main_sequence(chosen_mode, chord_nodes)
