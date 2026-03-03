# -*- coding: utf-8 *-*
#-----------------------------------------------------
# Cours 2_25 : Création objets TKinter
#-----------------------------------------------------
#
# On importe la bibliothèque graphique Tkinter
from tkinter import *
from random import randrange
from PIL import Image, ImageTk

#-----------------------------------------------------
# Les fonctions
#----------------------------------------------------
_bg_photo = None
_bg_id = None      # id pour l'image derrière
from random import choice

def Random_Avatar():
    choice([Jungle, Space, City, ClearFond])()
    Canevas.coords(barbe, choice([(375, 420), (1500, 1500)]))
    Canevas.coords(lunette, choice([(500, 600), (1500, 1500)]))
    Canevas.coords(chapeau, choice([(375, 180), (1500, 1500)]))

n = 2
def Barbe():
    global n
    if n % 2 == 0:
       X = 375
       Y = 420
    if n % 2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(barbe, X, Y)
    n = n + 1
def Logo():
    global n
    if n % 2 == 0:
       X = 500
       Y = 600
    if n % 2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(lunette, X, Y)
    n = n + 1
def Chapeau():
    global n
    if n % 2 == 0:
       X = 375
       Y = 180
    if n % 2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(chapeau, X, Y)
    n = n + 1
# Image de fond
bg_image = None
bg_item = None

def set_bg_image(path):
    global bg_image, bg_item
    bg_image = PhotoImage(file=path)

    # Si aucune image n'est encore affichée
    if bg_item is None:
        bg_item = Canevas.create_image(375, 375, image=bg_image)
    else:
        Canevas.itemconfig(bg_item, image=bg_image)

    # Mettre l'image derrière les les objet que je veut affiché

    Canevas.tag_lower(bg_item)

def clear_bg():
    global bg_image, bg_item
    if bg_item is not None:
        Canevas.delete(bg_item)
        bg_item = None
        bg_image = None

    Canevas.config(bg="light grey")
    label_1.config(bg="light grey")
def Jungle():
    set_bg_image("jungle.png")

def Space():
    set_bg_image("space.png")

def City():
    set_bg_image("city.png")

def ClearFond():
    clear_bg()

#-----------------------------------------------------
# Les constantes
#-----------------------------------------------------
LARG = 750      # Taille du canevas
HAUT = 750
TAILLE = 100   # Taille des objets

#-----------------------------------------------------
# Les fenetres
#-----------------------------------------------------
# On crée la fenêtre principale
fenetre = Tk()
fenetre.title("Graphique")

label_1 = Label(fenetre, text="Avataaars", fg='red', bg="light grey", font="Garamond 50")
label_1.pack(padx = 5, pady = 5)

# Le canevas
# Frame bordure
frame = Frame(fenetre, bg='green', bd=3)
frame.pack(padx=10, pady=10)

# canvas dedan
Canevas = Canvas(frame, width = LARG, height = HAUT, bg ='white')
Canevas.pack(padx=3, pady=3)

image_avatars = ImageTk.PhotoImage(file ="avatars.png")
avatars = Canevas.create_image(375, 375, image = image_avatars)


image_barbe = ImageTk.PhotoImage(file ="Barbe.png")
barbe = Canevas.create_image(1500, 1500, image = image_barbe)

image_logo = ImageTk.PhotoImage(file ="Logo.png")
lunette = Canevas.create_image(1500, 1500, image = image_logo)

image_chapeau = ImageTk.PhotoImage(file ="Chapeau.png")
chapeau = Canevas.create_image(1500, 1500, image = image_chapeau)


bouton_quitter = Button(fenetre, text = " Quitter(9)", bg = 'red', command = fenetre.destroy)
bouton_quitter.pack(side = RIGHT, padx = 50, pady = 10)

bouton_barbe = Button(fenetre, text = " Barbe(1) ", bg = 'grey', fg = 'white', command = Barbe)
bouton_barbe.pack(side = LEFT, padx = 50, pady = 10)

bouton_lunette = Button(fenetre, text = " Logo(2)", bg = 'grey', fg = 'white', command = Logo)
bouton_lunette.pack(side = LEFT, padx = 50, pady = 10)

bouton_chapeau = Button(fenetre, text = " Chapeau(3)", bg = 'grey', fg = 'white', command = Chapeau)
bouton_chapeau.pack(side = LEFT, padx = 50, pady = 10)


bouton_jungle = Button(fenetre, text = " Jungle(4)", bg='grey', fg='white', command = Jungle)
bouton_jungle.pack(side = LEFT, padx = 50, pady = 10)

bouton_space  = Button(fenetre, text = " Space(5)", bg='grey', fg='white', command = Space)
bouton_space.pack(side = LEFT, padx = 50, pady = 50)

bouton_city   = Button(fenetre, text = " City(6)", bg='grey', fg='white', command = City)
bouton_city.pack(side = LEFT, padx = 50, pady = 10)

bouton_clear  = Button(fenetre, text = " Clear(7)", bg='grey', fg='white', command = ClearFond)
bouton_clear.pack(side = LEFT, padx = 50, pady = 10)

Button(fenetre, text="Random(8)", bg='gold', command=Random_Avatar).pack(side=LEFT, padx=50, pady=10)

def key_handler(event):
    if event.char == '1':
        Barbe()
    elif event.char == '2':
        Logo()
    elif event.char == '3':
        Chapeau()
    elif event.char == '4':
        Jungle()
    elif event.char == '5':
        Space()
    elif event.char == '6':
        City()
    elif event.char == '7':
        ClearFond()
    elif event.char == '8':
        Random_Avatar()
    elif event.char == '9':
        fenetre.destroy()

fenetre.bind('<Key>', key_handler)

fenetre.mainloop()








