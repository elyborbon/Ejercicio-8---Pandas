import pandas as pd
datos = pd.Series([100, 200, "python", 300.15, 500.8])
print (datos)
datos = pd.to_numeric(datos, errors= "coerce")
print (datos)