{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "aa8a9ecf-a06c-4a13-8a12-072303b0a760",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from PIL import Image\n",
    "\n",
    "# Load your image\n",
    "image = Image.open(\"lab_photo.jpg.jpeg\")\n",
    "\n",
    "# Page config\n",
    "st.set_page_config(page_title=\"Kowiyu Abidemi Bamidele\", layout=\"wide\")\n",
    "\n",
    "# Title and image\n",
    "st.image(image, caption=\"Kowiyu Abidemi Bamidele in the lab\", use_column_width=True)\n",
    "st.title(\"Digital Transformation Portfolio\")\n",
    "\n",
    "# About Me\n",
    "st.header(\"👨‍🔬 About Me\")\n",
    "st.write(\"\"\"\n",
    "Hydrologist and Climate Scientist passionate about applying digital tools in managing water-related disasters, \n",
    "droughts, and promoting sustainability in developing countries.\n",
    "\"\"\")\n",
    "\n",
    "# Project\n",
    "st.header(\"📊 Project: Drought Pattern Analysis in the Alazani River Basin\")\n",
    "st.write(\"\"\"\n",
    "Analyzed hydroclimatic drivers using ERA5 climate reanalysis data and Bayesian statistical modeling \n",
    "to support drought risk management strategies.\n",
    "\"\"\")\n",
    "\n",
    "# Skills\n",
    "st.header(\"🧠 Skills & Tools\")\n",
    "st.markdown(\"\"\"\n",
    "- Python (Pandas, NumPy, Matplotlib)\n",
    "- R, MATLAB\n",
    "- GIS Tools (QGIS, ArcGIS)\n",
    "- Remote Sensing\n",
    "- Machine Learning\n",
    "\"\"\")\n",
    "\n",
    "# Goals\n",
    "st.header(\"🎯 Goals for Joining the Digital Transformation Programme\")\n",
    "st.write(\"\"\"\n",
    "To integrate digital transformation into environmental and water resource challenges, \n",
    "design human-centered solutions, and collaborate on real-world projects with diverse teams.\n",
    "\"\"\")\n",
    "\n",
    "# Footer\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"🌍 Connect with me on [LinkedIn](https://www.linkedin.com/in/kowiyu-abidemi-bamidele/)\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0886be70-3809-4262-9c6d-c697304dd7b4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
