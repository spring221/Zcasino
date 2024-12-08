#By TNS Software software engineer
#ULaval
 
import variable

def choix_du_nombre():


    while(variable.true_choix_nbre == False):

        try :

            variable.nbre_choisir = int(input("entrer un nombre\n"))

            variable.true_choix_nbre = True
        

        except:

            print("veillez entrer un entier \n")

        finally:
            print("bye")

    return variable.nbre_choisir 