import numpy as np
import pandas as pd

file="supply_chain_messy.csv"
df=pd.read_csv(file)

print("-------------------------")
print(df.shape)
print("-------------------------")
print(df.head())
print("-------------------------")
print(df.columns)
print("-----1.Valori lipsa initiale--------")
print(df.isnull().sum())
df["Supplier"]=df["Supplier"].fillna("Unknown Supplier")#pt supplier

media=df[df["ShippingCost"]>0]["ShippingCost"].mean()
df.loc[df["ShippingCost"]<0,"ShippingCost"]=np.nan  #punem media pt shipping
df["ShippingCost"]=df["ShippingCost"].fillna(media)


print("------2.curatarea duplicatelor------------------")
noOfDuplicates=df.duplicated().sum()
df=df.drop_duplicates()
print(f"Au fost sterse {noOfDuplicates} randuri duplicate")
print("-------3.Curatarea textului (spatii libere)-----------------")
print(df['Destination'].unique())
df["Destination"]=df["Destination"].str.strip()
city_mapping={"new york":"New York","NY":"New York"}
df["Destination"]=df["Destination"].replace(city_mapping)
print("-------------------------")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'])
# 6. Corectarea anomaliilor logice (DeliveryDate < OrderDate)
# Dacă data livrării e înaintea comenzii, considerăm că e o eroare și setăm DeliveryDate ca NaT, apoi o estimăm sau o corectăm
invalid_dates = df['DeliveryDate'] < df['OrderDate']
print(
    f'\n[Clean] Număr de rânduri cu anomalie de date (Livrare < Comandă): {invalid_dates.sum()}'
)
# Le corectăm adăugând o medie de 3 zile la OrderDate pentru a repara anomalia
df.loc[invalid_dates, 'DeliveryDate'] = df.loc[invalid_dates, 'OrderDate'] + pd.Timedelta(
    days=3
)

# Pentru DeliveryDate complet lipsă (NaN), le estimăm tot pe baza unei medii de transport de 4 zile
df['DeliveryDate'] = df['DeliveryDate'].fillna(df['OrderDate'] + pd.Timedelta(days=4))
# 1. Ne asigurăm că ShippingCost este convertit corect în numeric
df['ShippingCost'] = pd.to_numeric(df['ShippingCost'], errors='coerce')

# 2. Identificăm mediana pe baza valorilor normale (ex: între 0 și 10.000)
valid_median_cost = df.loc[(df['ShippingCost'] > 0) & (df['ShippingCost'] <= 10000), 'ShippingCost'].median()

# 3. Tăiem și înlocuim orice valoare absurdă (> 10000, negativă sau nulă) cu mediana curată
df.loc[(df['ShippingCost'] > 10000) | (df['ShippingCost'] < 0) | (df['ShippingCost'].isna()), 'ShippingCost'] = valid_median_cost

# 4. Rotunjim totul la 2 zecimale, exact ca un cost real
df['ShippingCost'] = df['ShippingCost'].round(2)

print("--------7.Feature Engineering---------------")
# Timpul de tranzit în zile
df["TransitDays"]=(df["DeliveryDate"]-df["OrderDate"]).dt.days
# Costul unitar de transport per cantitate
df["ShippingCostPerUnit"]=df["ShippingCost"]/df["Quantity"]
# An și Lună pentru analize de trend
df["YearMonth"]=df["OrderDate"].dt.to_period("M").astype(str)
# Statusul livrării
df["DeliveryStatus"]=np.where(df["TransitDays"]<=6,"In-Time","Delayed")

print(df.isnull().sum())

# Recalculăm corect costul per unitate pe baza noului ShippingCost curățat și a cantității
df['ShippingCostPerUnit'] = np.round(df['ShippingCost'] / df['Quantity'], 2)

df.to_csv("supply_chain_cleaned1.csv",index=False)