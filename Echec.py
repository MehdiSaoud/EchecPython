from upemtk import * #Biblihothèque de l'Université Paris Est Marne la vallée.

#Dimension du Jeu
taille_case = 10
largeur_plateau = 80
hauteur_plateau = 80

        
def milieu_case() : #Cette fonction renvoi les coordonnées du milieu de la case saisie par la souris
        MinAbs = 0
        MaxAbs = 100
        Abs = 50
        MinOrd = 0
        Ord = 50
        MaxOrd = 100
        while MaxAbs < 900 :
            if MinAbs < abscisse(ev) < MaxAbs :
                while MaxOrd < 900 :
                    if MinOrd < ordonnee(ev) < MaxOrd :
                        return (Abs,Ord)
                    MinOrd += 100
                    Ord += 100
                    MaxOrd += 100
            MinAbs += 100
            MaxAbs += 100
            Abs += 100
            
def message_debut(pions,lettre) : #Cette fonction affiche un message au début du jeu
    texte(largeur_plateau//2, hauteur_plateau//2, "                   La partie peut commencer\n                    Honneur aux pions noirs" ,couleur='black', ancrage='nw', police='Helvetica', taille=25, tag='')
    
def affiche_couleur_case() : #Cette fonction affiche les couleurs du plateau
    ax = 0
    ay = 0
    bx = 100
    by = 100
    while ax != 800 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 100
    ay = 100
    bx = 200 
    by = 200
    while ax != 900 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 0
    ay = 200
    bx = 100
    by = 300
    while ax != 800 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 100
    ay = 300
    bx = 200
    by = 400
    while ax != 900 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 0
    ay = 400
    bx = 100
    by = 500
    while ax != 800 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 100
    ay = 500
    bx = 200
    by = 600
    while ax != 900 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 0
    ay = 600
    bx = 100
    by = 700
    while ax != 800 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    ax = 100
    ay = 700
    bx = 200
    by = 800
    while ax != 900 :
        rectangle(ax, ay, bx, by, couleur='black', remplissage='grey', epaisseur=1)
        ax += 200
        bx += 200
    
        
                
                
def affiche_pions(pions,lettre) : #Cette fonction affiche tout les pions
    
    for i in range(8) :
        texte(pions[0][i][0],pions[0][i][1] , lettre[i] ,couleur='black', ancrage='center', police='Helvetica', taille=35, tag='')
    for i in range(8) :
        texte(pions[1][i][0],pions[1][i][1], "P" ,couleur='black', ancrage='center', police='Helvetica', taille=25, tag='')
    for i in range(8) :
        texte(pions[2][i][0],pions[2][i][1], "P" ,couleur='red', ancrage='center', police='Helvetica', taille=25, tag='')
    for i in range(8) :
        texte(pions[3][i][0],pions[3][i][1], lettre[i] ,couleur='red', ancrage='center', police='Helvetica', taille=35, tag='')
        
        
def Mange_pions(pions,Mange1,Mange2,Mange3,Mange4) : #Cette fonction permet à un pions d'en manger un autre lorsque leur coordonnées sont égales. Les varialbe Mange prennent la valeur de la nouvelle position d'un pions si celle ci est egal à un autre pions.
    for z in range(8) :
        if Mange1 == pions[2][z] or Mange2 == pions[2][z] :
            pions[2][z] = (900,900)
            return pions[2][z]
        elif Mange1 == pions[3][z] or Mange2 == pions[3][z] :
            pions[3][z] = (900,900)
            return pions[3][z]
        elif Mange3 == pions[0][z] or Mange4 == pions[0][z] :
            pions[0][z] = (900,900)
            return pions[0][z]
        elif Mange3 == pions[1][z] or Mange4 == pions[1][z] :
            pions[1][z] = (900,900)
            return pions[1][z]

    
def regle_pions(pions,i) : #Cette fonction donne les règles des petits pions
    if x == pions[1][i] :
        for elem in pions[2] :
            
            if elem[0] == pions[1][i][0] + 100 and elem[1] == pions[1][i][1] + 100 or elem[0] == pions[1][i][0] - 100 and elem[1] == pions[1][i][1] + 100 :
                if milieu_case()[1] == pions[1][i][1]+100 and milieu_case()[0] == pions[1][i][0] + 100 or milieu_case()[1] == pions[1][i][1]+100 and milieu_case()[0] == pions[1][i][0] - 100 :
                    return milieu_case() #Si un petit pion rouge se trouver en bas a gauche ou en bas a droite du pion noir, ce dernier peut aller sur lui.
            elif elem[0] == pions[1][i][0] and elem[1] == pions[1][i][1] + 100 :
                if milieu_case()[0] == pions[1][i][0] and milieu_case()[1] == pions[1][i][1] + 100 :
                    return pions[1][i] #Si un petit pion rouge se trouve en face d'un pion noir, ce dernier ne peut pas avancer.
        
        for elem in pions[3] :
            if elem[0] == pions[1][i][0] + 100 and elem[1] == pions[1][i][1] + 100 or elem[0] == pions[1][i][0] - 100 and elem[1] == pions[1][i][1] + 100 :
                if milieu_case()[1] == pions[1][i][1]+100 and milieu_case()[0] == pions[1][i][0] + 100 or milieu_case()[1] == pions[1][i][1]+100 and milieu_case()[0] == pions[1][i][0] - 100 :
                    return milieu_case() #Si un pion rouge se trouver en bas a gauche ou en bas a droite d'un pion noir, ce dernier peut aller sur lui.
            elif elem[0] == pions[1][i][0] and elem[1] == pions[1][i][1] + 100 :
                if milieu_case()[0] == pions[1][i][0] and milieu_case()[1] == pions[1][i][1] + 100 :
                    return pions[1][i] #Si un pion rouge se trouve en face d'un pion noir, ce dernier ne peut pas avancer.
        
        while pions[1][i][1] == 150 :
            if pions[1][i][1] < milieu_case()[1] <= pions[1][i][1] + 200 and milieu_case()[0] == pions[1][i][0] :
                return milieu_case()
            else :
                return pions[1][i] #A sa position initial le pion peu avancer de deux cases
       
        if milieu_case()[1] < pions[1][i][1] or milieu_case()[0] != pions[1][i][0] or milieu_case()[1] > pions[1][i][1] + 100 :
            return pions[1][i]
        else :
            return milieu_case() #Le pions ne peut pas retourner en arrière, ni aller sur le côté, ni avancer de plus d'une case.
    
    else :
        for elem in pions[1] :
         
            if elem[0] == pions[2][i][0] + 100 and elem[1] == pions[2][i][1] - 100 or elem[0] == pions[2][i][0] - 100 and elem[1] == pions[2][i][1] - 100 :
                if milieu_case()[1] == pions[2][i][1]-100 and milieu_case()[0] == pions[2][i][0] + 100 or milieu_case()[1] == pions[2][i][1]-100 and milieu_case()[0] == pions[2][i][0] - 100 :
                    return milieu_case() #Si un petit pion noir se trouver en haut a gauche ou en haut a droite du pion rouge, ce dernier peut aller sur lui.
            elif elem[0] == pions[2][i][0] and elem[1] == pions[2][i][1] - 100 :
                if milieu_case()[0] == pions[2][i][0] and milieu_case()[1] == pions[2][i][1] - 100 :
                    return pions[2][i] #Si un petit pion noir se trouve en face d'un pion rouge, ce dernier ne peut pas avancer.
       
        for elem in pions[0] :
            if elem[0] == pions[2][i][0] + 100 and elem[1] == pions[2][i][1] - 100 or elem[0] == pions[2][i][0] - 100 and elem[1] == pions[2][i][1] - 100 :
                if milieu_case()[1] == pions[2][i][1]-100 and milieu_case()[0] == pions[2][i][0] + 100 or milieu_case()[1] == pions[2][i][1]-100 and milieu_case()[0] == pions[2][i][0] - 100 :
                    return milieu_case() #Si un pion noir se trouver en haut a gauche ou en haut a droite d'un pion rouge, ce dernier peut aller sur lui.
            elif elem[0] == pions[2][i][0] and elem[1] == pions[2][i][1] - 100 :
                if milieu_case()[0] == pions[2][i][0] and milieu_case()[1] == pions[2][i][1] - 100 :
                    return pions[2][i] #Si un pion noir se trouve en face d'un pion rouge, ce dernier ne peut pas avancer.
       
        while pions[2][i][1] == 650 :
            if pions[2][i][1] > milieu_case()[1] >= pions[2][i][1] -200 and milieu_case()[0] == pions[2][i][0] :
                return milieu_case()
            else :
                return pions[2][i] #A sa position initial le pion peu avancer de deux cases
        
        if milieu_case()[1] > pions[2][i][1] or milieu_case()[0] != pions[2][i][0] or milieu_case()[1] < pions[2][i][1] - 100:
            return pions[2][i]
        else :
            return milieu_case() #Le pions ne peut pas retourner en arrière, ni aller sur le côté, ni avancer de plus d'une case.
            


def regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) : #Cette fonction donne les regle de la tour
       
        if milieu_case()[0] != pions[i1][i2][0] and milieu_case()[1] != pions[i1][i2][1] :
            return pions[i1][i2] #La tour ne peut aller que tout droit ou sur le coter
        
        elif  milieu_case() == pions[i1][i2] :
            return pions[i1][i2]
       
        elif milieu_case()[0] > pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] : #Si la tour va à droite
            z = 100
            while z < 800 :
                for y in range(8) :
                    if pions[iA1][y][0] == pions[i1][i2][0] + z and pions[iA1][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] >= pions[iA1][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] >= pions[iA2][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :
                        if pions[Enn][y][0] == pions[i1][i2][0] + z and pions[Enn][y][1] == pions[i1][i2][1] :
                            if milieu_case()[0] > pions[Enn][y][0] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemi
                z += 100
            return milieu_case()
        
        elif milieu_case()[0] < pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] : #Si la tour va a gauche
            z = 100
            while z < 800 :
                for y in range(8) :
                    if pions[iA1][y][0] == pions[i1][i2][0] - z and pions[iA1][y][1] == pions[i1][i2][1] :                 
                        if milieu_case()[0] <= pions[iA1][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] <= pions[iA2][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :
                        if pions[Enn][y][0] == pions[i1][i2][0] - z and pions[Enn][y][1] == pions[i1][i2][1] :                 
                            if milieu_case()[0] < pions[Enn][y][0] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                z += 100
            return milieu_case()
            
        elif milieu_case()[1] > pions[i1][i2][1] and milieu_case()[0] == pions[i1][i2][0] :    #Si la tour va en bas
            z = 100
            while z < 800 :
                for y in range(8) :
                    if pions[iA1][y][1] == pions[i1][i2][1] + z and pions[iA1][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] >= pions[iA1][y][1] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][1] == pions[i1][i2][1] + z and pions[iA2][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] >= pions[iA2][y][1] :
                            return pions[i1][i2]                    
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :
                        if pions[Enn][y][1] == pions[i1][i2][1] + z and pions[Enn][y][0] == pions[i1][i2][0] :
                            if milieu_case()[1] > pions[Enn][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemi
                z += 100
            return milieu_case()
        
        elif milieu_case()[1] < pions[i1][i2][1] and milieu_case()[0] == pions[i1][i2][0] : #Si la tour va en haut
            z = 100
            while z < 800 :
                for y in range(8) :            
                    if pions[iA1][y][1] == pions[i1][i2][1] - z and pions[iA1][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] <= pions[iA1][y][1] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][1] == pions[i1][i2][1] - z and pions[iA2][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] <= pions[iA2][y][1] :
                            return pions[i1][i2]
                        else : 
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :          
                        if pions[Enn][y][1] == pions[i1][i2][1] - z and pions[Enn][y][0] == pions[i1][i2][0] :
                            if milieu_case()[1] < pions[Enn][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                z += 100
            return milieu_case()
        
        
def regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) : #Cette fonction donne les regle du fou
            
        if milieu_case()[0] != pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] or milieu_case()[0] == pions[i1][i2][0] and milieu_case()[1] != pions[i1][i2][1] :
            return pions[i1][i2] # Le fou ne peut pas aller tout droit
        
        elif  milieu_case() == pions[i1][i2] :
            return pions[i1][i2]
            
        p = 100
        while p < 800 :
            if milieu_case()[0] == pions[i1][i2][0] + p and milieu_case()[1] == pions[i1][i2][1] + p : #Si le fou va en bas a droite
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] + z and pions[iA1][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] >= pions[iA1][y][0] and milieu_case()[1] >= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(8) :
                        for Enn in range(iE1,iE2) :
                            if pions[Enn][y][0] == pions[i1][i2][0] + z and pions[Enn][y][1] == pions[i1][i2][1] + z :
                                if milieu_case()[0] > pions[Enn][y][0] and milieu_case()[1] > pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Il ne peut pas passer par dessus un pions ennemie
                    z += 100
                return milieu_case()
        
            elif milieu_case()[0] == pions[i1][i2][0] + p and milieu_case()[1] == pions[i1][i2][1] - p : #Si le fou va en haut a droite
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] + z and pions[iA1][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] >= pions[iA1][y][0] and milieu_case()[1] <= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(8) :
                        for Enn in range(iE1,iE2) :
                            if pions[Enn][y][0] == pions[i1][i2][0] + z and pions[Enn][y][1] == pions[i1][i2][1] - z :
                                if milieu_case()[0] > pions[Enn][y][0] and milieu_case()[1] < pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Il ne peut pas passer par dessus un pions ennemie
                    z += 100
                return milieu_case()
            
            elif milieu_case()[0] == pions[i1][i2][0] - p and milieu_case()[1] == pions[i1][i2][1] + p : #Si le fou va en bas a gauche
            
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] - z and pions[iA1][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] <= pions[iA1][y][0] and milieu_case()[1] >= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] +  z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for Enn in range(iE1,iE2) :
                        for y in range(8) :
                            if pions[Enn][y][0] == pions[i1][i2][0] - z and pions[Enn][y][1] == pions[i1][i2][1] + z :
                                if milieu_case()[0] < pions[Enn][y][0] and milieu_case()[1] > pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Il ne peut pas passer par dessus un pions ennemie
                        z += 100
                return milieu_case()
            
            elif milieu_case()[0] == pions[i1][i2][0] - p and milieu_case()[1] == pions[i1][i2][1] - p : #Si le fou va en haut a gauche 
            
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] - z and pions[iA1][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] <= pions[iA1][y][0] and milieu_case()[1] <= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] -  z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Il ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(8) :
                        for Enn in range(iE1,iE2) :
                            if pions[Enn][y][0] == pions[i1][i2][0] - z and pions[Enn][y][1] == pions[i1][i2][1] - z :
                                if milieu_case()[0] < pions[Enn][y][0] and milieu_case()[1] < pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Il ne peut pas passer par dessus un pions ennemie
                    z += 100
                return milieu_case()
            p += 100
        return pions[i1][i2]
            
