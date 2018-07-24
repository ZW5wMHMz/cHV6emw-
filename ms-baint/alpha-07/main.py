#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple draw thingey
=====ALPHA-1=====
window with grid and palette on the bottom
=====ALPHA-2=====
Added 2nd window with palette
Grid can be activated by uncommentig draw_grid() in main()
=====ALPHA-3=====
Added box that takes in custom colors
Toggle grid by pressing <g>
=====ALPHA-4=====
Added current color window in CAN1
Added eraser
=====ALPHA-5=====
Added custom color palette
Added (shitty) verification to user input
=====ALPHA-6=====
Added palette and pixel map in save_img module
=====ALPHA-7=====
Remapped bindings to Ctrl-[old key]
"""

import tkinter
import tkFileDialog

import bfunc
import save_img

CAN = tkinter.Canvas(height=1000, width=1000)
CAN.pack()

CAN1_TOPLEVEL = tkinter.Toplevel()
CAN1 = tkinter.Canvas(CAN1_TOPLEVEL, width=400, height=300)
CAN1.pack()
ENTRY = tkinter.Entry(CAN1)
ERASER_IMG = tkinter.PhotoImage(file='eraser.png')

#define some useful dynamic constants
CAN1_BOTTOM = int(CAN1["height"])
CAN1_RIGHT = int(CAN1["width"])
EDGE_BOTTOM = 10

ROW = 100
COL = 100
SQUARE_A = int(CAN["width"]) / COL

color_arr = []
color_arr_i = 0
COLORS = bfunc.return_arr("HEX_4BIT_ARR")
color_i = 0
color_cust = ""
grid = False
eraser = False

save_img.create_map(COL, ROW)

#Define things for file header
VERSION = "alpha-7"

#========================
#Start of the actual code
#========================

def save_file(event):
    print event
    print "save_file function in use"
    file2write = save_img.return_file_content(VERSION, COL, ROW)
    file_save(file2write)

def ask_debug(event):
    print event.char
    if event.char == "Control-d":
        print save_img.send_debug("used_colors")
    elif event.char == "Control-f":
        print save_img.send_debug("pixel_map")

def draw_palette(i):
    """draw palette"""
    #pos_y = int(CAN["height"])
    if (i < int(CAN1["width"]) // 50):
        CAN1.create_rectangle(i*50, 0, (i+1)*50, 50, fill=COLORS[i], tag="plte")
    else:
        place = i-(int(CAN1["width"]) // 50)
        CAN1.create_rectangle(place*50, 50, (place+1)*50, 100, fill=COLORS[i], tag="plte")

def draw_custom():
    for i in range(len(color_arr)):
        #place = i-(int(CAN1["width"]) // 50)
        CAN1.create_rectangle(i*50, 100, (i+1)*50, 150, fill=color_arr[i], tag="plte_custom"+str(color_arr_i))

def on_click_can(event):
    """on mouse click"""
    print(event.x, event.y)
    num_x = event.x // SQUARE_A
    num_y = event.y // SQUARE_A
    pos_x = num_x * SQUARE_A
    pos_y = num_y * SQUARE_A
    tag = str(pos_x)+"#"+str(pos_y)
    CAN.delete(tag)
    if eraser == False:
        CAN.create_rectangle(pos_x, pos_y, pos_x+SQUARE_A, pos_y+SQUARE_A, fill=color, outline="", tag=tag)
        save_img.change_pixel(num_y, num_x, color)

def on_click_can1(event):
    global color_i, color, eraser
    if event.y < 50:
        color_i = event.x // 50
        color = COLORS[color_i]
        eraser = False
    elif (event.y > 50) and (event.y < 100):
        color_i = (event.x//50)+(int(CAN1["width"])//50)
        color = COLORS[color_i]
        eraser = False
	#Is this what ur searching for? https://discord.gg/XWwVwkx
    elif (event.y > 100) and (event.y < 150):
        eraser = False
        print event.x // 50 * len(color_arr)/8
        color = color_arr[event.x // 50 * len(color_arr)/8]
    elif event.y > CAN1_BOTTOM-60-EDGE_BOTTOM:
        if event.x > CAN1_RIGHT-50:
            eraser = True
            print "eraser enabled"
    update_color()

def reset(event):
    CAN.delete("all")

def get_color_hex(event):
    global color, color_arr, color_arr_i, eraser
    eraser = False
    check = ENTRY.get()
    if (check[0] == "#") and (len(check) == 7):
        color = ENTRY.get()
        print color
        if len(color_arr) < 8:
            color_arr.append(color)
        else:
            color_arr[color_arr_i] = color
            CAN1.delete("plte_custom"+str(color_arr_i))
            eraser = False
        if color_arr_i == 7:
            color_arr_i = 0
        else:
            color_arr_i += 1
        update_color()

def draw_grid():
    for x_pos in range(ROW):
        for y_pos in range(COL):
            CAN.create_rectangle(SQUARE_A*x_pos, SQUARE_A*y_pos,SQUARE_A*(x_pos+1), SQUARE_A*(y_pos+1), tag="grid")

def toggle_grid(event):
    global grid
    if grid == False:
        draw_grid()
        grid = True
    else:
        CAN.delete("grid")
        grid = False

def file_save(file2write):
    print "file_save function in use"
    dialog = tkFileDialog.asksaveasfile(mode='w', defaultextension=".baint")
    if dialog is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    dialog.write(file2write)
    dialog.close()

def open_file(event):
    save_img.open_file(tkFileDialog.askopenfilename(), VERSION)

def secondary_can():
    txt_size = 10
    CAN1.create_image(CAN1_RIGHT-25, CAN1_BOTTOM-25, image=ERASER_IMG)
    can1_txt_pos = int(CAN1["height"])-(txt_size/2)-EDGE_BOTTOM #Y of text in CAN1
    for i in range(len(COLORS)):
        draw_palette(i)
    CAN1.create_window(100, can1_txt_pos, window=ENTRY)

def update_color():
    global color
    CAN1.delete("current_color")
    if eraser == False:
        CAN1.create_rectangle(50, CAN1_BOTTOM-60-EDGE_BOTTOM, 100, CAN1_BOTTOM-10-EDGE_BOTTOM, fill=color, tag="current_color")
    elif eraser == True:
        CAN1.create_image(75, CAN1_BOTTOM-50, image=ERASER_IMG, tag="current_color")
    draw_custom()


def main():
    """main function"""
    secondary_can()


ENTRY.bind("<Return>", get_color_hex)
CAN.bind("<Button-1>", on_click_can)
CAN.bind("<B1-Motion>", on_click_can)
CAN1.bind("<Button-1>", on_click_can1)
CAN.bind_all("<Control-g>", toggle_grid)
CAN.bind_all("<Control-d>", ask_debug)
CAN.bind_all("<Control-f>", ask_debug)
CAN.bind_all("<Control-s>", save_file)
CAN.bind_all("<Control-o>", open_file)
CAN.bind_all("<Control-r>", reset)

main()

CAN.mainloop()
