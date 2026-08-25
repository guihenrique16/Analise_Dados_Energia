import pandas as pd
import numpy as np


# ETAPA A — Simulando o Orange Data Mining no Python / Pandas 

# https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction
df_original = pd.read_csv('AppliancesEnergyPrediction.csv')

print("--- [ETAPA A] Dataset Original Carregado ---")
print(f"Linhas/Colunas originais: {df_original.shape}")

# 2. Selecionar Colunas (Widget Select Columns)
# Appliances, lights, 3 temperaturas (T1, T2, T3) e 3 umidades (RH_1, RH_2, RH_3)
colunas_selecionadas = ['Appliances', 'lights', 'T1', 'T2', 'T3', 'RH_1', 'RH_2', 'RH_3']
df_filtrado = df_original[colunas_selecionadas].copy()

# 3. Verificar valores ausentes/nulos
print("\n--- Verificação de Valores Ausentes ---")
print(df_filtrado.isnull().sum())

# 4. Amostragem de 10% (Widget Data Sampler)
# random_state=42 garante que a amostra seja idêntica toda vez que rodar
amostra = df_filtrado.sample(frac=0.10, random_state=42).reset_index(drop=True)

print(f"\nTamanho da amostra (10%): {amostra.shape}")

# 5. Exportar a amostra para CSV (Widget Save Data)
amostra.to_csv("amostra_energydata_10pct.csv", index=False)
print("Amostra salva como 'amostra_energydata_10pct.csv' com sucesso!\n")


# ETAPA B — Análise de Dados no Pandas

# 1. Carregar a amostra gerada
df = pd.read_csv("Appliances_EnergyPrediction/amostra_energydata_10pct.csv")


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


df.rename(columns={
    'Appliances': 'Consumo_Eletrodomesticos',
    'T1': 'Temp_Cozinha',
    'T2': 'Temp_Sala',
    'T3': 'Temp_Lavanderia',
    'RH_1': 'Umid_Cozinha',
    'RH_2': 'Umid_Sala',
    'RH_3': 'Umid_Lavanderia'
}, inplace=True)

print("\n--- Colunas Renomeadas ---")
print(df.columns)

# 3. Maior consumo de eletrodomésticos na amostra
max_consumo = df['Consumo_Eletrodomesticos'].max()
print(f"\nMaior consumo de eletrodomésticos registrado: {max_consumo} Wh")

# 4. Limiar de 70% do consumo máximo
limiar_70 = 0.70 * max_consumo
print(f"Limiar de 70% do consumo máximo: {limiar_70:.2f} Wh")

# Criar DataFrame com consumo > 70% do máximo
df_consumo_alto = df[df['Consumo_Eletrodomesticos'] > limiar_70]

# 5. Contagem e percentual da amostra
total_amostra = df.shape[0]
qtd_consumo_alto = df_consumo_alto.shape[0]
pct_consumo_alto = (qtd_consumo_alto / total_amostra) * 100

print(f"\nRegistros com consumo > 70%: {qtd_consumo_alto}")
print(f"Representação na amostra: {pct_consumo_alto:.2f}%")

# 6. Temperatura média de T1 (Temp_Cozinha) e segundo filtro
media_temp_cozinha = df['Temp_Cozinha'].mean()
print(f"\nTemperatura média da cozinha (Temp_Cozinha / T1): {media_temp_cozinha:.2f} °C")

# DataFrame com ambos os critérios: consumo > 70% E temperatura > média
df_consumo_e_temp_alta = df[
    (df['Consumo_Eletrodomesticos'] > limiar_70) & 
    (df['Temp_Cozinha'] > media_temp_cozinha)
]

qtd_duplo_criterio = df_consumo_e_temp_alta.shape[0]
pct_duplo_criterio = (qtd_duplo_criterio / total_amostra) * 100

print(f"Registros com consumo > 70% E temp > média: {qtd_duplo_criterio}")
print(f"Representação na amostra: {pct_duplo_criterio:.2f}%")

# 7. Comparação e Explicação
print("\n==================================================")
print("--- Comparação e Análise dos Resultados ---")
print("==================================================")
print(f"Apenas Consumo Alto (>70%): {qtd_consumo_alto} registros ({pct_consumo_alto:.2f}%)")
print(f"Consumo Alto (>70%) + Temp Acima da Média: {qtd_duplo_criterio} registros ({pct_duplo_criterio:.2f}%)")

