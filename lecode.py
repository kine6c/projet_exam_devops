#creer un generateur de mot de passe
import random

print("------- Welcome to  Your Password Generator -------- ")
# 1- on demande a l'utilisateur le nombre de mot de passe qu'il souhaite generer

pattern= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^*&(),.?0123456789'

nbr_de_mdp= int(input("Saisissez le nombre de mot de passe que vous souhaitez generer : "))
print(nbr_de_mdp, "mot de passe")

length= int(input("Veuillez saisir la longueur du mot de passe :"))

for mot in range(nbr_de_mdp) :
    motdepasse=''
    for i in range(length)  :
        motdepasse +=random.choice(pattern)   
    print(f"VOICI VOS MOTS DE PASSE :{motdepasse}")
