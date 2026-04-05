######################################
GUIDE D'UTILISATION VSCode : LiveShare
######################################

J'ai créer un espace de travail collaboratif sur VSCode avec LiveShare (une extension de VSCode que vous devrez
installer si vous voulez pouvoir travailler sur le projet)

J'ai demandé à Claude de faire un guide pour faire une mise en route. Les commandes peuvet un peu changer si vous êtes sur Mac mais en vrai si ça marche psa demander 
à un IA de vous expliquer elle font ça très bien.

------------------------------------------------------------
ETAPE 1 - PRE-REQUIS
------------------------------------------------------------

Avant de commencer, assure-toi d'avoir installé :

  - Python 3.x        --> https://www.python.org/downloads/
  - VS Code           --> https://code.visualstudio.com/
  - Extension Live Share (Microsoft) dans VS Code
  - Extension Python (Microsoft) dans VS Code
  - Extension Jupyter (Microsoft) dans VS Code

------------------------------------------------------------
ETAPE 2 - RECUPERER LE PROJET
------------------------------------------------------------

Récupère le dossier du projet partagé via Live Share ou
par tout autre moyen convenu avec le groupe.

Place le dossier à un endroit accessible sur ta machine,
par exemple :
  C:\Users\TonNom\Documents\Projet\

------------------------------------------------------------
ETAPE 3 - OUVRIR LE PROJET DANS VS CODE
------------------------------------------------------------

  1. Ouvre VS Code
  2. File > Open Folder
  3. Sélectionne le dossier racine du projet

------------------------------------------------------------
ETAPE 4 - CREER TON ENVIRONNEMENT VIRTUEL
------------------------------------------------------------

Ouvre un terminal dans VS Code (Ctrl + ù) et vérifie
que tu es bien à la racine du projet :

  cd chemin/vers/le/projet

Crée l'environnement virtuel (une seule fois) :

  python -m venv .venv

Active l'environnement :

  Windows  -->  .venv\Scripts\activate
  Mac/Linux --> source .venv/bin/activate

Tu dois voir (.venv) apparaître dans ton terminal.

/!\ IMPORTANT : n'appelle pas ton environnement autrement
que ".venv" pour que tout le groupe soit aligné.

------------------------------------------------------------
ETAPE 5 - INSTALLER LES DEPENDANCES (IMPORTANT)
------------------------------------------------------------

Une fois l'environnement activé, installe les librairies :

  pip install -r requirements.txt

Pour vérifier que l'installation s'est bien passée :

  pip list

------------------------------------------------------------
ETAPE 6 - SELECTIONNER L'INTERPRETEUR PYTHON
------------------------------------------------------------

  1. Ctrl + Shift + P
  2. Tape : "Python: Select Interpreter"
  3. Choisis ".venv" dans la liste

------------------------------------------------------------
ETAPE 7 - SELECTIONNER LE KERNEL DU NOTEBOOK
------------------------------------------------------------

  1. Ouvre le fichier NOM1_NOM2.ipynb
  2. Clique sur le bouton en haut à droite (version Python)
  3. Sélectionne "Python Environments" puis ".venv"

------------------------------------------------------------
ETAPE 8 - REJOINDRE LA SESSION LIVE SHARE
------------------------------------------------------------

  1. Clique sur l'icône Live Share dans la barre de gauche
  2. Clique sur "Join Collaboration Session"
  3. Colle le lien partagé par l'hôte
  4. Connecte-toi avec ton compte GitHub ou Microsoft

------------------------------------------------------------
STRUCTURE DU PROJET (pour rappel)
------------------------------------------------------------

  Projet/
  |
  |-- Assets/               (ou mettra dans ce dossier toutes les données statiques récupérée ou crées)
  |   |-- Data/
  |   |-- Graphs/
  |   |-- Tables/
  |
  |-- Classes/
  |   |-- portfolio.py       (class Portfolio)
  |
  |-- Returns/               
  |   |-- __init__.py
  |   |-- Utils.py           (fonctions personnalisées)
  |
  |-- config.py              (constantes globales)
  |-- requirements.txt       (librairies nécessaires)
  |-- LAVANDIER_LINON_JOLIBOIS.ipynb        (notebook principal)
  |-- README.txt             (ce fichier)

------------------------------------------------------------
EN CAS DE PROBLEME
------------------------------------------------------------

  - ".venv" n'apparait pas comme interpreter
    --> Refais l'étape 4 et redémarre VS Code

  - "pip install" échoue
    --> Vérifie que (.venv) est bien affiché dans le terminal

  - Le kernel ne trouve pas les librairies
    --> Vérifie que le kernel pointe bien sur ".venv" (étape 7)

  - Tu vois un dossier ".venv_autrennom" dans le projet
    --> Supprime-le : rmdir /s /q .venv_autrennom (Windows)
                      rm -rf .venv_autrennom (Mac/Linux)

============================================================