from tkinter import *
from customtkinter import *
import random

root = Tk()
root.title("Configuraciones Electrónicas")
root.geometry("500x300")
root.configure(background = "#D3D4D5")


elements =[
["h", None, None, None, None, None, None, "he"],
["li", "be", "b", "c", "n", "o", "f", "ne"],
["na", "mg", "al", "si", "p", "s", "cl", "ar"],
["k", "ca", "ga", "ge", "as", "se", "br", "kr"],
["rb", "sr", "in", "sn", "sb", "te", "i", "xe"]
]

streak = 0


def get_real_position(element):
    col = 1
    row = 1

    for i in elements:
        for j in i:
            if element == j:
                break
            col += 1
        if element == j:
            break
        row += 1
        col = 1

    x = col
    y = row

    return (x, y)


def get_configuration(x, y):
    config = "Internal Error"

    if y == 1:
        if x == 1:
            config = ("1s1",)
        if x == 8:
            config = ("1s2",)

    else:
        previous_noble_gas = elements[y-2][7]

        if y == 2 or y == 3:
            if x <= 2:
                config = (previous_noble_gas, f"{y}s{x}")
            if x > 2:
                config = (previous_noble_gas, f"{y}s2", f"{y}p{x-2}")
        
        if y == 4 or y == 5:
            if x <= 2:
                config = (previous_noble_gas, f"{y}s{x}")
            if x > 2:
                config = (previous_noble_gas, f"{y}s2", f"{y-1}d10", f"{y}p{x-2}")

    return config


def next_element():
    element_string = ""
    for i in elements:
        for j in i:
            if j != None:
                element_string += f"{j} "
    element_string = element_string[:-1]

    element_list = element_string.split(" ")

    random_element = random.choice(element_list)
    element_label.configure(text = random_element.capitalize())

    userinput_entry.delete(0, END)
    userinput_entry.insert(0, "")


def enter_pressed(event):
    global streak

    wrong = False

    element = element_label.text
    element_position = get_real_position(element.lower())
    element_configuration = get_configuration(element_position[0], element_position[1])
    userinput = userinput_entry.get()

    if " " in userinput:
        userconfig_list = userinput.split(" ")
    else:
        userconfig_list = (userinput,)

    if len(userconfig_list) == len(element_configuration):
        for i in userconfig_list:
            if i not in element_configuration:
                wrong = True
    else:
        wrong = True

    if wrong:
        configuration = ""
        for i in element_configuration:
            configuration += f"{i} "

        correction_label.configure(text = f"ERROR | Corrección: {element}: {configuration.capitalize()}")

        streak = 0
        streak_label.configure(text = f"RACHA:\n{streak}")
    
    else:
        correction_label.configure(text = "¡Correcto!")
        streak += 1
        streak_label.configure(text = f"RACHA:\n{streak}")

    next_element()


root.bind("<Return>", enter_pressed)


info_label = CTkLabel(
    text = "NOTA: Presiona enter cuando hayas     \ncompletado la configuración electrónica\npara pasar al siguiente elemento.           ",
    text_font = ("Arial", 13),
    master = root,
    fg_color = "#9EA6A9",
    corner_radius = 12,
    width = 370,
    height = 90,
    anchor = "w")
info_label.place(x = 10, y = 10)


streak_label = CTkLabel(
    text = f"RACHA:\n{streak}",
    text_font = ("Arial", 13),
    master = root,
    fg_color = "#9EA6A9",
    corner_radius = 12,
    width = 100,
    height = 60,
    anchor = "w")
streak_label.place(x = 390, y = 25)


element_label = CTkLabel(
    text = "Na",
    text_font = ("Arial", 30, "bold"),
    master = root,
    fg_color = "#9EA6A9",
    corner_radius = 12,
    width = 80,
    height = 60)
element_label.place(x = 40, y = 145)


userinput_entry = CTkEntry(
    placeholder_text = "Config. electrónica",
    text_font = ("Arial", 14),
    master = root,
    width = 300,
    height = 40,
    fg_color = "#afb6c1",
    corner_radius = 12,
    border_width = 1)
userinput_entry.place(x= 160, y = 155)


correction_label = CTkLabel(
    text = "¡Mucha suerte!",
    text_font = ("Arial", 14, "bold"),
    master = root,
    fg_color = "#9EA6A9",
    corner_radius = 12,
    width = 480,
    height = 40,
    anchor = "w")
correction_label.place(x = 10, y = 250)



root.mainloop()