import pandas as pd

# ==============================================================================
# ETAPA A — Simulando o Orange Data Mining (Carga, Filtro e Amostragem 20%)
# ==============================================================================

try:
    df_original = pd.read_csv("Plant_1_Generation_Data.csv")
except FileNotFoundError:
    df_original = pd.read_csv()

print("--- [ETAPA A] Dataset Original Carregado ---")
print(f"Dimensões originais: {df_original.shape}")

# 2. Seleção de Colunas (Select Columns)
colunas_selecionadas = [
    'DATE_TIME', 
    'SOURCE_KEY', 
    'DC_POWER', 
    'AC_POWER', 
    'DAILY_YIELD', 
    'TOTAL_YIELD'
]
df_filtrado = df_original[colunas_selecionadas].copy()

# 3. Inspeção e verificação de nulos (Data Table)
print("\n--- Verificação de Valores Ausentes ---")
print(df_filtrado.isnull().sum())

print("\n--- Quantidade de registros com Potência CA (AC_POWER) igual a zero (Noite) ---")
zeros_ac = (df_filtrado['AC_POWER'] == 0).sum()
print(f"{zeros_ac} registros ({zeros_ac / df_filtrado.shape[0] * 100:.2f}% do total)")

# 4. Amostra de 20% (Data Sampler)
amostra = df_filtrado.sample(frac=0.20, random_state=42).reset_index(drop=True)
print(f"\nTamanho da amostra (20%): {amostra.shape}")

# 5. Exportar a amostra em CSV (Save Data)
amostra.to_csv("amostra_solar_generation_20pct.csv", index=False)
print("Amostra salva como 'amostra_solar_generation_20pct.csv' com sucesso!\n")


# ==============================================================================
# ETAPA B — Análise com Pandas
# ==============================================================================

# 1. Carregar amostra e renomear variáveis
df = pd.read_csv("amostra_solar_generation_20pct.csv")

df.rename(columns={
    'DATE_TIME': 'Data_Hora',
    'SOURCE_KEY': 'Inversor_ID',
    'DC_POWER': 'Potencia_CC',
    'AC_POWER': 'Potencia_CA',
    'DAILY_YIELD': 'Geracao_Diaria',
    'TOTAL_YIELD': 'Geracao_Total'
}, inplace=True)

# 2. Inspeção Inicial
print("==================================================")
print("--- [ETAPA B] Apresentação Inicial dos Dados ---")
print("==================================================")
print("\n--- head() ---")
print(df.head())

print("\n--- shape ---")
print(df.shape)

print("\n--- info() ---")
df.info()

print("\n--- describe() ---")
print(df.describe())

# 3. Determinar maior potência CA e limiar de 70%
max_ac = df['Potencia_CA'].max()
limiar_70 = 0.70 * max_ac

print(f"\nMaior Potência CA registrada: {max_ac:.2f} kW")
print(f"Limiar de 70% da Potência CA máxima: {limiar_70:.2f} kW")

# 4. Criar DataFrame com alta geração (> 70%)
df_alta_geracao = df[df['Potencia_CA'] > limiar_70]

total_amostra = df.shape[0]
qtd_alta_geracao = df_alta_geracao.shape[0]
pct_alta_geracao = (qtd_alta_geracao / total_amostra) * 100

print(f"\nRegistros acima de 70% da Potência CA: {qtd_alta_geracao}")
print(f"Representação na amostra: {pct_alta_geracao:.2f}%")

# 5. Frequência dos inversores na alta geração (value_counts)
print("\n--- Frequência de Inversores no Período de Alta Geração ---")
frequencia_inversores = df_alta_geracao['Inversor_ID'].value_counts()
print(frequencia_inversores)

# 6. Identificar o inversor mais frequente
inversor_top = frequencia_inversores.index[0]
qtd_top = frequencia_inversores.iloc[0]

print(f"\nInversor mais frequente em alta geração: {inversor_top} ({qtd_top} aparições)")