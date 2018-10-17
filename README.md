# Chord Sequence Chooser
```
                        +-------+---------------+
                        |       |               |
                        |       |               |
                        v       v               |          o
        I      iii      vi      IV      ii      V       vii     I
        |       ^       ^       ^       ^       ^        ^      ^
        |       |       |       |       |       |        |      |
        v       v       v       v       v       v        v      |
         ------> ------> ------> ------> ------> -------> ----->
```

Pedagogical aid for Kate Pukinskis and Harvard's ES-25 course, designed to illustrate means of generating harmonic sequences from a fixed network structure.

## Setup

### Dependencies
[music21](https://pypi.org/project/music21/)

### _Optional_ Dependencies
* QuickTime (or other midi player for `Play sequence` functionality)
* MuseScore (or other musicxml reader for `Show notation` functionality)
  - Setting music21 [environment](http://web.mit.edu/music21/doc/moduleReference/moduleEnvironment.html) settings may be needed to enable these features (to allow music21 to find the appropriate external software)
#### (to suppress warnings from music21)
* numpy
* scipy
* matplotlib

## Usage
Run `chordchoice.py` from the command line, with Python3 and the above dependencies installed.

Below is an extract from the command line output for a brief (partial) execution of the program:

```
Choose your own harmonic adventure...

                        +-------+---------------+
                        |       |               |
                        |       |               |
                        v       v               |          o
        I      iii      vi      IV      ii      V       vii     I
        |       ^       ^       ^       ^       ^        ^      ^
        |       |       |       |       |       |        |      |
        v       v       v       v       v       v        v      |
         ------> ------> ------> ------> ------> -------> ----->
        
Global commands: (0) Show Chord Network Diagram
                 (1) Show Global Commands
                 (2) Undo
                 (3) Play sequence
                 (4) Show notation
Sequence:  I
Next option(s):  (5) I (6) iii (7) vi (8) IV (9) ii (10) V (11) viio
>>> 5
Sequence:  I, I
Next option(s):  (5) I (6) iii (7) vi (8) IV (9) ii (10) V (11) viio
>>> 6
Sequence:  I, I, iii
Next option(s):  (5) iii (6) vi (7) IV (8) ii (9) V (10) viio (11) I
>>> 7
Sequence:  I, I, iii, IV
Next option(s):  (5) IV (6) ii (7) V (8) viio (9) I
>>> 8
Sequence:  I, I, iii, IV, viio
Next option(s):  (5) viio (6) I
>>> 6
Sequence:  I, I, iii, IV, viio, I
Next option(s):  (5) I
>>> 4
Sequence:  I, I, iii, IV, viio, I
Next option(s):  (5) I
```
