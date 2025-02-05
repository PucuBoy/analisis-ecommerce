from src.data_processing import load_and_preprocess, save_to_sql
from src.eda import exploratory_analysis
from src.clustering import customer_clustering

if __name__ == "__main__":
    # Langkah 1: Load dan preprocessing data
    df = load_and_preprocess()
    save_to_sql(df)
    
    # Langkah 2: Analisis eksploratif
    exploratory_analysis()
    
    # Langkah 3: Klustering pelanggan
    customer_clustering()
    print("Proses selesai! Cek folder outputs/ dan database/.")