import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo enviado pelo usuário
import pandas as pd

# Caminho completo para o arquivo CSV na pasta Documentos
caminho = "D:\MVP\mvp2\imdb_top_5000_tv_shows.csv"

# Lendo o arquivo CSV
df = pd.read_csv(caminho)

# Exibindo as primeiras linhas
print(df.head())


# Conversões e tratamentos básicos
df['imdbRating'] = pd.to_numeric(df['imdbRating'], errors='coerce')
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['genre_list'] = df['genres'].apply(lambda x: [g.strip() for g in x.split(',')] if isinstance(x, str) else [])

# Explode os gêneros para contagem
df_exploded = df.explode('genre_list')
genre_counts = df_exploded['genre_list'].value_counts().head(10)

# Cria os gráficos
figures = []

# Gráfico de barras dos gêneros mais frequentes
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar')
plt.title("Top 10 Gêneros mais Frequentes")
plt.xlabel("Gênero")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()
figures.append(plt.gcf())
plt.clf()

# Gráfico de dispersão: votos vs. imdbRating
plt.figure(figsize=(10, 6))
plt.scatter(df['votes'], df['imdbRating'], alpha=0.3)
plt.title("Relação entre Número de Votos e Nota IMDB")
plt.xlabel("Número de Votos")
plt.ylabel("Nota IMDB")
plt.grid(True)
plt.tight_layout()
figures.append(plt.gcf())
plt.clf()

# Evolução da média do rating ao longo dos anos
ratings_by_year = df.groupby('year')['imdbRating'].mean().dropna()

plt.figure(figsize=(10, 6))
ratings_by_year.plot(marker='o')
plt.title("Média de Avaliações por Ano")
plt.xlabel("Ano")
plt.ylabel("Nota Média (IMDB)")
plt.grid(True)
plt.tight_layout()
figures.append(plt.gcf())
plt.clf()

figures

# Salva os gráficos como imagens PNG para inclusão no repositório GitHub
output_paths = [
    "/mnt/data/top_10_generos.png",
    "/mnt/data/votos_vs_nota.png",
    "/mnt/data/media_rating_por_ano.png"
]

# Recriação dos gráficos com salvamento

# 1. Top 10 Gêneros mais Frequentes
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar')
plt.title("Top 10 Gêneros mais Frequentes")
plt.xlabel("Gênero")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_paths[0])
plt.clf()

# 2. Relação entre Número de Votos e Nota Média
plt.figure(figsize=(10, 6))
plt.scatter(df['numVotes'], df['averageRating'], alpha=0.3)
plt.title("Relação entre Número de Votos e Nota Média")
plt.xlabel("Número de Votos")
plt.ylabel("Nota Média (IMDB)")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_paths[1])
plt.clf()

# 3. Média de Avaliações por Ano de Início
plt.figure(figsize=(10, 6))
ratings_by_year.plot(marker='o')
plt.title("Média de Avaliações por Ano de Início")
plt.xlabel("Ano")
plt.ylabel("Nota Média (IMDB)")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_paths[2])
plt.clf()

output_paths
