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
        "ambert.pdf",
    ],
    "AVT Thiers": [
        "thiers1.png",
        "thiers2.png",
        "thiers.pdf",
    ],
     "CCAS Clermont-Ferrand": [
        "Clermont-Ferrand1.png",
        "Clermont-Ferrand2.png",
        "Clermont-Ferrand.pdf",
    ],
    "CCAS Pont-du-Château": [
        "Pont-du-chateau1.png",
        "Pont-du-chateau2.png",
        "Pont-du-chateau.pdf",
    ],
    "Com.Com. Dômes Sancy Artense": [
        "ComCom-Dôme Sancy-Artense1.png",
        "Domes Sancy Artense.png",
        "ComCom-Dômes Sancy-Artense.pdf",
    ],
     " Cebazat-SISPA": [
        "Cebazat-SISPA1.png",
        "Cebazat-SISPA2.png",
        "Cebazat-SISPA.pdf",
    ],
    "CCAS Beaumont": [
        "Beaumont1.png",
        "beaumont2.png",
        "beaumont.pdf",
    ],
    "CIAS Riom Limagne et Volcans": [
        "CiAS Riom Limagne et Volcans1.png",
        "CIAS Riom Limagne et Volcans.png",
        "CIAS Riom Limagne et Volcans.pdf",
    ],
    "SIVOS de Billom": [
        "billom1.png",
        "billom2.png",
        "Billom.pdf",
    ],
    "Ceyrat Pôle Social et Proximité": [
        "ceyrat1.png",
        "ceyrat2.png",
        "Ceyrat.pdf",
    ],
    "Etap-Auvergne 43": [
        "etap-auvergne1.png",
        "etap-auvergne2.png",
        "etap-auvergne.pdf",
    ],
    "Mond'Arverne Communauté": [
        "mondarverne1.png",
        "mondarverne2.png",
        "mondarverne.pdf",
    ],
     "CCAS Aubiere": [
        "Aubiere1.png",
        "Aubiere2.png",
        "Aubiere.pdf",
    ],
    "SIVOM de la Vallée de l’Anse": [
        "SIVOM de la Vallée de l’Anse1.png",
        "SIVOM de la Vallée de l’Anse.png",
        "SIVOM de la Vallée de l’Anse.pdf",
    ],
     "Com.Com. Chavanon Combrailles et Volcans": [
        "Com.Com. Chavanon Combrailles et Volcans1.png",
        "Com.Com. Chavanon Combrailles et Volcans.png",
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur.pdf",
    ],
     "Com.Com. Massif du Sancy": [
        "Com.Com. Massif du Sancy1.png",
        "Com.Com. Massif du Sancy.png",
        "Com.Com. Massif du Sancy.pdf",
    ],
     "EURL Etang de Montmazot": [
        "EURL Etang de Montmazot1.png",
        "EURL Etang de Montmazot.png",
        "EURL Etang de Montmazot.pdf",
    ],
}

# ==============================================================================
# ROW 1: Main Map (Left) and Region Selection (Right)
# ==============================================================================
col_map, col_select = st.columns([1, 1])

with col_map:
    st.subheader("Carte des territoires")
    main_map_path = "carte1.png"
    if os.path.exists(main_map_path):
        st.image(main_map_path, use_container_width=True)
    else:
        st.warning(f"⚠️ Image introuvable : '{main_map_path}'")

with col_select:
    st.markdown("### 🔍 Sélectionnez une région :")
    selected_region = st.selectbox(
        "Choisissez une région dans la liste ci-dessous :", 
        list(regions.keys())
    )
    st.write(f"Région active : **{selected_region}**")

st.markdown("---") # Visual separator

# Extract valid files for processing
file_paths = regions[selected_region]
valid_files = [f for f in file_paths if os.path.exists(f)]
png_files = [f for f in valid_files if f.lower().endswith(".png")]
pdf_files = [f for f in valid_files if f.lower().endswith(".pdf")]

# ==============================================================================
# ROW 2: Geographical Region Map (Left) & Infographic PNG (Right)
# ==============================================================================
col_geo, col_info = st.columns([1, 1])

# Left Side: The primary geographical regional map
with col_geo:
    st.subheader(f"Carte géographique : {selected_region}")
    if png_files:
        region_map = Image.open(png_files[0])
        st.image(region_map, use_container_width=True)
    else:
        st.warning("⚠️ Aucune carte disponible pour cette région.")

# Right Side: The infographic layout (the 2nd regional PNG file)
with col_info:
    st.subheader("Données Infographiques")
    if len(png_files) > 1:
        infographic = Image.open(png_files[1])
        st.image(infographic, use_container_width=True)
    else:
        st.info("ℹ️ Pas d'infographie additionnelle au format image pour cette région.")

st.markdown("---") # Visual separator

# ==============================================================================
# ROW 3: Améliorer PNG (Left) and Verbatim/PDF Document Container (Right)
# ==============================================================================
col_ameliorer, col_pdf_verbatim = st.columns([1, 1])

# Left Side: Persistent Améliorer Image without the old extra titles
with col_ameliorer:
    always_visible_map = "ameliorer.png" 
    if os.path.exists(always_visible_map):
        st.image(always_visible_map, use_container_width=True)
    else:
        st.warning(f"⚠️ Image permanente introuvable : '{always_visible_map}'")

# Right Side: PDF displaying directly inside the Verbatim block framework
with col_pdf_verbatim:
    st.subheader("💬 Verbatim / Documents")
    if pdf_files:
        with st.container(border=True): # Gives it a clean frame matching your image look
            show_pdf(pdf_files[0])
    else:
        st.info("ℹ️ Aucun document PDF associé disponible pour cette région.")
