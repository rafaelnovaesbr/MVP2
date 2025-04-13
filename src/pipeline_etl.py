import pandas as pd

def extract_data(input_path):
    """Extrai os dados do CSV."""
    df = pd.read_csv(input_path)
    print("Dados extraídos: {} linhas e {} colunas".format(*df.shape))
    return df

def transform_data(df):
    """Transforma os dados: converte tipos, trata valores ausentes e processa a coluna de gêneros."""
    df['imdbRating'] = pd.to_numeric(df['imdbRating'], errors='coerce')
    df['votes'] = pd.to_numeric(df['votes'], errors='coerce')
    
    # Remover registros sem avaliação
    df = df.dropna(subset=['imdbRating'])
    
    # Processar a coluna de gêneros
    if 'genres' in df.columns:
        df['genre_list'] = df['genres'].apply(lambda x: [g.strip() for g in x.split(',')] if isinstance(x, str) else [])
    
    # Remover duplicatas
    df = df.drop_duplicates()
    return df

def load_data(df, output_path):
    """Salva o DataFrame transformado em um novo CSV."""
    df.to_csv(output_path, index=False)
    print("Dados transformados salvos em:", output_path)

def main():
    input_path = '/mnt/data/imdb_top_5000_tv_shows.csv'
    output_path = '/mnt/data/imdb_top_5000_tv_shows_transformado.csv'
    
    df = extract_data(input_path)
    df = transform_data(df)
    load_data(df, output_path)

if __name__ == '__main__':
    main()
