# Chord Sequence Chooser

```
                           +-------+---------------+
                           |       |               |
                           |       |               |
                           v       v               |
           I ---->iii ---> vi ---> IV ---> ii ---> V ----> I
                                   |               ^
                                   |               |
                                   |               |
                                   +---------------+
```

Pedagogical aid for Kate Pukinskis and Harvard's __ES-25__ course, designed to illustrate means of generating harmonic sequences from a set network structure.

## Setup

### Dependencies
[music21](https://pypi.org/project/music21/)

### _Optional_ Dependencies (to suppress warnings from music21)
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
                        v       v               |
        I ---->iii ---> vi ---> IV ---> ii ---> V ----> I
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
>>> 
```

## TODO
* Add modal mixture
* Add "_V_-of" type substitutions
* Add chord other substitutions!
