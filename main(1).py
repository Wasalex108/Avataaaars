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
_bg_photo = None   # single background PhotoImage reference
_bg_id = None      # canvas id for the background image

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
def set_bg_image(path):
    """Load path and show its original size centered behind canvas content (no resizing)."""
    global _bg_photo, _bg_id
    try:
        img = Image.open(path).convert("RGBA")     # keep original size
        _bg_photo = ImageTk.PhotoImage(img)        # keep reference so GC doesn't remove it
        if _bg_id is None:
            # place centered on the canvas
            _bg_id = Canevas.create_image(LARG//2, HAUT//2, image=_bg_photo, anchor='center', tags='bg')
        else:
            Canevas.itemconfig(_bg_id, image=_bg_photo)
        Canevas.tag_lower('bg')  # send background behind everything
    except Exception as e:
        print(f"Can't load background '{path}': {e}")

def clear_bg():
    global _bg_photo, _bg_id
    if _bg_id is not None:
        try:
            Canevas.delete(_bg_id)
        except Exception:
            pass
    _bg_id = None
    _bg_photo = None
    Canevas.config(bg='light grey')
    try:
        label_1.config(bg='light grey')
    except Exception:
        pass

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
Canevas = Canvas(fenetre, width = LARG, height = HAUT, bg ='light grey')
Canevas.pack(padx = 5, pady = 5)

image_avatars = ImageTk.PhotoImage(file ="avatars.png")
avatars = Canevas.create_image(375, 375, image = image_avatars)


image_barbe = ImageTk.PhotoImage(file ="Barbe.png")
barbe = Canevas.create_image(1500, 1500, image = image_barbe)

image_logo = ImageTk.PhotoImage(file ="Logo.png")
lunette = Canevas.create_image(1500, 1500, image = image_logo)

image_chapeau = ImageTk.PhotoImage(file ="Chapeau.png")
chapeau = Canevas.create_image(1500, 1500, image = image_chapeau)


bouton_quitter = Button(fenetre, text = " Quitter ", bg = 'red', command = fenetre.destroy)
bouton_quitter.pack(side = RIGHT, padx = 10, pady = 10)

bouton_barbe = Button(fenetre, text = " Barbe ", bg = 'grey', fg = 'red', command = Barbe)
bouton_barbe.pack(side = LEFT, padx = 10, pady = 10)

bouton_lunette = Button(fenetre, text = " Logo ", bg = 'grey', fg = 'red', command = Logo)
bouton_lunette.pack(side = LEFT, padx = 180, pady = 10)

bouton_chapeau = Button(fenetre, text = " Chapeau ", bg = 'grey', fg = 'red', command = Chapeau)
bouton_chapeau.pack(side = LEFT, padx = 10, pady = 10)


bouton_jungle = Button(fenetre, text = " Jungle ", bg='forest green', fg='white', command = Jungle)
bouton_jungle.pack(side = LEFT, padx = 10, pady = 10)

bouton_space  = Button(fenetre, text = " Space  ", bg='black', fg='white', command = Space)
bouton_space.pack(side = LEFT, padx = 10, pady = 10)

bouton_city   = Button(fenetre, text = " City   ", bg='gray20', fg='white', command = City)
bouton_city.pack(side = LEFT, padx = 10, pady = 10)

bouton_clear  = Button(fenetre, text = " Clear  ", bg='light grey', fg='black', command = ClearFond)
bouton_clear.pack(side = LEFT, padx = 10, pady = 10)

fenetre.mainloop()







