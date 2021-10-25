#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:38:38 2021

@author: Sam
"""

"""
This is a recreation of a similar puzzle simulator that I made in MatLab back in
college. This is a simulator for my FlipDot Puzzle. I unknowingly designed a puzzle
that was analagous to the VeryPuzzle Snow Mystery, so this also doubles as a
simulation for that puzzle.

At the moment, I just want to develop some functionality. Perhaps a GUI will
come later, but not now.
"""


class Piece:
    def __init__(self, bodyDisplayOption, faceDisplayOption):
        bodyDisplayOptions = {
            0: "O",
            1: "X"
            }
        faceDisplayOptions = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F"
            }
        self.in_order = (bodyDisplayOption == 0)
        self.body = bodyDisplayOptions.get(bodyDisplayOption)
        self.face = faceDisplayOptions.get(faceDisplayOption)
    def toStr(self):
        if self.in_order:
            return self.face + self.body
        return self.body+ self.face

def display(pieceArray):
    """
    solved state should look like
    
    A|  AO  O|X  XA  |A
     |      O|X      |
    B|  BO  O|X  XB  |B
     |      O|X      |
    C|  CO  O|X  XC  |C
     |      O|X      |
    D|  DO  O|X  XD  |D
     |      O|X      |
    E|  EO  O|X  XE  |E
     |      O|X      |
    F|  OF  O|X  XF  |F
    
    """
    
    print("")
    print("A|  %s  O|X  %s  |A" % (pieceArray[0].toStr(), pieceArray[6].toStr()))
    print(" |      O|X      | ")
    print("B|  %s  O|X  %s  |B" % (pieceArray[1].toStr(), pieceArray[7].toStr()))
    print(" |      O|X      | ")
    print("C|  %s  O|X  %s  |C" % (pieceArray[2].toStr(), pieceArray[8].toStr()))
    print(" |      O|X      | ")
    print("D|  %s  O|X  %s  |D" % (pieceArray[3].toStr(), pieceArray[9].toStr()))
    print(" |      O|X      | ")
    print("E|  %s  O|X  %s  |E" % (pieceArray[4].toStr(), pieceArray[10].toStr()))
    print(" |      O|X      | ")
    print("F|  %s  O|X  %s  |F" % (pieceArray[5].toStr(), pieceArray[11].toStr()))
    print("")
    

def swap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp

def move(pieceArray):
    move_1 = int(input("What move would you like to make?\n(swap across row: 0, shift left column upwards: 1\n"))
    if move_1 == 0:
        move_2 = int(input("which row would you like to flip? (from top to bottom, 0-5)\n"))
        # swap selected components
        swap(pieceArray, move_2, move_2 + 6)
    else:
        move_2 = int(input("how far would you like to shift left column upwards? (1-5)\n"))
        # swap selected components
        tmp = [pieceArray[0], pieceArray[1], pieceArray[2],
               pieceArray[3], pieceArray[4], pieceArray[5]]
        for i in range(6):
            pieceArray[i] = tmp[(i + move_2) % 6]
    return pieceArray

pieceArray = [
    Piece(0,0),
    Piece(0,1),
    Piece(0,2),
    Piece(0,3),
    Piece(0,4),
    Piece(0,5),
    Piece(1,0),
    Piece(1,1),
    Piece(1,2),
    Piece(1,3),
    Piece(1,4),
    Piece(1,5)
    ]
while(True):
    display(pieceArray)
    move(pieceArray)
    
    
    
            
        
    
    