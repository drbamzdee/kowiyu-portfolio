{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "67370428-85d6-4ec4-b91c-e5003f6bc295",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from fpdf import FPDF\n",
    "\n",
    "class PDF(FPDF):\n",
    "    def header(self):\n",
    "        self.set_font('Arial', 'B', 14)\n",
    "        self.cell(0, 10, 'Kowiyu Abidemi Bamidele - Digital Transformation Portfolio', ln=True, align='C')\n",
    "        self.ln(10)\n",
    "\n",
    "    def chapter_title(self, title):\n",
    "        self.set_font('Arial', 'B', 12)\n",
    "        self.set_text_color(30, 30, 30)\n",
    "        self.cell(0, 10, title, ln=True)\n",
    "        self.ln(5)\n",
    "\n",
    "    def chapter_body(self, body):\n",
    "        self.set_font('Arial', '', 11)\n",
    "        self.multi_cell(0, 10, body)\n",
    "        self.ln()\n",
    "\n",
    "pdf = PDF()\n",
    "pdf.add_page()\n",
    "\n",
    "# Introduction\n",
    "pdf.chapter_title(\"About Me\")\n",
    "pdf.chapter_body(\"Hydrologist and Climate Scientist passionate about applying digital tools in managing water-related disasters, droughts, and sustainability in developing countries.\")\n",
    "\n",
    "# Project Example\n",
    "pdf.chapter_title(\"Project: Drought Pattern Analysis in the Alazani River Basin\")\n",
    "pdf.chapter_body(\"Analyzed hydroclimatic drivers using ERA5 data and Bayesian modeling to support drought risk management strategies.\")\n",
    "\n",
    "# Digital Tools\n",
    "pdf.chapter_title(\"Skills & Tools\")\n",
    "pdf.chapter_body(\"Python (Pandas, NumPy, Matplotlib), R, MATLAB, QGIS, ArcGIS, Remote Sensing, Machine Learning.\")\n",
    "\n",
    "# Goals\n",
    "pdf.chapter_title(\"Goals for Joining the Digital Transformation Programme\")\n",
    "pdf.chapter_body(\"To integrate digital transformation into environmental and water resource challenges, design human-centered solutions, and collaborate on real-world projects with diverse teams.\")\n",
    "\n",
    "pdf.output(\"Kowiyu_Portfolio.pdf\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c507754c-71c7-4c7a-8e20-b7430a1837f9",
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