def regle_dame(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) : #Cette fonction donne les regles de la dame
        
        if  milieu_case() == pions[i1][i2] :
            return pions[i1][i2]
       
        elif milieu_case()[0] > pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] : #Si la dame va a droite
            z = 100
            while z < 800 :
                for y in range(8) :
                    if pions[iA1][y][0] == pions[i1][i2][0] + z and pions[iA1][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] >= pions[iA1][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] >= pions[iA2][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA2+1,8) :
                    if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] >= pions[iA2][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :
                        if pions[Enn][y][0] == pions[i1][i2][0] + z and pions[Enn][y][1] == pions[i1][i2][1] :
                            if milieu_case()[0] > pions[Enn][y][0] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                z += 100
            return milieu_case()
        
        elif milieu_case()[0] < pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] : #Si la dame va a gauche
            z = 100
            while z < 800 :
                for y in range(8) :
                    if pions[iA1][y][0] == pions[i1][i2][0] - z and pions[iA1][y][1] == pions[i1][i2][1] :                 
                        if milieu_case()[0] <= pions[iA1][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] <= pions[iA2][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA2+1,8) :
                    if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] :
                        if milieu_case()[0] <= pions[iA2][y][0] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :
                        if pions[Enn][y][0] == pions[i1][i2][0] - z and pions[Enn][y][1] == pions[i1][i2][1] :                 
                            if milieu_case()[0] < pions[Enn][y][0] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                z += 100
            return milieu_case()
            
        elif milieu_case()[1] > pions[i1][i2][1] and milieu_case()[0] == pions[i1][i2][0] :    #Si la dame va en haut
            z = 100
            while z < 800 :
                for y in range(8) :
                    if pions[iA1][y][1] == pions[i1][i2][1] + z and pions[iA1][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] >= pions[iA1][y][1] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][1] == pions[i1][i2][1] + z and pions[iA2][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] >= pions[iA2][y][1] :
                            return pions[i1][i2]                    
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA2+1,8) :
                    if pions[iA2][y][1] == pions[i1][i2][1] + z and pions[iA2][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] >= pions[iA2][y][1] :
                            return pions[i1][i2]                    
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :
                        if pions[Enn][y][1] == pions[i1][i2][1] + z and pions[Enn][y][0] == pions[i1][i2][0] :
                            if milieu_case()[1] > pions[Enn][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                z += 100
            return milieu_case()
        
        elif milieu_case()[1] < pions[i1][i2][1] and milieu_case()[0] == pions[i1][i2][0] : #Si la dame va en bas
            z = 100
            while z < 800 :
                for y in range(8) :            
                    if pions[iA1][y][1] == pions[i1][i2][1] - z and pions[iA1][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] <= pions[iA1][y][1] :
                            return pions[i1][i2]
                        else :
                            return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA1,irangeA2) :
                    if pions[iA2][y][1] == pions[i1][i2][1] - z and pions[iA2][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] <= pions[iA2][y][1] :
                            return pions[i1][i2]
                        else : 
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(irangeA2+1,8) :
                    if pions[iA2][y][1] == pions[i1][i2][1] - z and pions[iA2][y][0] == pions[i1][i2][0] :
                        if milieu_case()[1] <= pions[iA2][y][1] :
                            return pions[i1][i2]
                        else : 
                            return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                z += 100
            z = 100
            while z < 800 :
                for y in range(8) :
                    for Enn in range(iE1,iE2) :          
                        if pions[Enn][y][1] == pions[i1][i2][1] - z and pions[Enn][y][0] == pions[i1][i2][0] :
                            if milieu_case()[1] < pions[Enn][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                z += 100
            return milieu_case()
        
        p = 100
        while p < 800 :
            if milieu_case()[0] == pions[i1][i2][0] + p and milieu_case()[1] == pions[i1][i2][1] + p : #Si la dame va en bas a droite
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] + z and pions[iA1][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] >= pions[iA1][y][0] and milieu_case()[1] >= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] + z :  
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(8) :
                        for Enn in range(iE1,iE2) :
                            if pions[Enn][y][0] == pions[i1][i2][0] + z and pions[Enn][y][1] == pions[i1][i2][1] + z :
                                if milieu_case()[0] > pions[Enn][y][0] and milieu_case()[1] > pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                    z += 100
                return milieu_case()
            
            elif milieu_case()[0] == pions[i1][i2][0] + p and milieu_case()[1] == pions[i1][i2][1] - p : #Si la dame va en haut a droite
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] + z and pions[iA1][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] >= pions[iA1][y][0] and milieu_case()[1] <= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] + z and pions[iA2][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(8) :
                        for Enn in range(iE1,iE2) :
                            if pions[Enn][y][0] == pions[i1][i2][0] + z and pions[Enn][y][1] == pions[i1][i2][1] - z :
                                if milieu_case()[0] > pions[Enn][y][0] and milieu_case()[1] < pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                    z += 100
                return milieu_case()
            
            elif milieu_case()[0] == pions[i1][i2][0] - p and milieu_case()[1] == pions[i1][i2][1] + p : #Si la dame va en bas a gauche
            
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] - z and pions[iA1][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] <= pions[iA1][y][0] and milieu_case()[1] >= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] + z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] +  z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for Enn in range(iE1,iE2) :
                        for y in range(8) :
                            if pions[Enn][y][0] == pions[i1][i2][0] - z and pions[Enn][y][1] == pions[i1][i2][1] + z :
                                if milieu_case()[0] < pions[Enn][y][0] and milieu_case()[1] > pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                        z += 100
                return milieu_case()
            
            elif milieu_case()[0] == pions[i1][i2][0] - p and milieu_case()[1] == pions[i1][i2][1] - p : #Si la dame va en haut a gauche 
                z = 100
                while z < 800 :
                    for y in range(8) :
                        if pions[iA1][y][0] == pions[i1][i2][0] - z and pions[iA1][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] <= pions[iA1][y][0] and milieu_case()[1] <= pions[iA1][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un petit pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA1,irangeA2) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] - z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(irangeA2+1,8) :
                        if pions[iA2][y][0] == pions[i1][i2][0] - z and pions[iA2][y][1] == pions[i1][i2][1] -  z :
                            if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                                return pions[i1][i2]
                            else :
                                return milieu_case() #Elle ne peut pas passer par dessus un pions allié
                    z += 100
                z = 100
                while z < 800 :
                    for y in range(8) :
                        for Enn in range(iE1,iE2) :
                            if pions[Enn][y][0] == pions[i1][i2][0] - z and pions[Enn][y][1] == pions[i1][i2][1] - z :
                                if milieu_case()[0] < pions[Enn][y][0] and milieu_case()[1] < pions[Enn][y][1] :
                                    return pions[i1][i2]
                                else :
                                    return milieu_case() #Elle ne peut pas passer par dessus un pions ennemie
                    z += 100
                return milieu_case()
            p += 100
        return pions[i1][i2]
            
            
