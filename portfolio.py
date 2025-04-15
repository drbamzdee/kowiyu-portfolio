import streamlit as st
from PIL import Image

# Load image
image = Image.open("lab_photo.jpg.jpeg")

# Page config
st.set_page_config(page_title="Kowiyu Abidemi Bamidele", layout="wide")

# Title and image
st.image(image, caption="Kowiyu Abidemi Bamidele in the lab", use_column_width=True)
st.title("Digital Transformation Portfolio")

# Single scroll layout
with st.container():
    st.header("👨‍🔬 Professional Profile")
    st.write("""
    Adaptable, ambitious, and qualified individual seeking a prolonged and rewarding career within Water Resource Engineering. Maintains a meticulous and attentive approach to perform innovative research and evaluation. Proven in supporting large-scale projects, exceeding research objectives, and presenting intricate findings in understandable formats. Skilled in Python, QGIS, MIKE SHE, HEC-HMS, MODFLOW, WEAP, ArcGIS, SPI, and SPEI.
    """)

    st.header("💼 Competencies")
    st.write("""
    Project Management ▪ Strategic Planning ▪ Research & Evaluation ▪ Data Analysis ▪ Stakeholder Collaboration ▪ Reporting ▪ Critical Thinking ▪ Problem Solving ▪ Time Management ▪ Creativity
    """)

    st.header("🎓 Education")
    st.subheader("MSc Water Science and Engineering, IHE Delft (2021–2023)")
    st.markdown("- Thesis: *Characterizing Natural Hazards and their Drivers: Meteorological Drought in the Alazani River Basin, Georgia*")
    st.subheader("BSc Water Resources Management and Agro-Meteorology, FUNAAB (2014–2019)")
    st.markdown("- Project: *The Effect of Waste Dumping on the Quality of Surface Water in OFIKI Town*")

    st.header("🧑‍💼 Career Summary")
    st.subheader("Water Resources Engineer/Hydrologist – Favour Consult Ltd (2019–2023)")
    st.markdown("""
    - Managed complex project schedules
    - Analyzed large datasets and produced insight reports
    - Provided technical guidance and stakeholder communication
    """)
    st.subheader("Laboratory Instructor – The Peace College (2016–2019)")
    st.subheader("Industrial Training – Oyo State Water Corporation (2015–2017)")

    st.header("🏆 Awards & Qualifications")
    st.markdown("""
    - Bill Gates Scholarship (2022–2023)
    - Orange Knowledge Programme (2021–2022)
    - QGIS for Hydrological Applications Course (IHE Delft, 2021)
    """)

    st.header("🔬 Research Interests")
    st.markdown("""
    - Climate Change Studies
    - Disaster Response Planning
    - Clean Water Advocacy
    - Wastewater Solutions
    - Surface & Groundwater Dynamics
    - Pollution Impact Analysis
    """)

    st.header("🌐 Memberships")
    st.markdown("""
    - I-CISK, IAHS, IAENG, CIWEM, IAHR, YHS, HEPEX
    """)

    st.header("📄 Publications")
    st.markdown("""
    - *Characterizing Natural Hazards...* (Published)
    - *The Effect of Waste Dumping...* (Unpublished)
    """)

    st.header("🧑‍🏫 Leadership & Volunteering")
    st.markdown("""
    - Disciplinary Committee Chairman – The Peace College (2017–2019)
    - Senate President – FILGS (2015–2017)
    - Science & Math Tutor – FUNAAB, JAF Iseyin
    """)

    st.header("📬 References")
    st.markdown("""
    - Dr. Ilyas Mashi (IHE Delft)
    - Prof. O. A. Idowu (FUNAAB)
    - Micha Werner (IHE Delft)
    - Prof. G. C. Ufoegbune (FUNAAB)
    """)

    st.markdown("---")
    st.markdown("🌍 [Connect on LinkedIn](https://www.linkedin.com/in/kowiyu-abidemi-bamidele/)")
