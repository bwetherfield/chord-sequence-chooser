#!/usr/bin/env python3

import os

from music21 import *

us = environment.UserSettings()
set_sound_player = True
set_score_editor = True

while True:
    user_input = input("Set sound player (e.g. QuickTime)? (y/n) ")
    if user_input.strip() == 'y':
        set_sound_player = True
        break
    elif user_input.strip() == 'n':
        set_sound_player = False
        break

while set_sound_player:
    try:
        file_path = input("Set sound player (e.g. QuickTime). Filepath: ")
        if not os.path.exists(file_path):
            raise(ValueError('Invalid file path'))
        else:
            us['midiPath'] = file_path
            set_sound_player = False
    except ValueError:
        print("Invalid file path. Try again.")

while True:
    user_input = input("Set score editor (e.g. MuseScore)? (y/n) ")
    if user_input.strip() == 'y':
        set_score_editor = True
        break
    elif user_input.strip() == 'n':
        set_score_editor = False
        break

while set_score_editor:
    try:
        file_path = input("Set score editor (e.g. MuseScore). Filepath: ")
        if not os.path.exists(file_path):
            raise(ValueError('Invalid file path')))
        else:
            us['musicxmlPath'] = file_path
            set_score_editor = False
    except ValueError:
        print("Invalid file path. Try again.")
