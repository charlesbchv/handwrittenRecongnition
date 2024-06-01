# Reconnaissance de Chiffres Manuscrits

<p align="center"><a href="https:/laravel.com" target="_blanc"><img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*cQePQw-v3lC7QpZq9LdbKg.png" width="600"></a></p>
<p align="center"> 
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/charlesbchv/handwrittenRecongnition">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/charlesbchv/handwrittenRecongnition">
<img alt="GitHub watchers" src="https://img.shields.io/github/watchers/charlesbchv/handwrittenRecongnition">
<img alt="Bower" src="https://img.shields.io/bower/l/space">
</p>


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
