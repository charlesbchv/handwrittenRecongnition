import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas

# Ajout un fond d'écran avec l'URL de l'image hébergée
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("background.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Charge les modèles
modeles = {
    "Perceptron Simple": load_model('modele_1couche.h5'),
    "Perceptron 2 couches": load_model('modele_2couches.h5'),
    "MLP": load_model('modele_3couches.h5'),
    "CNN": load_model('cnn_model_prediction.h5')
}

# Sélection de modèle
choix_modele = st.sidebar.selectbox("Choisissez un modèle", list(modeles.keys()))
modele = modeles[choix_modele]

# Titre avec modèle sélectionné
st.title(f"Reconnaissance de chiffres manuscrits avec {choix_modele}")

#Partie digits
st.markdown("## Dessinez un chiffre ci-dessous")
canvas_result = st_canvas(
    stroke_width=10,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

if canvas_result.image_data is not None:
    # Traite l'image dessinée
    image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
    image = image.convert('L')
    image = ImageOps.invert(image)
    image = image.resize((28, 28))
    image = np.array(image).astype('float32') / 255.0

    # Vérifie si le modèle est un CNN ou non pour adapter les dimensions
    if choix_modele == "CNN":
        image = np.expand_dims(image, axis=(0, -1))
    else:
        image = np.expand_dims(image, axis=0)

    # Prédit le chiffre
    if st.button('Prédire'):
        prediction = modele.predict(image)
        st.write(f"Chiffre prédit : {np.argmax(prediction)}")
