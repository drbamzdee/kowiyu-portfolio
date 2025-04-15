import streamlit as st
from PIL import Image

# Load your image
image = Image.open("lab_photo.jpg.jpeg")

# Page config
st.set_page_config(page_title="Kowiyu Abidemi Bamidele", layout="wide")

# Title and image
st.image(image, caption="Kowiyu Abidemi Bamidele in the lab", use_column_width=True)
st.title("Digital Transformation Portfolio")

# About Me
st.header("👨‍🔬 About Me")
st.write("""
Hydrologist and Climate Scientist passionate about applying digital tools in managing water-related disasters, 
droughts, and promoting sustainability in developing countries.
""")

# Project
st.header("📊 Project: Drought Pattern Analysis in the Alazani River Basin")
st.write("""
Analyzed hydroclimatic drivers using ERA5 climate reanalysis data and Bayesian statistical modeling 
to support drought risk management strategies.
""")

# Skills
st.header("🧠 Skills & Tools")
st.markdown("""
- Python (Pandas, NumPy, Matplotlib)
- R, MATLAB
- GIS Tools (QGIS, ArcGIS)
- Remote Sensing
- Machine Learning
""")

# Goals
st.header("🎯 Goals for Joining the Digital Transformation Programme")
st.write("""
To integrate digital transformation into environmental and water resource challenges, 
design human-centered solutions, and collaborate on real-world projects with diverse teams.
""")

# Footer
st.markdown("---")
st.markdown("🌍 Connect with me on [LinkedIn](https://www.linkedin.com/in/kowiyu-abidemi-bamidele/)")
