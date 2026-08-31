import pandas as pd

# ==============================================================================
# ETAPA A — Carga, Reestruturação e Amostragem (20%)
# ==============================================================================

# 1. Carregar arquivo original do seu CSV
df_original = pd.read_csv("wind_solar_data.csv")  # Ajuste o nome se necessário

# 2. Reestruturar o dataset (Transformar 'Source' em colunas 'Solar' e 'Wind')
# Agrupa por Date e por hora/período mantendo a soma da coluna Production
df_pivoted = df_original.pivot_table(
    index=['Date', 'Start_Hour'], 
    columns='Source', 
    values='Production', 
    aggfunc='sum'
).reset_index()

# Garantir seleção das colunas desejadas
df_filtrado = df_pivoted[['Date', 'Solar', 'Wind']].copy()

# 3. Verificação de valores ausentes
print("--- Verificação de Valores Ausentes ---")
print(df_filtrado.isnull().sum())
df_filtrado.fillna(0, inplace=True)  # Preenche dias/horas sem geração com 0

# 4. Amostra aleatória de 20%
amostra = df_filtrado.sample(frac=0.20, random_state=42).reset_index(drop=True)
print(f"\nTamanho da amostra (20%): {amostra.shape}")

# 5. Exportar amostra em CSV
amostra.to_csv("amostra_wind_solar_20pct.csv", index=False)
print("Amostra salva como 'amostra_wind_solar_20pct.csv'!\n")


# ==============================================================================
# ETAPA B — Análise com Pandas
# ==============================================================================

# 1. Carregar amostra e renomear colunas
df = pd.read_csv("amostra_wind_solar_20pct.csv")

df.rename(columns={
    'Solar': 'Geracao_Solar',
    'Wind': 'Geracao_Eolica'
}, inplace=True)

# 2. Inspeção inicial
print("==================================================")
print("--- Inspeção Inicial ---")
print("==================================================")
print("\n--- head() ---")
print(df.head())

print("\n--- describe() ---")
print(df.describe())

# 3. Determinar valores máximos e limiares de 70%
max_solar = df['Geracao_Solar'].max()
max_eolica = df['Geracao_Eolica'].max()

limiar_70_solar = 0.70 * max_solar
limiar_70_eolica = 0.70 * max_eolica

print(f"\nMáximo Solar: {max_solar:.2f} | Limiar 70%: {limiar_70_solar:.2f}")
print(f"Máximo Eólica: {max_eolica:.2f} | Limiar 70%: {limiar_70_eolica:.2f}")

# 4. DataFrames de alta geração
df_alta_solar = df[df['Geracao_Solar'] > limiar_70_solar]
df_alta_eolica = df[df['Geracao_Eolica'] > limiar_70_eolica]

total_amostra = df.shape[0]

qtd_solar = df_alta_solar.shape[0]
pct_solar = (qtd_solar / total_amostra) * 100

qtd_eolica = df_alta_eolica.shape[0]
pct_eolica = (qtd_eolica / total_amostra) * 100

print("\n--- Frequência acima de 70% do próprio máximo ---")
print(f"Alta Geração Solar: {qtd_solar} registros ({pct_solar:.2f}%)")
print(f"Alta Geração Eólica: {qtd_eolica} registros ({pct_eolica:.2f}%)")