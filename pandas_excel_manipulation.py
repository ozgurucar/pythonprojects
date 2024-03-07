import pandas as pd 
path = "D:/test.xlsx"
veri = pd.read_excel(path)
veri['Toplam Fiyat'] = veri['Adet'] * veri['Birim Fiyat']
veri.to_excel(path, index=False)