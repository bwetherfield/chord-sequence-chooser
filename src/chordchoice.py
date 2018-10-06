#!/usr/bin/env python3

class Chord:

    def __init__(self, scale_degree, string_representation):
        self.scale_degree = scale_degree
        self.string_representation = string_representation

    def __str__(self):
        return string_representation


if __name__ == "__main__":

    print("Choose your own harmonic adventure...")
