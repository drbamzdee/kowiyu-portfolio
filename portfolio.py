import streamlit as st
from PIL import Image
import os

# Page Configuration
st.set_page_config(page_title="Kowiyu Abidemi Bamidele", layout="wide")

# --- Custom Background and Styling ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Improve visibility for all links */
    a {
        color: white !important;
        text-decoration: none;
    }

    a:hover {
        color: #FFD700 !important;  /* Golden yellow on hover */
    }

    /* Make headings and paragraphs slightly brighter */
    h1, h2, h3, p {
        color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Load and Display Image ---
try:
    image = Image.open("lab_photo.jpg.jpeg")  # Ensure this file exists
    st.image(image, caption="Kowiyu Abidemi Bamidele in the lab", use_column_width=True)
except FileNotFoundError:
    st.warning("Profile image not found. Please make sure 'lab_photo.jpg.jpeg' is in the working directory.")

# --- Title ---
st.title("Digital Transformation Portfolio")

# --- Table of Contents ---
st.markdown("## 🧭 Table of Contents")
st.markdown("""
- [👨‍🔬 About Me](#about-me)
- [📄 Download CV](#download-my-cv)
- [📊 Project](#project-drought-pattern-analysis-in-the-alazani-river-basin)
- [🧠 Skills & Tools](#skills--tools)
- [🎯 Goals](#goals-for-joining-the-digital-transformation-programme)
- [📚 Education](#education)
- [🛠️ Career Summary](#career-summary)
- [🏅 Awards & Memberships](#awards--qualifications)
- [📚 Research Interests](#research-interests)
- [📢 Leadership Experience](#leadership-experience)
- [❤️ Voluntary/Community Services](#voluntarycommunity-services)
- [🔗 Contact](#footer)
""", unsafe_allow_html=True)

# --- About Me ---
st.header("👨‍🔬 About Me")
st.write("""
Adaptable, ambitious, and qualified individual seeking to pursue a prolonged and rewarding career within Water Resource Engineering. Maintains a meticulous and attentive approach to perform innovative research and evaluation.
""")

# --- Download CV ---
cv_path = r"C:\Users\IHE-Sale\OneDrive\Documents\southapton\CV_KOWIYU ABIDEMI BAMIDELE.pdf"

if os.path.exists(cv_path):
    with open(cv_path, "rb") as file:
        st.download_button(
            label="📄 Download My CV",
            data=file,
            file_name="Kowiyu_Abidemi_CV.pdf",
            mime="application/pdf"
        )
else:
    st.error("CV file not found. Please check the file path or move the file to your working directory.")

# --- Project Section ---
st.header("📊 Project: Drought Pattern Analysis in the Alazani River Basin")
st.write("""
Analyzed hydroclimatic drivers using ERA5 climate reanalysis data and Bayesian statistical modeling to support drought risk management strategies.
""")

# --- Skills & Tools ---
st.header("🧠 Skills & Tools")
st.markdown("""
- Python (Pandas, NumPy, Matplotlib)
- R, MATLAB
- GIS Tools (QGIS, ArcGIS)
- Remote Sensing
- MIKE SHE, HEC-HMS, MODFLOW, WEAP
- SPI, SPEI
""")

# --- Goals ---
st.header("🎯 Goals for Joining the Digital Transformation Programme")
st.write("""
To integrate digital transformation into environmental and water resource challenges, design human-centered solutions, and collaborate on real-world projects with diverse teams.
""")

# --- Education ---
st.header("📚 Education")

st.subheader("MSc Water Science and Engineering (Hydrology and Water Resources)")
st.write("IHE Delft, Netherlands (2021 – 2023)")
st.markdown("- **Thesis:** Characterizing Natural Hazards and their Drivers in the Alazani River Basin, Georgia")

st.subheader("BSc Water Resources Management and Agro-Meteorology (Hydrology)")
st.write("Federal University of Agriculture, Nigeria (2014 – 2019)")
st.markdown("- **Project:** Effect of Waste Dumping on Surface Water Quality in OFIKI town")

# --- Career Summary ---
st.header("🛠️ Career Summary")

st.subheader("Water Resources Engineer/Hydrologist – Favour Consult Limited (2019 – 2023)")
st.markdown("""
- Conducted research, data analysis, stakeholder communication, and report writing.
- Managed project deadlines and complex schedules effectively.
""")

st.subheader("Laboratory Instructor – The Peace College (2016 – 2019)")
st.markdown("""
- Delivered lab sessions and evaluated student performance.
- Acted as first contact for technical questions.
""")

st.subheader("Industrial Training – Oyo State Water Corporation (2015 – 2017)")
st.markdown("""
- Supported water treatment analysis, reporting, and departmental operations.
""")

# --- Awards & Memberships ---
st.header("🏅 Awards & Memberships")
st.markdown("""
- **Scholarships:** Bill Gate Scholarship (2022–2023), Orange Knowledge Program (2021–2022)
- **Memberships:** I-CISK, IAHS, IAENG, CIWEM, IAHR, YHS, HEPEX
""")

# --- Research Interests ---
st.header("📚 Research Interests")
st.markdown("""
- Climate Change Patterns and Impacts
- Disaster Response Planning (Droughts, Floods, Heatwaves)
- Clean Water Advocacy and Sanitation
- Innovative Wastewater Solutions
- Surface Water and Groundwater Dynamics
- Water Pollution and Waste Dumping Effects
""")

# --- Leadership Experience ---
st.header("📢 Leadership Experience")
st.markdown("""
- Disciplinary Committee Chairman – The Peace College (2017–2019)
- Senate President – FILGS (2015–2017)
- Senate Member – NAOOS (2017–2018)
- President – WREMSA (2016)
""")

# --- Voluntary / Community Services ---
st.header("❤️ Voluntary/Community Services")
st.markdown("""
- Science Teacher – FUNAAB INHURD (2012–2014)
- Mathematics Teacher – JAF Iseyin (2017)
- Tutorial Coordinator – MSSN FUNAAB (2016–2018)
""")

# --- Contact / Footer ---
st.markdown("---")
st.markdown("🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/kowiyu-abidemi-bamidele/)")
