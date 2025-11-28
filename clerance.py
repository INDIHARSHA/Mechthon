{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f7f9789-c27d-4549-8683-cd6353a214c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Clearance:\n",
    "    def __init__(self):\n",
    "        self.hole_dia = float(input(\"Please enter the diameter of Hole \"))\n",
    "        self.ll_hole = float(input(\"Please enter the LowerLimit of Hole \"))\n",
    "        self.up_hole = float(input(\"Please enter the UpperLimit of Hole \"))\n",
    "        self.shaft_dia = float(input(\"Please enter the diameter of Shaft \"))\n",
    "        self.ll_shaft = float(input(\"Please enter the LowerLimit of Shaft \"))\n",
    "        self.up_shaft = float(input(\"Please enter the UpperLimit of Shaft \"))\n",
    "        choice = int(input(\"Enter 0 for Minimum Clearance, 1 for Maximum Clearance: \"))\n",
    "\n",
    "        if choice == 0:\n",
    "            print(\"Minimum Clearance:\", self.minimum_clearance())\n",
    "        else:\n",
    "            print(\"Maximum Clearance:\", self.maximum_clearance())\n",
    "\n",
    "    def minimum_clearance(self):\n",
    "        return self.ll_hole - self.up_shaft\n",
    "\n",
    "    def maximum_clearance(self):\n",
    "        return self.up_hole - self.ll_shaft\n",
    "\n",
    "Clearance()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "413b7226-bac0-4d50-b38f-b551efe5d8d9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
