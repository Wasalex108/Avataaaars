# -*- coding: utf-8 *-*
#
#-----------------------------------------------------
# Projet Hackathon
#-----------------------------------------------------
#
from PIL import Image

def rouge() :
    # Valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
    for x in range(largeur) :
        for y in range(hauteur) :
            pixel = im.getpixel((x, y))

    # Récuperer les valeurs des couleurs rouge, vert, bleu --> de im
            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]

    # Modification du pixel de coordonnées x, y --> dans im_new
            p_vert = 0
            p_bleu = 0
            im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))

    # Affichage et sauvegarde de l'image
##    im_new.save('sortie.png')
    im_new.show()

# Ouvrir l'image
im = Image.open("Lena_Couleur.jpg")

# informations sur l'image
largeur, hauteur = im.size
print(im.format, largeur, hauteur)
im.show() # Afficher l'image

# Créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (largeur, hauteur), (128, 128, 128))



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Modification de la taille de l'image
##image_retaille_1 = image_ini.resize((500, 200), Image.ANTIALIAS)
##image_retaille_1.show()
### ou
##facteur=0.4
##largeur_2 = int(largeur*facteur)
##hauteur_2 = int(hauteur*facteur)
##image_retaille_2 = image_ini.resize((largeur_2, hauteur_2), Image.ANTIALIAS)
##image_retaille_2.show()


