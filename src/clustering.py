import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from src.config import DB_PATH
from sqlalchemy import create_engine

def customer_clustering():
    engine = create_engine(f'sqlite:///{DB_PATH}')
    df = pd.read_sql('transactions', engine)
    
    # Aggregasi data pelanggan
    customer_data = df.groupby('customer_id').agg({
        'total_price': 'sum',
        'Quantity': 'sum',
        'order_id': 'nunique'
    }).rename(columns={'order_id': 'total_orders'})
    
    # Normalisasi
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(customer_data)
    
    # Klustering K-Means
    kmeans = KMeans(n_clusters=4, random_state=42)
    customer_data['cluster'] = kmeans.fit_predict(scaled_data)
    
    # Simpan hasil ke SQL
    customer_data.to_sql('customer_clusters', engine, if_exists='replace')