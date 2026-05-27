import streamlit as st
from PIL import Image
import os
from streamlit_pdf_viewer import pdf_viewer

# --- Function to display PDF ---
def show_pdf(file_path):
    pdf_viewer(file_path)

# 1. Configure the web page
st.set_page_config(layout="wide", page_title="Cartographie Portage à Domicile")
st.title("Cartographie des communes - Portage à domicile")

# 2. Define the regions and their respective files (PNG + PDF)
regions = {
    "Com.Com. Ambert": [
        "ambert1.png",
        "ambert2.png",
        "ambert.pdf"
    ],
    "AVT Thiers": [
        "thiers1.png",
        "thiers2.png",
        "thiers.pdf"
    ],
     "CCAS Clermont-Ferrand": [
        "Clermont-Ferrand1.png",
        "Clermont-Ferrand2.png",
        "Clermont-Ferrand.pdf"
    ],
    
    "CCAS Pont-du-Château": [
        "Pont-du-chateau1.png",
        "Pont-du-chateau2.png",
        "Pont-du-chateau.pdf"
    ],
    "Com.Com. Dômes Sancy Artense": [
        "ComCom-Dôme Sancy-Artense1.png",
        "Domes Sancy Artense.png",
        "ComCom-Dômes Sancy-Artense.pdf"
    ],
     " Cebazat-SISPA": [
        "Cebazat-SISPA1.png",
        "Cebazat-SISPA2.png",
        "Cebazat-SISPA.pdf"
    ],
    "CCAS Beaumont": [
        "Beaumont1.png",
        "beaumont2.png",
        "beaumont.pdf"
    ],
    "SIVOS de Billom": [
        "billom1.png",
        "billom2.png",
        "Billom.pdf"
    ],
    "Ceyrat Pôle Social et Proximité": [
        "ceyrat1.png",
        "ceyrat2.png",
        "Ceyrat.pdf"
    ],
    "Etap-Auvergne 43": [
        "etap-auvergne1.png",
        "etap-auvergne2.png",
        "etap-auvergne.pdf"
    ],
    "Mond'Arverne Communauté": [
        "mondarverne1.png",
        "mondarverne2.png",
        "mondarverne.pdf"
    ],
     "CCAS Aubiere": [
        "Aubiere1.png",
        "Aubiere2.png",
        "Aubiere.pdf"
    ],
    "SIVOM de la Vallée de l’Anse": [
        "SIVOM de la Vallée de l’Anse1.png",
        "SIVOM de la Vallée de l’Anse.png",
        "SIVOM de la Vallée de l’Anse.pdf"
    ],
     "Com.Com. Chavanon Combrailles et Volcans Pontaumur": [
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur1.png",
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur.png",
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur.pdf"
    ],
}

# 3. Create a split layout
col1, col2 = st.columns([1, 1])

# LEFT COLUMN
with col1:
    st.subheader("Carte des territoires")
    
    main_map_path = "carte1.png"
    
    if os.path.exists(main_map_path):
        st.image(main_map_path, use_container_width=True)
    else:
        st.warning(f"⚠️ Image introuvable : '{main_map_path}'")

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
