"sqt qui permet de donner la racine carre"
from math import sqrt

#### Fonction secondaire


def isprime(p):
    "vérifie si un entier est un nombre premier ou pas."
    if p <= 1 :
        return False
    for i in range (2,int(sqrt(p)+1) ):
        if p % i == 0 :
            return False
    return True

    # votre code ici


#### Fonction principale


def main():
    "fait quelques appels à la fonction secondaire"
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
