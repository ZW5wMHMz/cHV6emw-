#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for management of pixel map, saving and opening"""

import bfunc

HEX_4BIT_ARR = bfunc.return_arr("HEX_4BIT_ARR")

def send_debug(arr):
    if arr == "pixel_map":
        return pixel_map
    elif arr == "used_colors":
        return used_colors

#create pixel map and fill it with zeros
pixel_map = []
used_colors = [0]

#=============================================
#=Please don't mind the code between comments=
#=============================================

def pixel_rate_3rd(element_id, arr):
    count = [element_id]
    counter = 0
    while arr[element_id+counter] == arr[element_id+counter+1]:
        count.append(element_id+counter+1)
    arr[element_id] = str(counter)+str(arr[element_id])
    for xd in count:
        arr.pop(xd)
    return arr

def pixel_rate_2nd(arr):
    for element_id in range(len(arr)):
        return pixel_rate_3rd(element_id, arr)

def pixel_rate_1st(array2d):
    for array in array2d:
        return pixel_rate_2nd(array)

#=============================================
#=Please don't mind the code between comments=
#=============================================

def create_map(size_x, size_y):
    global pixel_map
    for i in range(size_y):
        temp_array = []
        for j in range(size_x):
            temp_array.append(0)
        pixel_map.append(temp_array)

def check_count_2d(array, element):
    count = 0
    for dimension in array:
        if element in dimension:
            count += 1
    return count

def change_pixel(arr1, arr2, color):
    global pixel_map, used_colors

    temp_var = pixel_map[arr1][arr2]

    if color not in used_colors:
        used_colors.append(color)
        pixel_map[arr1][arr2] = used_colors.index(color)
    else:
        pixel_map[arr1][arr2] = used_colors.index(color)

    if pixel_map[arr1][arr2] == 0:
        pass
    else:
        if check_count_2d(pixel_map, temp_var) > 0:
            print "*******PASSED********"
        elif check_count_2d(pixel_map, temp_var) == 0:
            used_colors[temp_var] = "NULL"

def prepare_head(version, size_x, size_y):
    file_head = "BAINT"+"$"+version+"$"+str(size_x)+"$"+str(size_y)+"^"
    return file_head


def lower_grid(null_id):
    global pixel_map
    for dimension in pixel_map:
        for element in dimension:
            if element >= null_id:
                element -= 1

def poppin_nulls():
    global pixel_map
    count = 0
    try:
        for color in range(len(used_colors)):
            print color
            if used_colors[color] == "NULL":
                lower_grid(color)
                used_colors.pop(color)
                count += 1
                print "popped"
            else:
                print "skipped"
    except IndexError:
        print "should be done lol"
    print "Popped", count, "elements."

def prepare_plte(colors):
    file_plte = ""
    poppin_nulls()
    for color in colors:
        print color
        file_plte += str(color)
    file_plte += "^"
    return file_plte


def prepare_map():
    file_map = ""
    for i in range(len(pixel_map)):
        for j in range(len(pixel_map[i])):
            file_map += str(pixel_map[i][j]) + "|"
        file_map += ";"
    return file_map

def return_file_content(version, size_x, size_y):
    file_head = prepare_head(version, size_x, size_y)
    file_plte = prepare_plte(used_colors)
    file_map = prepare_map()
    file_content = file_head+file_plte+file_map
    return file_content

#==========================
#== File Loading section ==
#==========================

def val_head(head, version):
    head_split = head.split("$")
    f_type = head_split[0]
    f_version = head_split[1]
    size_x = head_split[2]
    size_y = head_split[3]
    if f_type != "BAINT":
        print "NaNi? Bad header!?"
        return False
    if f_version != version:
        print "Different versions detected, problems might occur"
    return True

def get_plte(plte):
    global used_colors
    used_colors = [0]
    used_colors += plte

def get_p_map(p_map):
    global pixel_map
    rows = p_map.split(";")
    print rows
    pixel_map_tmp = []
    for row in rows:
        elems = row.split("|")
        elems.pop(len(elems)-1)
        elems = map(int, elems)
        pixel_map_tmp.append(elems)
    pixel_map_tmp.pop(len(pixel_map)-1)
    

def draw_p_map():
    for row in pixel_map:
        pass

def decode(content, version):
    splitted = content.split("^")
    head = splitted[0]
    plte = splitted[1]
    p_map = splitted[2]
    print head, plte, p_map
    if val_head(head, version):
        get_plte(plte)
        get_p_map(p_map)
        # draw_p_map()


def open_file(file_path, version):
    opened_file = open(file_path, "r")
    content = opened_file.read()
    decode(content, version)
