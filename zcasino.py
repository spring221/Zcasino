#By TNS Software software engineer
#ULaval
 
import generate_random
import variable

nombre_roulet = generate_random.Generate()

while(variable.true_choix_nbre == False):

    try :

        variable.nbre_choisir = int(input("entrer un nombre\n"))

        variable.true_choix_nbre = True
      

    except:

        print("veillez entrer un entier \n")

    finally:
        print("bye")

        

