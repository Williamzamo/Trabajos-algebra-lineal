import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.DataFrame({"paciente": ["P1","P2","P3","P4","P5","P6"],
                   "edad": [23, np.nan, 45, 31, np.nan, 52],
                   "peso_kg": [68, 72, np.nan, 85, 61, np.nan],
                   "grupo": ["A", "B", "A", None, "B", "A"],
                   "resultado": ["Positivo", "Negativo", np.nan, "Positivo", "Negativo", "Negativo"]                   
})
#cuantos nulos hay por columna
print(df.isnull())#true y false
print(df.isnull().sum())

