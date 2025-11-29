{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c18ee436-edac-4b3c-9d7f-f0fa35f91c2a",
   "metadata": {},
   "source": [
    "Shrinkage allowance = aL(Tf– T0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "bffe203e-327f-4485-8059-dad359e930fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Shrinkageallowance(tm,lnth,mtemp,rtemp):\n",
    "    \"\"\"used to calculate Shrinkage allowance of all materials to assist efficient\n",
    "       casting, if you are unaware of thermal properties of materialtry to access the\n",
    "       csv Thermal expansion file, the problem takes the following argumets \n",
    "       tm=Thermalexpansion of material\n",
    "       lnth=length of casting material\n",
    "       mtemp=temperature of molten metal\n",
    "       rtemp=temperature of room temperature\n",
    "    \"\"\"\n",
    "    sh=0\n",
    "    sh=tm*lnth*(mtemp-rtemp)\n",
    "    return sh"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6b3510fc-fa29-4856-9088-4b2e08319da8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_csv(\"Thermalexpansion.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8c0f28a6-f669-4f41-b5f9-b7bb477479d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Material \\tThermal expansion (1/°C) 10-6 \n",
      "0                                Acrylic\\t70\n",
      "1                                  Air\\t3400\n",
      "2                             Aluminum\\t23.1\n",
      "3                            Beryllium\\t11.3\n",
      "4                    Borosilicate Glass\\t3.3\n",
      "5                                Brass\\t19.0\n",
      "6                               Bronze\\t18.7\n",
      "7                          Carbon Fiber\\t0.8\n",
      "8                         Carbon Steel\\t10.8\n",
      "9                              Cast Iron\\t11\n",
      "10                       Ceramics\\t3.0 - 5.0\n",
      "11                        Chrome Steel\\t12.0\n",
      "12                                Cobalt\\t13\n",
      "13                              Concrete\\t12\n",
      "14                              Copper\\t16.5\n",
      "15                        Diamond\\t1.0 - 1.3\n",
      "16                     Epoxy Resin\\t60 - 120\n",
      "17                              Ethanol\\t250\n",
      "18                             Gasoline\\t315\n",
      "19                                Glass\\t9.0\n",
      "20                          Glass Fiber\\t5.5\n",
      "21                                  Gold\\t14\n",
      "22                              Granite\\t7.9\n",
      "23                             Graphite\\t4.5\n",
      "24                             Inconel\\t12.5\n",
      "25                                Indium\\t33\n",
      "26                                Invar\\t1.2\n",
      "27                              Iridium\\t6.5\n",
      "28                                Iron\\t11.8\n",
      "29                                  Lead\\t29\n",
      "30                              Limestone\\t8\n",
      "31                               Lithium\\t46\n",
      "32                             Magnesium\\t26\n",
      "33                             Manganese\\t22\n",
      "34                                 Marble\\t7\n",
      "35                                   Mica\\t3\n",
      "36                           Molybdenum\\t4.8\n",
      "37                              Nickel\\t13.5\n",
      "38                                Nylon\\t110\n",
      "39                               Osmium\\t5.5\n",
      "40                               Platinum\\t9\n",
      "41                            Polyester\\t125\n",
      "42                    Polyethylene (PE)\\t110\n",
      "43                   Polypropylene (PP)\\t150\n",
      "44                      Polystyrene (PS)\\t70\n",
      "45                      Quartz - Fused\\t0.55\n",
      "46                             Rock salt\\t40\n",
      "47                                Rubber\\t80\n",
      "48                                Silicon\\t3\n",
      "49                              Silver\\t19.5\n",
      "50                                Sodium\\t71\n",
      "51                                 Steel\\t12\n",
      "52                        Teflon (PTFE)\\t112\n",
      "53                            Thallium\\t29.9\n",
      "54                             Thulium\\t13.5\n",
      "55                                   Tin\\t22\n",
      "56                             Titanium\\t8.5\n",
      "57                             Tungsten\\t4.5\n",
      "58                             Uranium\\t13.5\n",
      "59                                 Water\\t69\n",
      "60                                 Water\\t69\n",
      "61                                  Wax\\t6.5\n",
      "62                             Ytterbium\\t26\n",
      "63                               Yttrium\\t11\n",
      "64                                  Zinc\\t35\n",
      "65                            Zirconium\\t5.5\n"
     ]
    }
   ],
   "source": [
    "print(df.to_string())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2bda1dce-29c6-433c-9125-b86f5ae167c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 45\n",
      " 554\n",
      " 866\n",
      " 28\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "20891340.0"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tm=float(input())\n",
    "lnth=float(input())\n",
    "mtemp=float(input())\n",
    "rtemp=float(input())\n",
    "Shrinkageallowance(tm,lnth,mtemp,rtemp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4924b927-51c9-45e2-a578-8ce1415a9f71",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "219df0b7-c922-487d-8d1b-e46d9feb4d89",
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
