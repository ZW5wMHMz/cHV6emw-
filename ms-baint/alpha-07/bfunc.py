#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import Libraries
import random


#=================
# Color Generators
#=================
HEX_CHARS_STR = "0123456789abcdef"
HEX_CHARS_ARR = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
HEX_4BIT_ARR = ("#FFFFFF", "#000000", "#808080", "#C0C0C0",
                "#FF0000", "#00FF00", "#0000FF",
                "#FFFF00", "#FF00FF", "#00FFFF",
                "#800000", "#008000", "#000080",
                "#808000", "#800080", "#008080")

def return_arr(array):
    """return array from module
    I don't know how not to make it hardcoded"""
    if array == "HEX_4BIT_ARR":
        return HEX_4BIT_ARR
    elif array == "HEX_CHARS_ARR":
        return HEX_CHARS_ARR
    else:
        print("Array not known")

def return_str(string):
    if string == "HEX_CHARS_STR":
        return HEX_CHARS_STR
    else:
        print("String not known")

def rand_color_hex():
    """generate random color hex"""
    color_hex = "#"
    for i in range(6):
        color_hex += random.choice(HEX_CHARS_STR)
    return color_hex


def color_shade_hex(color):
    """generate shades of color"""
    if color == "red" or "r":
        color_hex = "#"
        for i in range(2):
            color_hex += random.choice(HEX_CHARS_STR)
        color_hex += "0000"
    elif color == "blue" or "b":
        color_hex = "#0000"
        for i in range(2):
            color_hex += random.choice(HEX_CHARS_STR)
    elif color == "green" or "g":
        color_hex = "#00"
        for i in range(2):
            color_hex += random.choice(HEX_CHARS_STR)
        color_hex += "00"
    elif color == "yellow" or "y":
        color_hex = "#"
        color_hex_var = ""
        for m in range(2):
            color_hex_var += random.choice(HEX_CHARS_STR)
        color_hex += color_hex_var * 2
        color_hex += "00"
    return color_hex


