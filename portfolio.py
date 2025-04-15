{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "aa8a9ecf-a06c-4a13-8a12-072303b0a760",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-15 12:44:18.090 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\IHE-Sale\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from PIL import Image\n",
    "\n",
    "# Load image\n",
    "image = Image.open(\"lab_photo.jpg.jpeg\")\n",
    "\n",
    "# Title and Image\n",
    "st.title(\"Kowiyu Abidemi Bamidele\")\n",
    "st.subheader(\"Hydrologist | Climate Scientist | Digital Transformation Enthusiast\")\n",
    "st.image(image, caption=\"In the Lab\", use_column_width=True)\n",
    "\n",
    "# About Me\n",
    "st.header(\"About Me\")\n",
    "st.write(\"\"\"\n",
    "I am a Hydrologist and Climate Scientist passionate about applying digital tools to manage \n",
    "water-related disasters, droughts, and sustainability challenges in developing countries. \n",
    "My background combines hydrological modeling, remote sensing, climate data analysis, and \n",
    "Bayesian statistical methods.\n",
    "\"\"\")\n",
    "\n",
    "# Project\n",
    "st.header(\"Project: Drought Pattern Analysis in the Alazani River Basin\")\n",
    "st.write(\"\"\"\n",
    "Analyzed hydroclimatic drivers using ERA5 climate reanalysis data and Bayesian modeling \n",
    "approaches to support drought risk management strategies in the region.\n",
    "\"\"\")\n",
    "\n",
    "# Skills\n",
    "st.header(\"Skills & Tools\")\n",
    "st.write(\"\"\"\n",
    "- Programming: Python (Pandas, NumPy, Matplotlib), R, MATLAB  \n",
    "- GIS & Remote Sensing: QGIS, ArcGIS, Google Earth Engine  \n",
    "- Modeling & Analysis: Hydrological Modeling, Climate Data Analysis, Machine Learning\n",
    "\"\"\")\n",
    "\n",
    "# Goals\n",
    "st.header(\"Goals for Joining the Digital Transformation Programme\")\n",
    "st.write(\"\"\"\n",
    "To integrate digital transformation into environmental and water resource challenges, \n",
    "design human-centered solutions, and collaborate on real-world projects with diverse teams.\n",
    "\"\"\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0886be70-3809-4262-9c6d-c697304dd7b4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cfef2018-cdca-49bd-8def-de760ef4b96b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
