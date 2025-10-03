import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Global finance data.csv')
df['Date']=pd.to_datetime(df['Date'], errors='coerce')
print("Raws × Columns:", df.shape)
print("Unique countries:",df['Country'].nunique())
print("Data range:",df['Date'].min(),df['Date'].max())
print("\nPreview:")
print(df.head())

kpi_cols =[
    "Country","Date",
    "GDP_Growth_Rate_Percent",
    "Inflation_Rate_Percent",
    "Unemployment_Rate_Percent",
    "Market_Cap_Trillion_USD",
    "Export_Growth_Percent",
    "Import_Growth_Percent",
    "Credit_Rating"
]
df_kpi=df[kpi_cols].copy()

df_kpi["Trade_Balance"]=df_kpi["Export_Growth_Percent"]-df_kpi["Import_Growth_Percent"]
print(df_kpi.head())

print("\nTop 5 GDP Growth:")
print(df_kpi.nlargest(5, "GDP_Growth_Rate_Percent")[["Country","GDP_Growth_Rate_Percent"]])

print("\nTop 5 Inflation:")
print(df_kpi.nlargest(5, "Inflation_Rate_Percent")[["Country","Inflation_Rate_Percent"]])

print("\nTop 5 Trade Surplus:")
print(df_kpi.nlargest(5, "Trade_Balance")[["Country","Trade_Balance"]])

print("\nTop 5 Trade Deficit:")
print(df_kpi.nsmallest(5, "Trade_Balance")[["Country","Trade_Balance"]])

print("\nTop 10 Market Cap")
print(df_kpi.nlargest(10, "Market_Cap_Trillion_USD")[["Country","Market_Cap_Trillion_USD"]])

plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df_kpi,
    x= "GDP_Growth_Rate_Percent",
    y="Inflation_Rate_Percent",
    size="Market_Cap_Trillion_USD",
    sizes=(20,500),
    hue="Country",
    legend=False
)
df_kpi.to_csv("finance_kpi_clean.csv", index=False)

plt.title("GDP Growth vs Inflation (bubble size = Market Cap)")
plt.show()

top10_mc = df_kpi.nlargest(10,"Market_Cap_Trillion_USD")
plt.figure(figsize=(10,6))
sns.barplot(data=top10_mc, x="Country",y="Market_Cap_Trillion_USD")
plt.xticks(rotation=45)
plt.title("Top 10 Countries by Market Cap")
plt.show()