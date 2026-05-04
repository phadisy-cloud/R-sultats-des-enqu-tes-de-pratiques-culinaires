import streamlit as st
from PIL import Image
import os
import base64

# --- Function to display PDF ---
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" height="800px" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

# 1. Configure the web page
st.set_page_config(layout="wide", page_title="Cartographie Portage à Domicile")
st.title("Cartographie des communes - Portage à domicile")

# 2. Define the regions and their respective files (PNG + PDF)
regions = {
    "Ambert": [
        "ambert1.png",
        "ambert2.png",
        "ambert.pdf"
    ],
    "AVT Thiers": [
        "thiers1.png",
        "thiers2.png",
        "thiers.pdf"
    ],
     "Clermont-Ferrand": [
        "Clermont-Ferrand1.png",
        "Clermont-Ferrand2.png",
        "Clermont-Ferrand.pdf"
    ],
    
    "CCAS Pont-du-Château": [
        "Pont-du-Chateau1.png",
        "Pont-du-Chateau2.png",
        "Pont-du-Chateau.pdf"
    ],
    "Montagne-dôme-sancy": [
        "Montagne-Dome-Sancy1.png",
        "Montagne-Dome-Sancy2.png",
        "Montagne-dôme-sancy.pdf"
    ],
    "Beaumont": [
        "beaumont1.png",
        "beaumont2.png",
        "beaumont.pdf"
    ],
    "Billom": [
        "billom1.png",
        "billom2.png",
        "billom.pdf"
    ],
    "Ceyrat": [
        "ceyrat1.png",
        "ceyrat2.png",
        "ceyrat.pdf"
    ],
    "Etap-Auvergne": [
        "etap-auvergne1.png",
        "etap-auvergne2.png",
        "etap-auvergne.pdf"
    ],
    "Mond'Arverne": [
        "mondarverne1.png",
        "mondarverne2.png",
        "mondarverne.pdf"
    ]
}

# 3. Create a split layout
col1, col2 = st.columns([1, 1])

# LEFT COLUMN
with col1:
    st.subheader("Carte des territoires")
    
    main_map_path = "carte1.png"  # ⚠️ keep filename simple
    
    if os.path.exists(main_map_path):
        st.image(main_map_path, use_container_width=True)
    else:
        st.warning(f"⚠️ Image de la carte introuvable : '{main_map_path}'")

    st.markdown("### 🔍 Sélectionnez une région :")
    selected_region = st.selectbox(
        "Choisissez une région :", 
        list(regions.keys())
    )

# RIGHT COLUMN
with col2:
    st.subheader(f"Infographies : {selected_region}")
    
    file_paths = regions[selected_region]

    for file_path in file_paths:
        if os.path.exists(file_path):

            # PNG display
            if file_path.lower().endswith(".png"):
                img = Image.open(file_path)
                st.image(img, use_container_width=True)

            # PDF display
            elif file_path.lower().endswith(".pdf"):
                show_pdf(file_path)

            else:
                st.warning(f"Format non supporté : {file_path}")

        else:
            st.error(f"⚠️ Fichier introuvable : '{file_path}'")