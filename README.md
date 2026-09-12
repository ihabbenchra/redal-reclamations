# Redal - Application de gestion des réclamations des employés

Projet de stage 3ème année. Application web qui remplace les réclamations par
e-mail par une plateforme simple : les employés déposent leurs réclamations
(avec option anonymat) et suivent leur état, les techniciens les traitent et
changent leur statut.

## Stack technique

- Back-End : Django (Python)
- Front-End : Bootstrap
- Base de données : MySQL

## Installation rapide (VS Code)

1. Ouvrir le dossier du projet dans VS Code.
2. Ouvrir un terminal (Ctrl + ù ou Terminal > Nouveau terminal).
3. Créer et activer l'environnement virtuel :

```
python3 -m venv venv
venv\Scripts\activate      (Windows)
source venv/bin/activate   (Mac/Linux)
```

4. Installer les dépendances :

```
pip install -r requirements.txt
```

5. Créer la base de données MySQL (MySQL doit être installé et démarré) :

```
mysql -u root -e "CREATE DATABASE redal_db CHARACTER SET utf8mb4;"
```

6. Appliquer les migrations :

```
python manage.py migrate
```

7. Lancer le serveur :

```
python manage.py runserver
```

8. Ouvrir http://127.0.0.1:8000 dans le navigateur.

## Lancer directement depuis VS Code (sans terminal)

1. Aller dans l'onglet "Run and Debug" (icône lecture + bug, à gauche).
2. Choisir "Django - Lancer le serveur" dans le menu déroulant en haut.
3. Cliquer sur le bouton vert ▶️.
4. Ouvrir http://127.0.0.1:8000 dans le navigateur.

## Comptes

- S'inscrire en choisissant le rôle "Employé" pour déposer et suivre des réclamations.
- S'inscrire en choisissant le rôle "Technicien" pour traiter les réclamations.

## Configuration base de données (optionnel)

Par défaut : root sans mot de passe, localhost, port 3306. Pour changer :

```
export DB_NAME=redal_db
export DB_USER=root
export DB_PASSWORD=motdepasse
export DB_HOST=127.0.0.1
export DB_PORT=3306
```

## Structure du projet

- `accounts/` : comptes utilisateurs, inscription, connexion.
- `reclamations/` : dépôt, consultation, traitement des réclamations.
- `templates/` : pages HTML Bootstrap.
- `redal_project/` : configuration Django.
- `.vscode/` : configuration VS Code (lancement rapide du serveur).
