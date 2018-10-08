# Chord Sequence Chooser
```
                           +-------+---------------+---------------+
                           |       |               |               |
                           |       |               |               |
                           v       v               |          o    v
           I ---->iii ---> vi ---> IV ---> ii ---> V ----> vii --->I
                                   |               ^
                                   |               |
                                   |               |
                                   +---------------+
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

                        +-------+---------------+---------------+
                        |       |               |               |
                        |       |               |               |
                        v       v               |          o    v
        I ---->iii ---> vi ---> IV ---> ii ---> V ----> vii --->I
                                |               ^
                                |               |
                                |               |
                                +---------------+
        
Global commands: (0) Show Chord Network Diagram
                 (1) Show Global Commands
                 (2) Undo
                 (3) Show sequence
                 (4) Play sequence
                 (5) Show notation
Current chord:  I
Next option(s):  (6) iii
>>> 6
Current chord:  iii
Next option(s):  (6) vi
>>> 6
Current chord:  vi
Next option(s):  (6) IV
>>> 6
Current chord:  IV
Next option(s):  (6) ii (7) V
>>> 7
Current chord:  V
Next option(s):  (6) IV (7) I (8) viio
>>> 7
Current chord:  I
You have reached the final chord:  I
>>> 
```

## TODO
* Add modal mixture
* Add "_V_-of" type substitutions
* Add chord other substitutions!