def regle_roi(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) : #Cette fonction donne les regles du roi
    
    if  milieu_case() == pions[i1][i2] :
        return pions[i1][i2]
        
    elif milieu_case()[0] > pions[i1][i2][0] + 100 or milieu_case()[0] < pions[i1][i2][0] - 100 or milieu_case()[1] > pions[i1][i2][1] + 100 or milieu_case()[1] < pions[i1][i2][1] - 100 : 
        return pions[i1][i2] #Le roi ne peut avancer que d'une seul case
       
    elif milieu_case()[0] > pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] : #Si le roi va sur a droite
        
        for y in range(8) :
            if pions[iA1][y][0] == pions[i1][i2][0] + 100 and pions[iA1][y][1] == pions[i1][i2][1] :
                if milieu_case()[0] >= pions[iA1][y][0] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
        
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][0] == pions[i1][i2][0] + 100 and pions[iA2][y][1] == pions[i1][i2][1] :
                if milieu_case()[0] >= pions[iA2][y][0] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
   
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][0] == pions[i1][i2][0] + 100 and pions[iA2][y][1] == pions[i1][i2][1] :
                if milieu_case()[0] >= pions[iA2][y][0] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
    
        for y in range(8) :
            for Enn in range(iE1,iE2) :
                if pions[Enn][y][0] == pions[i1][i2][0] + 100 and pions[Enn][y][1] == pions[i1][i2][1] :
                    if milieu_case()[0] > pions[Enn][y][0] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion allié ennemie
        return milieu_case()
        
    elif milieu_case()[0] < pions[i1][i2][0] and milieu_case()[1] == pions[i1][i2][1] : #Si le roi va a gauche
    
        for y in range(8) :
            if pions[iA1][y][0] == pions[i1][i2][0] - 100 and pions[iA1][y][1] == pions[i1][i2][1] :                 
                if milieu_case()[0] <= pions[iA1][y][0] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
               
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][0] == pions[i1][i2][0] - 100 and pions[iA2][y][1] == pions[i1][i2][1] :
                if milieu_case()[0] <= pions[iA2][y][0] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
             
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][0] == pions[i1][i2][0] - 100 and pions[iA2][y][1] == pions[i1][i2][1] :
                if milieu_case()[0] <= pions[iA2][y][0] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
               
        for y in range(8) :
            for Enn in range(iE1,iE2) :
                if pions[Enn][y][0] == pions[i1][i2][0] - 100 and pions[Enn][y][1] == pions[i1][i2][1] :                 
                    if milieu_case()[0] < pions[Enn][y][0] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
        return milieu_case()
            
    elif milieu_case()[1] > pions[i1][i2][1] and milieu_case()[0] == pions[i1][i2][0] :    #Si le roi va en bas
        
        for y in range(8) :
            if pions[iA1][y][1] == pions[i1][i2][1] + 100 and pions[iA1][y][0] == pions[i1][i2][0] :
                if milieu_case()[1] >= pions[iA1][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
     
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][1] == pions[i1][i2][1] + 100 and pions[iA2][y][0] == pions[i1][i2][0] :
                if milieu_case()[1] >= pions[iA2][y][1] :
                    return pions[i1][i2]                    
                else :
                    return milieu_case()#Il ne peut pas passer par dessus un pion allié
         
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][1] == pions[i1][i2][1] + 100 and pions[iA2][y][0] == pions[i1][i2][0] :
                if milieu_case()[1] >= pions[iA2][y][1] :
                    return pions[i1][i2]                    
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
               
        for y in range(8) :
            for Enn in range(iE1,iE2) :
                if pions[Enn][y][1] == pions[i1][i2][1] + 100 and pions[Enn][y][0] == pions[i1][i2][0] :
                    if milieu_case()[1] > pions[Enn][y][1] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
        return milieu_case()
        
    elif milieu_case()[1] < pions[i1][i2][1] and milieu_case()[0] == pions[i1][i2][0] : #Si le roi va en haut 
    
        for y in range(8) :            
            if pions[iA1][y][1] == pions[i1][i2][1] - 100 and pions[iA1][y][0] == pions[i1][i2][0] :
                if milieu_case()[1] <= pions[iA1][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
             
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][1] == pions[i1][i2][1] - 100 and pions[iA2][y][0] == pions[i1][i2][0] :
                if milieu_case()[1] <= pions[iA2][y][1] :
                    return pions[i1][i2]
                else : 
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
             
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][1] == pions[i1][i2][1] - 100 and pions[iA2][y][0] == pions[i1][i2][0] :
                if milieu_case()[1] <= pions[iA2][y][1] :
                    return pions[i1][i2]
                else : 
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
               
        for y in range(8) :
            for Enn in range(iE1,iE2) :          
                if pions[Enn][y][1] == pions[i1][i2][1] - 100 and pions[Enn][y][0] == pions[i1][i2][0] :
                    if milieu_case()[1] < pions[Enn][y][1] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
            return milieu_case()
        
    elif milieu_case()[0] > pions[i1][i2][0] and milieu_case()[1] > pions[i1][i2][1] : #Si le roi va en bas a droite
        for y in range(8) :
            if pions[iA1][y][0] == pions[i1][i2][0] + 100 and pions[iA1][y][1] == pions[i1][i2][1] + 100 :
                if milieu_case()[0] >= pions[iA1][y][0] and milieu_case()[1] >= pions[iA1][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
      
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][0] == pions[i1][i2][0] + 100 and pions[iA2][y][1] == pions[i1][i2][1] + 100 :
                if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
            
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][0] == pions[i1][i2][0] + 100 and pions[iA2][y][1] == pions[i1][i2][1] + 100 :
                if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
            
        for y in range(8) :
            for Enn in range(iE1,iE2) :
                if pions[Enn][y][0] == pions[i1][i2][0] + 100 and pions[Enn][y][1] == pions[i1][i2][1] + 100 :
                    if milieu_case()[0] > pions[Enn][y][0] and milieu_case()[1] > pions[Enn][y][1] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
        return milieu_case()
            
    elif milieu_case()[0] > pions[i1][i2][0] and milieu_case()[1] < pions[i1][i2][1] : #Si le roi va en haut a droite
    
        for y in range(8) :
            if pions[iA1][y][0] == pions[i1][i2][0] + 100 and pions[iA1][y][1] == pions[i1][i2][1] - 100 :
                if milieu_case()[0] >= pions[iA1][y][0] and milieu_case()[1] <= pions[iA1][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
        
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][0] == pions[i1][i2][0] + 100 and pions[iA2][y][1] == pions[i1][i2][1] - 100 :
                if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
            
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][0] == pions[i1][i2][0] + 100 and pions[iA2][y][1] == pions[i1][i2][1] - 100 :
                if milieu_case()[0] >= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
            
        for y in range(8) :
            for Enn in range(iE1,iE2) :
                if pions[Enn][y][0] == pions[i1][i2][0] + 100 and pions[Enn][y][1] == pions[i1][i2][1] - 100 :
                    if milieu_case()[0] > pions[Enn][y][0] and milieu_case()[1] < pions[Enn][y][1] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
        return milieu_case()
            
    elif milieu_case()[0] < pions[i1][i2][0] and milieu_case()[1] > pions[i1][i2][1] : #Si le roi va en bas a gauche
        
        for y in range(8) :
            if pions[iA1][y][0] == pions[i1][i2][0] - 100 and pions[iA1][y][1] == pions[i1][i2][1] + 100 :
                if milieu_case()[0] <= pions[iA1][y][0] and milieu_case()[1] >= pions[iA1][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
      
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][0] == pions[i1][i2][0] - 100 and pions[iA2][y][1] == pions[i1][i2][1] + 100 :
                if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
               
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][0] == pions[i1][i2][0] - 100 and pions[iA2][y][1] == pions[i1][i2][1] +  100 :
                if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] >= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
              
        for Enn in range(iE1,iE2) :
            for y in range(8) :
                if pions[Enn][y][0] == pions[i1][i2][0] - 100 and pions[Enn][y][1] == pions[i1][i2][1] + 100 :
                    if milieu_case()[0] < pions[Enn][y][0] and milieu_case()[1] > pions[Enn][y][1] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
        return milieu_case()
            
    elif milieu_case()[0] < pions[i1][i2][0] and milieu_case()[1] < pions[i1][i2][1] : #Si le roi va en haut a gauche
          
        for y in range(8) :
            if pions[iA1][y][0] == pions[i1][i2][0] - 100 and pions[iA1][y][1] == pions[i1][i2][1] - 100 :
                if milieu_case()[0] <= pions[iA1][y][0] and milieu_case()[1] <= pions[iA1][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un petit pion allié
           
        for y in range(irangeA1,irangeA2) :
            if pions[iA2][y][0] == pions[i1][i2][0] - 100 and pions[iA2][y][1] == pions[i1][i2][1] - 100 :
                if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
              
        for y in range(irangeA2+1,8) :
            if pions[iA2][y][0] == pions[i1][i2][0] - 100 and pions[iA2][y][1] == pions[i1][i2][1] -  100 :
                if milieu_case()[0] <= pions[iA2][y][0] and milieu_case()[1] <= pions[iA2][y][1] :
                    return pions[i1][i2]
                else :
                    return milieu_case() #Il ne peut pas passer par dessus un pion allié
               
        for y in range(8) :
            for Enn in range(iE1,iE2) :
                if pions[Enn][y][0] == pions[i1][i2][0] - 100 and pions[Enn][y][1] == pions[i1][i2][1] - 100 :
                    if milieu_case()[0] < pions[Enn][y][0] and milieu_case()[1] < pions[Enn][y][1] :
                        return pions[i1][i2]
                    else :
                        return milieu_case() #Il ne peut pas passer par dessus un pion ennemie
        return milieu_case()
        
def regle_cavalier(pions,i1,i2,iA1,iA2) : #Cette fonction donnent les regle du cavalier
            
    if milieu_case() in pions[iA1] or milieu_case() in pions[iA2] or milieu_case() == pions[i1][i2] :
                return pions[i1][i2] #Le cavalier ne peut pas aller a la même place que ses allié
            
    elif milieu_case()[0] == pions[i1][i2][0] + 200 and milieu_case()[1] == pions[i1][i2][1] + 100  or milieu_case()[0] == pions[i1][i2][0] + 200 and milieu_case()[1] == pions[i1][i2][1] - 100 or milieu_case()[0] == pions[i1][i2][0] - 200 and milieu_case()[1] == pions[i1][i2][1] + 100 or milieu_case()[0] == pions[i1][i2][0] - 200 and milieu_case()[1] == pions[i1][i2][1] - 100 or milieu_case()[1] == pions[i1][i2][1] + 200 and milieu_case()[0] == pions[i1][i2][0] + 100  or milieu_case()[1] == pions[i1][i2][1] + 200 and milieu_case()[0] == pions[i1][i2][0] - 100 or milieu_case()[1] == pions[i1][i2][1] - 200 and milieu_case()[0] == pions[i1][i2][0] + 100 or milieu_case()[1] == pions[i1][i2][1] - 200 and milieu_case()[0] == pions[i1][i2][0] - 100 :
        return milieu_case() #Le cavalier se deplace en L
            
    else :
        return pions[i1][i2]
      
        
    
    
#Programme Principal

#Initialisation du jeu

x = 0 #Cette variable va devenir une copie des coordonnee tu premier clic Gauche. On l'utilisera pour savoir quel pions a ete saisie
Mange1 = 0
Mange2 = 0
Mange3 = 0 #Les varialbe Mange prennent la valeur de la nouvelle position d'un pions lorsqu'elle est égal à un pion ennemie.
Mange4 = 0
tour = 1 #Cette variable permet le jeu à tour de rôle.
pions = [[(50,50),(150,50),(250,50),(350,50),(450,50),(550,50),(650,50),(750,50)],
        [(50,150),(150,150),(250,150),(350,150),(450,150),(550,150),(650,150),(750,150)],
        [(50,650),(150,650),(250,650),(350,650),(450,650),(550,650),(650,650),(750,650)],
        [(50,750),(150,750),(250,750),(350,750),(450,750),(550,750),(650,750),(750,750)]]
         #Liste des position initial de tout les pions : pions[0] = Les pions spéciaux noir ; pions[1] = les petit pions noir ; pions[2] = les petit pions rouge ; pions[3] = les pions spéciaux rouge.
         
lettre = ["T","C","F","R","D","F","C","T"] #Liste utilisee dans la fonction affiche_pions

cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)

                 
#Boucle Principal
while True :
    
    #Affichage des objets
    if pions[0][3] == (900,900) :
        efface_tout()
        texte(largeur_plateau//2, hauteur_plateau//2, "Les pions rouges ont gagné !",couleur='black', ancrage='nw', police='Helvetica', taille=25, tag='')
        break
    elif pions[3][3] == (900,900) :
        efface_tout()
        texte(largeur_plateau//2, hauteur_plateau//2, "Les pions noirs ont gagné !",couleur='black', ancrage='nw', police='Helvetica', taille=25, tag='')
        break #Si le Roi meurt, la partie est finit
    affiche_couleur_case()
    message_debut(pions,lettre)
    mise_a_jour()
    
    #Gestion des évènement
    ev = donne_ev()
    ty = type_ev(ev)
    if ty == 'Quitte':
        break
    elif ty == "ClicGauche" : #Saisie d'un pion
        message_debut = affiche_pions
        x = milieu_case() #x prend la valeur des coordonné du pions saisie
        for i in range(8) :
            if tour%2 != 0 : #Lorsque tour est impair c'est aux pions noir de jouer
                if pions[0][i] == x :
                    ev = attend_ev()
                    ty = type_ev(ev)
                    if ty == "ClicGauche" : #Destination du pions
                        if milieu_case() in pions[0] or milieu_case() in pions[1] :
                            tour = tour
                        else :
                            if x == pions[0][0] :
                                i1 = 0
                                i2 = 0
                                iA1 = 1
                                iA2 = 0
                                irangeA1 = 1
                                irangeA2 = 8
                                iE1 = 2
                                iE2 = 4
                                if regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[0][0] :
                                    pions[0][0] = regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[0][0] in pions[2] or pions[0][0] in pions[3] :
                                        Mange1 = pions[0][0]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[0][7] :
                                i1 = 0
                                i2 = 7
                                iA1 = 1
                                iA2 = 0
                                irangeA1 = 0
                                irangeA2 = 7
                                iE1 = 2
                                iE2 = 4
                                if regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[0][7] :
                                    pions[0][7] = regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[0][7] in pions[2] or pions[0][7] in pions[3] :
                                        Mange1 = pions[0][7]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                            
                            elif x == pions[0][2] :
                                i1 = 0
                                i2 = 2
                                iA1 = 1
                                iA2 = 0
                                irangeA1 = 0
                                irangeA2 = 2
                                iE1 = 2
                                iE2 = 4
                                if regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[0][2] :
                                    pions[0][2] = regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[0][2] in pions[2] or pions[0][2] in pions[3] :
                                        Mange1 = pions[0][2]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                            
                            elif x == pions[0][5] :
                                i1 = 0
                                i2 = 5
                                iA1 = 1
                                iA2 = 0
                                irangeA1 = 0
                                irangeA2 = 5
                                iE1 = 2
                                iE2 = 4
                                if regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[0][5] :
                                    pions[0][5] = regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[0][5] in pions[2] or pions[0][5] in pions[3] :
                                        Mange1 = pions[0][5]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[0][4] :
                                i1 = 0
                                i2 = 4
                                iA1 = 1
                                iA2 = 0
                                irangeA1 = 0
                                irangeA2 = 4
                                iE1 = 2
                                iE2 = 4
                                if regle_dame(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[0][4] :
                                    pions[0][4] = regle_dame(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[0][4] in pions[2] or pions[0][4] in pions[3] :
                                        Mange1 = pions[0][4]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[0][3] :
                                i1 = 0
                                i2 = 3
                                iA1 = 1
                                iA2 = 0
                                irangeA1 = 0
                                irangeA2 = 3
                                iE1 = 2
                                iE2 = 4
                                if regle_roi(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[0][3] :
                                    pions[0][3] = regle_roi(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[0][3] in pions[2] or pions[0][3] in pions[3] :
                                        Mange1 = pions[0][3]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[0][1] :
                                i1 = 0
                                i2 = 1
                                iA1 = 1
                                iA2 = 0
                                if regle_cavalier(pions,i1,i2,iA1,iA2) != pions[0][1] :
                                    pions[0][1] = regle_cavalier(pions,i1,i2,iA1,iA2)
                                    if pions[0][1] in pions[2] or pions[0][1] in pions[3] :
                                        Mange1 = pions[0][1]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[0][6] :
                                i1 = 0
                                i2 = 6
                                iA1 = 1
                                iA2 = 0
                                if regle_cavalier(pions,i1,i2,iA1,iA2) != pions[0][6] :
                                    pions[0][6] = regle_cavalier(pions,i1,i2,iA1,iA2)
                                    if pions[0][6] in pions[2] or pions[0][6] in pions[3] :
                                        Mange1 = pions[0][6]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                            
                                    
                elif pions[1][i] == x :
                    ev = attend_ev()
                    ty = type_ev(ev)
                    if ty == "ClicGauche" :
                        if milieu_case() in pions[1] or milieu_case() in pions[0] :
                            tour = tour
                        else :
                            if regle_pions(pions,i) == pions[1][i] :
                                tour = tour
                            else :
                                pions[1][i] = regle_pions(pions,i)
                                if pions[1][i] in pions[2] or pions[1][i] in pions[3] :
                                    Mange2 = pions[1][i]
                                    Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                tour += 1
            
            
            
            elif tour%2 == 0 :
                
                
                if pions[2][i] == x :
                    ev = attend_ev()
                    ty = type_ev(ev)
                    if ty == "ClicGauche" :
                        if milieu_case() in pions[2] or milieu_case() in pions[3] :
                            tour = tour
                        else :
                            if regle_pions(pions,i) == pions[2][i] :
                                tour = tour
                            else :
                                pions[2][i] = regle_pions(pions,i)
                                if pions[2][i] in pions[0] or pions[2][i] in pions[1] :
                                    Mange3 = pions[2][i]
                                    Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                tour += 1
                                
                
                elif pions[3][i] == x :
                    ev = attend_ev()
                    ty = type_ev(ev)
                    if ty == "ClicGauche" :
                        if milieu_case() in pions[3] or milieu_case() in pions[2] :
                            tour = tour
                            
                        else :
                            if x == pions[3][0] :
                                i1 = 3
                                i2 = 0
                                iA1 = 2
                                iA2 = 3
                                irangeA1 = 1
                                irangeA2 = 8
                                iE1 = 0
                                iE2 = 2
                                if regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[3][0] :
                                    pions[3][0] = regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[3][0] in pions[0] or pions[3][0] in pions[1] :
                                        Mange4 = pions[3][0]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[3][7] :
                                i1 = 3
                                i2 = 7
                                iA1 = 2
                                iA2 = 3
                                irangeA1 = 0
                                irangeA2 = 7
                                iE1 = 0
                                iE2 = 2
                                if regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[3][7] :
                                    pions[3][7] = regle_tour(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[3][7] in pions[0] or pions[3][7] in pions[1] :
                                        Mange4 = pions[3][7]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[3][2] :
                                i1 = 3
                                i2 = 2
                                iA1 = 2
                                iA2 = 3
                                irangeA1 = 0
                                irangeA2 = 2
                                iE1 = 0
                                iE2 = 2
                                if regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[3][2] :
                                    pions[3][2] = regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[3][2] in pions[0] or pions[3][2] in pions[1] :
                                        Mange4 = pions[3][2]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[3][5] :
                                i1 = 3
                                i2 = 5
                                iA1 = 2
                                iA2 = 3
                                irangeA1 = 0
                                irangeA2 = 5
                                iE1 = 0
                                iE2 = 2
                                if regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[3][5] :
                                    pions[3][5] = regle_fou(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[3][5] in pions[0] or pions[3][5] in pions[1] :
                                        Mange4 = pions[3][5]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[3][4] :
                                i1 = 3
                                i2 = 4
                                iA1 = 2
                                iA2 = 3
                                irangeA1 = 0
                                irangeA2 = 4
                                iE1 = 0
                                iE2 = 2
                                if regle_dame(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[3][4] :
                                    pions[3][4] = regle_dame(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[3][4] in pions[0] or pions[3][4] in pions[1] :
                                        Mange4 = pions[3][4]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                
                                
                            elif x == pions[3][3] :
                                i1 = 3
                                i2 = 3
                                iA1 = 2
                                iA2 = 3
                                irangeA1 = 0
                                irangeA2 = 3
                                iE1 = 0
                                iE2 = 2
                                if regle_roi(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2) != pions[3][3] :
                                    pions[3][3] = regle_roi(pions,i1,i2,iA1,iA2,irangeA1,irangeA2,iE1,iE2)
                                    if pions[3][3] in pions[0] or pions[3][3] in pions[1] :
                                        Mange4 = pions[3][3]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[3][1] :
                                i1 = 3
                                i2 = 1
                                iA1 = 2
                                iA2 = 3
                                if regle_cavalier(pions,i1,i2,iA1,iA2) != pions[3][1] :
                                    pions[3][1] = regle_cavalier(pions,i1,i2,iA1,iA2)
                                    if pions[3][1] in pions[0] or pions[3][1] in pions[1] :
                                        Mange4 = pions[3][1]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                                    
                            elif x == pions[3][6] :
                                i1 = 3
                                i2 = 6
                                iA1 = 2
                                iA2 = 3
                                if regle_cavalier(pions,i1,i2,iA1,iA2) != pions[3][6] :
                                    pions[3][6] = regle_cavalier(pions,i1,i2,iA1,iA2)
                                    if pions[3][6] in pions[0] or pions[3][6] in pions[1] :
                                        Mange4 = pions[3][6]
                                        Mange_pions(pions,Mange1,Mange2,Mange3,Mange4)
                                    tour += 1
                                else :
                                    tour = tour
                    
 
    efface_tout()
    
    
attend_fermeture()