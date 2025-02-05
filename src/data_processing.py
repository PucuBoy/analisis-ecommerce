import pandas as pd 
from sqlalchemy import create_engine
from src.config import DATA_PATH, DB_PATH

def load_and_preprocess():
    df = pd.read_csv(DATA_PATH, encoding='latin1')

    df = df.rename(columns={
        'InvoiceNo': 'order_id',
        'StockCode': 'product_id',
        'CustomerID': 'customer_id',
        'InvoiceDate': 'order_date'
    })

    df = df[df['customer_id'].notna()]
    df['customer_id'] = df['customer_id'].astype(int)
    df = df[df['Quantity'] > 0]

    df['total_price'] = df['Quantity'] * df['UnitPrice']
    return df

def save_to_sql(df):
    engine = create_engine(f'sqlite:///{DB_PATH}')
    df.to_sql('transactions', engine, if_exists='replace', index=False)