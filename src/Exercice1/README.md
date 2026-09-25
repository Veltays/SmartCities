# Exercice 1 — Clignotement d'une LED avec un bouton-poussoir

## Objectif

Ce projet MicroPython utilise un **Raspberry Pi Pico 2 W**, une LED et un
bouton-poussoir. Chaque appui sur le bouton change le niveau de fonctionnement
de la LED : sa vitesse de clignotement évolue, elle peut s'éteindre ou exécuter
un effet lumineux.

Le programme comporte cinq niveaux. Une fois le dernier niveau atteint, un
nouvel appui ramène au premier niveau.

## Matériel utilisé

### Raspberry Pi Pico 2 W

![Raspberry Pi Pico 2 W](../../documentation/GPIO/raspberry_pico.png)

### Module LED Grove — Socket V1.7

![Module LED Grove](../../documentation/GPIO/module_led.png)

### Module bouton Grove V1.3

![Module bouton Grove](../../documentation/GPIO/module_bouton.png)

## Branchement

| Composant | Broche du Pico | Mode |
|---|---:|---|
| LED | GPIO 18 | Sortie |
| Bouton-poussoir | GPIO 16 | Entrée |

Les broches sont configurées dans `constantes/pin.py`. Il suffit de modifier ce
fichier pour adapter le programme à un autre branchement.

## Organisation du code

![Schéma de l'architecture du programme](../../documentation/SCHEMA/exercice1_schema_developement.png)

```text
Exercice1/
├── constantes/
│   ├── config.py       # nombre de niveaux
│   ├── pin.py          # configuration des GPIO
│   └── time.py         # délai de base
├── drivers/
│   ├── button.py       # lecture du bouton
│   └── led.py          # contrôle de la LED
├── services/
│   ├── led_effect.py   # effet lumineux bonus
│   └── timer.py        # temporisations et écoute du bouton
├── main.py             # point d'entrée du programme
└── README.md
```

Cette séparation permet de ne pas mélanger la configuration matérielle, le
pilotage des composants et la logique de l'application.

## Fonctionnement

Le fichier `main.py` est organisé autour de deux fonctions :

1. `setup()` crée le timer, la LED et le bouton, puis injecte les dépendances
   nécessaires aux composants ;
2. `loop()` exécute la boucle principale, détecte les appuis et sélectionne le
   comportement correspondant au niveau courant.

Le niveau suivant est calculé avec un modulo :

```python
LevelNumber = LevelNumber % NUMBER_OF_LEVELS + 1
```

La valeur `NUMBER_OF_LEVELS`, définie dans `constantes/config.py`, permet de
modifier le nombre total de niveaux sans inscrire directement cette valeur dans
la logique principale.

### Comportement des niveaux

| Niveau | Comportement |
|---:|---|  
| 1 | Clignotement lent |
| 2 | Clignotement plus rapide |
| 3 | LED éteinte |
| 4 | Clignotement encore plus rapide |
| 5 | Effet `TicTicBoom`, avec accélération progressive |

Pour les niveaux classiques, le délai entre deux changements d'état est :

```python
delay = SLEEP_TIME / LevelNumber
```

Un niveau plus élevé réduit donc le délai et accélère le clignotement.

### Fréquence de clignotement

Une période complète comprend deux changements d'état : allumage puis
extinction. Pour obtenir une fréquence de **0,5 Hz**, une période complète doit
durer deux secondes. La LED doit donc changer d'état toutes les secondes.

La relation utilisée est :

```text
fréquence = 1 / période
```

ce qui nous donne donc un premier délais de 2 secondes


## Effet bonus : `TicTicBoom`

Le niveau 5 lance l'effet défini dans `services/led_effect.py`. Le délai entre
les changements d'état diminue progressivement, ce qui donne l'impression que
la LED accélère.

L'effet utilise également `sleep_listening()`. Un appui sur le bouton peut donc
l'interrompre sans attendre la fin complète de l'animation.


# Problème rencontrer 

Sleep était bloquant, le code ne pouvait donc pas voir si une actualisations des boutons avait été fait, n'ayant pas vu les interuptions sytème sur une GPIO j'ai du trouver une solutions

## Attente avec écoute du bouton

La méthode `sleep_listening()` de `services/timer.py` remplace une attente
totalement bloquante. Pendant le délai, elle vérifie continuellement l'état du
bouton :

- elle retourne `True` lorsque le délai se termine normalement ;
- elle retourne `False` lorsqu'un appui est détecté avant la fin du délai ;
- une courte pause de 100 ms limite les détections multiples provoquées par les
  rebonds mécaniques du bouton.

Cette méthode rend le changement de niveau plus réactif, y compris pendant un
clignotement lent.