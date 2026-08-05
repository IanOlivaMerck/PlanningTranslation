from pathlib import Path
parent_directory = Path.cwd().parent.parent
print(parent_directory) 
type(parent_directory)
import pandas as pd
import numpy as np
from pathlib import Path
#reemplazar con la ruta de los archivos correcta
parent_directory = Path.cwd().parent.parent
FCST=pd.read_excel(parent_directory / "FCST Merck Abril 26.xlsx",sheet_name="Abril 2026")
PROD_DC_2=pd.read_excel(parent_directory / "PRODUCTOS DC.xlsx",sheet_name="Catalogo")