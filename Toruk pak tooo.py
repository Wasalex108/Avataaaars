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

n=2
def Barbe():
    global n
    if n%2 == 0:
       X = 375
       Y = 375
    if n%2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(barbe,X,Y)
    n=n+1
def Lunette():
    global n
    if n%2 == 0:
       X = 375
       Y = 400
    if n%2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(lunette,X,Y)
    n=n+1
def Chapeau():
    global n
    if n%2 == 0:
       X = 375
       Y = 435
    if n%2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(chapeau,X,Y)
    n=n+1

#-----------------------------------------------------
# Les constantes
#-----------------------------------------------------
LARG=750      # Taille du canevas
HAUT=750
TAILLE = 100   # Taille des objets

#-----------------------------------------------------
# Les fenetres
#-----------------------------------------------------
# On crée la fenêtre principale
fenetre = Tk()
fenetre.title("Graphique")

label_1 = Label(fenetre,text = "Avataars",fg = 'red', bg = "cyan",font = "Arial 20 italic")
label_1.pack(padx = 5,pady = 5)

# Le canevas
Canevas = Canvas(fenetre,width = LARG,height = HAUT,bg ='cyan')
Canevas.pack(padx = 5,pady = 5)
image_avatars = ImageTk.PhotoImage(file ="avatars.png")
avatars = Canevas.create_image(375,375, image = image_avatars)

# On récupère l'image du vaisseau

image_barbe = ImageTk.PhotoImage(file ="Barbe.png")
barbe = Canevas.create_image(1500,1500, image = image_barbe)

image_lunette = ImageTk.PhotoImage(file ="Lunette.png")
lunette = Canevas.create_image(1500,1500, image = image_lunette)

image_chapeau = ImageTk.PhotoImage(file ="Chapeau.png")
chapeau = Canevas.create_image(1500,1500, image = image_chapeau)

# Les boutons
bouton_quitter = Button(fenetre,text = " Quitter ",bg = 'red' ,command = fenetre.destroy)
bouton_quitter.pack(side = RIGHT,padx = 10,pady = 10)

bouton_barbe = Button(fenetre,text = " Barbe ",bg = 'yellow',command = Barbe)
bouton_barbe.pack(side = LEFT,padx = 10,pady = 10)

bouton_lunette = Button(fenetre,text = " Lunette ",bg = 'yellow',command = Lunette)
bouton_lunette.pack(side = LEFT,padx = 180,pady = 10)

bouton_chapeau = Button(fenetre,text = " Chapeau ",bg = 'yellow',command = Chapeau)
bouton_chapeau.pack(side = LEFT,padx = 10,pady = 10)

fenetre.mainloop()



