# 🕵️ Inspector Image

## 🎯 Objectif

Ce projet a pour but de **détecter des informations cachées** dans une image au format `.jpeg` en utilisant deux techniques principales :

1. 📍 **Analyse des métadonnées GPS (EXIF)** : pour localiser où la photo a été prise.
2. 🕶️ **Stéganographie** : pour extraire une clé PGP cachée dans l’image.

Le projet est réalisé en **Python**, avec une interface en ligne de commande.

---

## 📦 Contenu du dépôt

- `main.py` : point d’entrée du programme.
- `map/handle_map.py` : traitement des métadonnées EXIF.
- `steg/handle_steg.py` : extraction de texte dissimulé via `strings`.
- `README.md` : ce fichier.

---

## ⚙️ Installation et dépendances

Assurez-vous d’avoir Python 3 installé, puis :

```bash
pip install exifread
````

---

## 🚀 Utilisation

### 📍 Extraire les coordonnées GPS

```bash
python main.py -map path/to/image.jpeg
```

**Exemple attendu :**

```
Lat/Lon: (32.0866) / (34.8851)
```

Cela correspond à une extraction des métadonnées EXIF de l’image.

---

### 🕶️ Extraire la clé PGP cachée

```bash
python main.py -steg path/to/image.jpeg
```

**Exemple attendu :**

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
...
-----END PGP PUBLIC KEY BLOCK-----
```

Le programme utilise la commande `strings` pour détecter la présence d'une clé publique PGP cachée dans les données binaires de l'image.

---

## 💡 Fonctionnement interne

### 🔍 `-map`

Le script lit les métadonnées EXIF à l’aide de la bibliothèque `exifread`, puis extrait la latitude et la longitude, qu’il convertit en format décimal.

### 🧬 `-steg`

Le script appelle la commande `strings` sur le fichier image, récupère toutes les chaînes imprimables, puis utilise une expression régulière pour détecter une clé PGP complète encodée dans l’image.

---

## ⭐ Bonus

* ❌ Autres méthodes de stéganographie → *non implémentées*
* ❌ Interface graphique (GUI) → *non implémentée*
* ❌ Comparaison d’images → *non implémentée*

---

## ⚠️ Avertissement

Ce projet est à but **éducatif uniquement**.
L’utilisation de ces techniques sur des fichiers, systèmes ou images sans autorisation est illégale.

## Script supplémentaire

Pour cacher un message sur une image tu peux:
```bash
steghide embed -cf cover.jpg -ef secret.txt -p mypassword
```
Et pour le decoder:

```bash
steghide extract -sf cover.jpg -p mypassword
```
