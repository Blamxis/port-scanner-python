# 🔍 HACKTOOL 1.0 — Port Scanner Python

HACKTOOL 1.0 est un scanner de ports rapide, lisible et personnalisable développé en Python.  
Il permet d’identifier les ports ouverts d’une machine, d’afficher les services associés et de visualiser la progression du scan en temps réel.

Ce projet a été réalisé dans le cadre de ma préparation au BUT Informatique, afin de comprendre le fonctionnement des ports TCP, des services réseau et des connexions bas niveau.

---

## 🎬 Vidéo de démonstration

👉 [Cliquez ici pour voir la vidéo](https://github.com/Blamxis/port-scanner-python/releases/download/v1.0/demo.mp4)


---

## ✨ Fonctionnalités

- 🎨 **Logo ASCII personnalisé** (HACKTOOL 1.0)
- 🧭 **Menu interactif complet**
  - Scan rapide (1 → 1024)
  - Scan moyen (1 → 20 000)
  - Scan complet (1 → 65 535)
  - Scan personnalisé (range)
  - Scan d’un seul port
- ⚡ **Scan multi‑thread** pour de hautes performances
- 🎯 **Détection automatique des services TCP**
- 📚 **Dictionnaire de services personnalisés** (MySQL, PostgreSQL, Ollama, Windows services…)
- 🟢 **Affichage coloré des ports ouverts**
- 📊 **Compteur final du nombre de ports ouverts**
- 🔄 **Progression dynamique du scan**
- 🛡️ Compatible Windows / PowerShell

---

## 📌 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-repo/PORT-SCANNER-PYTHON.git
cd PORT-SCANNER-PYTHON
```

### 2. Installer les dépendances

```bash
pip install colorama
```

### 3. Lancer le scanner

```bash
python scanner.py
```

---

## 📌 Exemple d'utilisation

Au lancement, le programme affiche :

- Le logo ASCII
- Le menu interactif
- La demande d'adresse IP
- Le scan en temps réel
- Les ports ouvert détectés
- Un résumé final avec le nombre total de ports ouverts

### Exemple

```bash
python scanner.py
```
---

## 🧠 Comment fonctionne le scanner ?

Le programme utilise :

- **socket** → pour tester les connexions TCP  
- **threading** → pour accélérer le scan  
- **colorama** → pour afficher des couleurs dans le terminal  
- **un dictionnaire interne** → pour reconnaître certains services non standards  

---

## 🔍 Principe du scan

1. Le programme tente d’établir une connexion TCP sur chaque port du range choisi.  
2. Si la connexion réussit → le port est considéré comme **ouvert**.  
3. Le service associé est identifié automatiquement (IANA + dictionnaire personnalisé).  
4. Le résultat est affiché en **vert** pour une meilleure lisibilité.  
5. Une **barre de progression** indique l’avancement du scan en temps réel.  
6. Un **compteur final** affiche le nombre total de ports ouverts détectés.  

---

## 📂 Structure du projet

```bash
📁 PORT-SCANNER-PYTHON
 ├── scanner.py        # Script principal
 ├── demo.gif          # Vidéo de démonstration (optionnelle)
 └── README.md         # Documentation
```

---

## 🛠️ Technologies utilisées

- **Python 3**
- **socket**
- **threading**
- **colorama**

---

## 🚀 Améliorations possibles

- Scan **UDP**
- Scan **multi‑IP** (réseau complet)
- **Export** des résultats dans un fichier
- **Détection d’OS** (fingerprinting)
- Mode **silencieux / verbose**
- Interface graphique (**Tkinter / PyQt**)

---

## 📜 Licence

Projet libre d’utilisation dans un cadre éducatif.

---

## 👤 Auteur

**Maxime Gavinet**  
Étudiant en préparation pour le BUT Informatique
