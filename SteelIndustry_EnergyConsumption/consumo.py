import pandas as pd
import numpy as np


# ETAPA A — Simulando o Orange Data Mining no Python / Pandas

# https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption
df_original = pd.read_csv('Steel_industry_data.csv')

print("--- [ETAPA A] Dataset Original Carregado ---")
print(f"Linhas/Colunas originais: {df_original.shape}")

# 2. Seleção de Colunas (Widget Select Columns)
colunas_selecionadas = [
    'Usage_kWh', 
    'Lagging_Current_Reactive.Power_kVarh',
    'Leading_Current_Reactive_Power_kVarh', 
    'Lagging_Current_Power_Factor', 
    'Leading_Current_Power_Factor', 
    'WeekStatus', 
    'Day_of_week', 
    'Load_Type'
]
df_filtrado = df_original[colunas_selecionadas].copy()

# 3. Observar categorias e valores ausentes (Widget Data Table)
print("\n--- Categorias em Load_Type ---")
print(df_filtrado['Load_Type'].value_counts())

print("\n--- Categorias em WeekStatus ---")
print(df_filtrado['WeekStatus'].value_counts())

print("\n--- Verificação de Valores Ausentes ---")
print(df_filtrado.isnull().sum())

# 4. Amostragem aleatória de 20% (Widget Data Sampler)
amostra = df_filtrado.sample(frac=0.20, random_state=42).reset_index(drop=True)
print(f"\nTamanho da amostra (20%): {amostra.shape}")

# 5. Exportar a amostra em CSV (Widget Save Data)
amostra.to_csv("amostra_steel_industry_20pct.csv", index=False)
print("Amostra salva como 'amostra_steel_industry_20pct.csv' com sucesso!\n")


# ETAPA B — Análise de Dados e Limiares de Operação

# 1. Carregar a amostra gerada e renomear colunas
df = pd.read_csv("amostra_steel_industry_20pct.csv")

df.rename(columns={
    'Usage_kWh': 'Consumo_kWh',
    'Lagging_Current_Power_Factor': 'FP_Atrasado',
    'Leading_Current_Power_Factor': 'FP_Adiantado',
    'Lagging_Current_Reactive_Power_kVARh': 'Reativa_Atrasada_kVARh',
    'Leading_Current_Reactive_Power_kVARh': 'Reativa_Adiantada_kVARh'
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

# 3. Maior consumo e limiar de 75%
max_consumo = df['Consumo_kWh'].max()
limiar_75 = 0.75 * max_consumo

print(f"\nMaior consumo registrado: {max_consumo:.2f} kWh")
print(f"Limiar de 75% do consumo máximo: {limiar_75:.2f} kWh")

# 4. DataFrame com consumo acima de 75% e métricas
df_consumo_alto = df[df['Consumo_kWh'] > limiar_75]
total_amostra = df.shape[0]
qtd_consumo_alto = df_consumo_alto.shape[0]
pct_consumo_alto = (qtd_consumo_alto / total_amostra) * 100

print(f"\nRegistros com consumo > 75%: {qtd_consumo_alto}")
print(f"Representação na amostra: {pct_consumo_alto:.2f}%")

# 5. Registros de consumo alto na categoria 'Maximum Load'
qtd_max_load = df_consumo_alto[df_consumo_alto['Load_Type'] == 'Maximum Load'].shape[0]
pct_max_load = (qtd_max_load / qtd_consumo_alto) * 100 if qtd_consumo_alto > 0 else 0

print(f"Desses registros de consumo alto, {qtd_max_load} ({pct_max_load:.2f}%) pertencem a 'Maximum Load'")

# 6. Escolha e limite para o Fator de Potência (FP_Atrasado)
# O fator de potência varia de 0 a 100 (ou 0 a 1). Valores abaixo de 85 (ou 0.85) indicam baixa eficiência reativa.
limite_fp = 85.0 

# 7. DataFrame simultâneo: Consumo > 75% E Fator de Potência Baixo (< 85)
df_critico = df[(df['Consumo_kWh'] > limiar_75) & (df['FP_Atrasado'] < limite_fp)]
qtd_critico = df_critico.shape[0]
pct_critico = (qtd_critico / total_amostra) * 100

print(f"\nRegistros com consumo > 75% E FP_Atrasado < {limite_fp}: {qtd_critico}")
print(f"Representação na amostra: {pct_critico:.2f}%")

# 8. Exibição final da comparação
print("\n==================================================")
print("--- Resumo Comparativo ---")
print("==================================================")
print(f"Consumo Elevado (> 75%): {qtd_consumo_alto} registros ({pct_consumo_alto:.2f}%)")
print(f"Consumo Elevado + FP Baixo (< 85): {qtd_critico} registros ({pct_critico:.2f}%)")