
import os
import zipfile
import pandas as pd

def download_dataset_kaggle(dataset: str, output_path: str):
    """
    Descarga un dataset desde Kaggle utilizando la API oficial.
    :param dataset: El identificador del dataset (e.g. "lokeshparab/amazon-products-dataset")
    :param output_path: Ruta donde guardar el archivo descargado
    """
    os.system(f'kaggle datasets download -d {dataset} -p {output_path} --unzip')

def load_and_combine_csv(folder_path: str) -> pd.DataFrame:
    """
    Carga y combina todos los archivos CSV en una carpeta.
    :param folder_path: Ruta de la carpeta que contiene los CSVs
    :return: DataFrame combinado
    """
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    all_dfs = [pd.read_csv(os.path.join(folder_path, f)) for f in csv_files]
    combined_df = pd.concat(all_dfs, ignore_index=True)
    return combined_df
