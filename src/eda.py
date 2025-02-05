import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
from src.config import DB_PATH
from sqlalchemy import create_engine

def exploratory_analysis():
    engine = create_engine(f'sqlite:///{DB_PATH}')
    df = pd.read_sql('transactions', engine)
    
    # Plot total transaksi per negara
    plt.figure(figsize=(12, 6))
    country_sales = df.groupby('Country')['total_price'].sum().nlargest(10)
    sns.barplot(x=country_sales.values, y=country_sales.index, palette='viridis')
    plt.title('Top 10 Negara dengan Penjualan Tertinggi')
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'plots')
    os.makedirs(output_dir, exist_ok=True)  

    plt.savefig(os.path.join(output_dir, 'top_countries.png'))
    
    # Distribusi harga
    plt.figure(figsize=(10, 6))
    sns.histplot(df['total_price'], bins=50, kde=True)
    plt.title('Distribusi Total Harga per Transaksi')
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'plots')
    os.makedirs(output_dir, exist_ok=True)

    plt.savefig(os.path.join(output_dir,'price_distribution.png'))