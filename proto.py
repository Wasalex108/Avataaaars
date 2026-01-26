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
       Y = 420
    if n%2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(barbe,X,Y)
    n=n+1
def Logo():
    global n
    if n%2 == 0:
       X = 500
       Y = 600
    if n%2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(lunette,X,Y)
    n=n+1
def Chapeau():
    global n
    if n%2 == 0:
       X = 375
       Y = 180
    if n%2 != 0:
       X = 1500
       Y = 1500
    Canevas.coords(chapeau,X,Y)
    n=n+1
def Choisir():
    if gender.get()=="garcon":
        Canevas.coords(Garcon,375,375)
        Canevas.coords(Fille,1500,1500)
    else :
        Canevas.coords(Fille,375,400)
        Canevas.coords(Garcon,1500,1500)

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

label_1 = Label(fenetre,text = "Avataaars",fg = 'red', bg = "light grey",font = "Garamond 50")
label_1.pack(padx = 5,pady = 5)

# Le canevas
frame_1 = Frame(fenetre,width = 350,height = 100,bg = "grey",bd = 20,relief = RAISED)
frame_1.pack(padx = 5,pady = 5)
Canevas = Canvas(fenetre,width = LARG,height = HAUT,bg ='light grey')
Canevas.pack(padx = 5,pady = 5)

image_Garcon = ImageTk.PhotoImage(file ="Garcon.png")
image_Fille = ImageTk.PhotoImage(file ="Fille.png")

image_barbe = ImageTk.PhotoImage(file ="Barbe.png")
barbe = Canevas.create_image(1500,1500, image = image_barbe)

image_logo = ImageTk.PhotoImage(file ="Logo.png")
lunette = Canevas.create_image(1500,1500, image = image_logo)

image_chapeau = ImageTk.PhotoImage(file ="Chapeau.png")
chapeau = Canevas.create_image(1500,1500, image = image_chapeau)

# Les boutons
bouton_quitter = Button(fenetre,text = " Quitter ",bg = 'red' ,command = fenetre.destroy)
bouton_quitter.pack(side = RIGHT,padx = 10,pady = 10)

bouton_choisir = Button(fenetre,text = " Choisir ",bg = 'grey',fg = 'red',command = Choisir)
bouton_choisir.pack(side = LEFT,padx = 10,pady = 10)

bouton_barbe = Button(fenetre,text = " Barbe ",bg = 'grey',fg = 'red',command = Barbe)
bouton_barbe.pack(side = LEFT,padx = 10,pady = 10)

bouton_lunette = Button(fenetre,text = " Logo ",bg = 'grey',fg = 'red',command = Logo)
bouton_lunette.pack(side = LEFT,padx = 180,pady = 10)

bouton_chapeau = Button(fenetre,text = " Chapeau ",bg = 'grey',fg = 'red',command = Chapeau)
bouton_chapeau.pack(side = LEFT,padx = 10,pady = 10)
# Les radioboutons

Garcon = Canevas.create_image(1500,1500, image = image_Garcon)
Fille = Canevas.create_image(1500,1500, image = image_Fille)

# envoyer les avatars en arrière pour que barbe/chapeau/lunette soient au-dessus
Canevas.tag_lower(Garcon)
Canevas.tag_lower(Fille)

gender = StringVar(value="garcon")


choix_garcon = Radiobutton(frame_1, text="Garçon", variable=gender, value="garcon")
choix_garcon.grid(row=0, column=0, padx=10, pady=5)

choix_fille = Radiobutton(frame_1, text="Fille", variable=gender, value="fille")
choix_fille.grid(row=0, column=1, padx=10, pady=5)
fenetre.mainloop()