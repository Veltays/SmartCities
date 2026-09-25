# Exercice 1 — Contrôle d'une LED avec un bouton

## Objectif

Cet exercice consiste à réaliser un montage électronique autour d'un **Raspberry Pi Pico 2 W**, d'un bouton et d'une LED.

La LED clignote en continu. Chaque fois qu'un appui sur le bouton est détecté, le niveau augmente, ce qui réduit le délai entre deux changements d'état. Après le dixième niveau, le programme revient au premier.

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
| Bouton | GPIO 16 | Entrée |

Les broches utilisées sont déclarées dans `constantes/pin.py` afin de centraliser la configuration matérielle.

## Organisation du code

![Schéma de l'architecture du programme](../../documentation/SCHEMA/exercice1_schema_developement.png)

Le programme est séparé en plusieurs parties :

- `drivers/` contient les classes qui pilotent les composants matériels :
  - `button.py` lit l'état du bouton ;
  - `led.py` contrôle l'état de la LED.
- `services/` contient la logique utilitaire :
  - `timer.py` gère les temporisations utilisées par l'application.
- `constantes/` centralise les paramètres du programme :
  - `pin.py` configure les GPIO de la LED et du bouton ;
  - `time.py` définit le délai de base ;
  - `config.py` définit le nombre de niveaux.
- `main.py` est le point d'entrée de l'application.

```text
Exercice1/
├── constantes/
│   ├── config.py
│   ├── pin.py
│   └── time.py
├── drivers/
│   ├── button.py
│   └── led.py
├── services/
│   └── timer.py
└── main.py
```

## Fonctionnement du programme

Le fichier `main.py` contient deux fonctions principales :

1. `setup()` initialise le timer, la LED et le bouton, puis injecte les dépendances nécessaires aux différents composants.
2. `loop()` exécute la boucle principale : elle détecte les appuis sur le bouton, met à jour le niveau, inverse l'état de la LED et adapte le délai de clignotement.

Le délai est calculé de la manière suivante :

```python
delay = SLEEP_TIME / LevelNumber
```

Plus le niveau est élevé, plus le délai est court et plus la LED clignote rapidement.

## Respect des consignes

Par défaut la led à un SLEEP_TIME de 0.5hz:

Soit 1/0.5Hz = 2 secondes

