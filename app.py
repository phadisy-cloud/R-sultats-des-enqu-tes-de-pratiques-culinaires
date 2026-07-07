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
}

# ==============================================================================
# LINE 1: Main Map (Left) and Region Selection (Right)
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

# ==============================================================================
# LINE 2: Geographical Region Map (Left) and Infographics/PDF + Améliorer (Right)
# ==============================================================================
col_geo, col_info = st.columns([1, 1])
file_paths = regions[selected_region]

# Filter valid, existing files for processing
valid_files = [f for f in file_paths if os.path.exists(f)]
png_files = [f for f in valid_files if f.lower().endswith(".png")]
pdf_files = [f for f in valid_files if f.lower().endswith(".pdf")]

# Left column of Line 2: The Map of the specific region (1st PNG)
with col_geo:
    st.subheader(f"Carte géographique : {selected_region}")
    if png_files:
        region_map = Image.open(png_files[0])
        st.image(region_map, use_container_width=True, caption=f"Plan de {selected_region}")
    else:
        st.warning("⚠️ Aucune carte disponible pour cette région.")

# Right column of Line 2: Infographic (2nd PNG) AND/OR PDF viewer + ameliorer.png next to it
with col_info:
    st.subheader("Infographies & Documents")
    
    # If there's a second PNG, use it as the infographic
    if len(png_files) > 1:
        infographic = Image.open(png_files[1])
        st.image(infographic, use_container_width=True, caption="Données infographiques")
    
    # Render PDF viewer
    if pdf_files:
        st.markdown("**Document PDF associé :**")
        show_pdf(pdf_files[0])
    elif len(png_files) <= 1 and not pdf_files:
        st.info("Aucune infographie additionnelle ou PDF disponible.")
    
    # NEW LOCATION: ameliorer.png renders right under/next to the PDF inside this column context
    st.markdown("---")
    st.markdown("#### Informations Générales / Améliorations")
    always_visible_map = "ameliorer.png" 
    if os.path.exists(always_visible_map):
        st.image(always_visible_map, use_container_width=True)
    else:
        st.warning(f"⚠️ Image permanente introuvable : '{always_visible_map}'")

st.markdown("---") # Visual separator

# ==============================================================================
# LINE 3: Verbatim Text Block (Spanning across the bottom cleanly)
# ==============================================================================
st.subheader("💬 Verbatim / Remarques")
st.info(
    """
    Insérez votre texte verbatim ici. Ce bloc reste visible en permanence tout en bas de la page.
    """
)
