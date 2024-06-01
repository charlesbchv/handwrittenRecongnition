# Reconnaissance de Chiffres Manuscrits

Ce projet utilise des réseaux de neurones profonds pour reconnaître les chiffres manuscrits à partir d'images, en exploitant le célèbre jeu de données MNIST. Plusieurs modèles de réseaux de neurones, y compris des perceptrons à deux couches, MLP et des réseaux de neurones convolutifs (CNN), sont entraînés et évalués.

## Structure du Projet

Le projet est structuré comme suit :
- `Demonstration`: Contient des vidéos de démonstration de l'application.
- `Interface`: Contient le code de l'interface des prédictions en temps réel selon les modèles
- `Trained Models`: Contient les modèles pré-entraînés.
- `DL_handwriteDP.ipynb`: Jupyter Notebook avec des détails sur le processus de traitement de données et d'entraînement des modèles.
- `Etat_de_lart_Handwritten_Digit_Recognition.pdf`: Document décrivant l'état de l'art de la reconnaissance de chiffres manuscrits.

## Installation

Pour exécuter ce projet, vous aurez besoin de Python ou Google Colab et des packages suivants :

```bash
pip install tensorflow keras numpy matplotlib streamlit streamlit-drawable-canvas
