import pandas as pd
import numpy as np

# ==============================================================================
# ETAPA A — Simulando o Orange Data Mining (Tratamento e Amostragem de 10%)
# ==============================================================================


# Altere o pd.read_csv para incluir sep=';' e tratar o '?' como valor nulo
df_original = pd.read_csv("household_power_consumption.txt", sep=';', na_values='?', low_memory=False)


print("--- [ETAPA A] Dataset Original Carregado ---")
print(f"Dimensões originais: {df_original.shape}")

# 2 e 3. Inspeção e Tratamento de Valores Ausentes
print("\n--- Quantidade de Valores Ausentes por Coluna ---")
print(df_original.isnull().sum())

# Tratamento: Remoção das linhas com valores nulos/ausentes
df_tratado = df_original.dropna().copy()
print(f"\nDimensões após remoção de ausentes: {df_tratado.shape}")

# 4. Seleção de Colunas (Select Columns)
colunas_selecionadas = [
    'Global_active_power', 
    'Global_reactive_power', 
    'Voltage', 
    'Global_intensity', 
    'Sub_metering_1', 
    'Sub_metering_2', 
    'Sub_metering_3'
]
df_filtrado = df_tratado[colunas_selecionadas].copy()

# Garantir que as colunas sejam numéricas
for col in df_filtrado.columns:
    df_filtrado[col] = pd.to_numeric(df_filtrado[col])

# 5. Gerar amostra aleatória de 10%
amostra = df_filtrado.sample(frac=0.10, random_state=42).reset_index(drop=True)
print(f"\nTamanho da nova amostra (10%): {amostra.shape}")

# 6. Exportar amostra em CSV
amostra.to_csv("amostra_household_10pct.csv", index=False)
print("Amostra exportada como 'amostra_household_10pct.csv' com sucesso!\n")


# ==============================================================================
# ETAPA B — Análise com Pandas
# ==============================================================================

# 1. Carregar a nova amostra e renomear colunas
df = pd.read_csv("amostra_household_10pct.csv")

df.rename(columns={
    'Global_active_power': 'Potencia_Ativa',
    'Global_reactive_power': 'Potencia_Reativa',
    'Voltage': 'Tensao',
    'Global_intensity': 'Corrente',
    'Sub_metering_1': 'Consumo_Cozinha',
    'Sub_metering_2': 'Consumo_Lavanderia',
    'Sub_metering_3': 'Consumo_Climatizacao'
}, inplace=True)

# Inspeção inicial
print("==================================================")
print("--- [ETAPA B] Apresentação Inicial dos Dados ---")
print("==================================================")
print("\n--- head() ---")
print(df.head())

print("\n--- describe() ---")
print(df.describe())

# 2. Determinar valor máximo da potência ativa
max_potencia = df['Potencia_Ativa'].max()
print(f"\nMaior Potência Ativa registrada: {max_potencia:.2f} kW")

# 3. Calcule 75% do valor máximo e crie o DataFrame
limiar_75 = 0.75 * max_potencia
df_potencia_alta = df[df['Potencia_Ativa'] > limiar_75]

# 4. Quantidade e percentual de registros
total_amostra = df.shape[0]
qtd_potencia_alta = df_potencia_alta.shape[0]
pct_potencia_alta = (qtd_potencia_alta / total_amostra) * 100

print(f"Limiar de 75% da Potência Ativa: {limiar_75:.2f} kW" if 'limiar_70' in locals() else f"Limiar de 75%: {limiar_75:.2f} kW")
print(f"Registros com Potência Ativa > 75%: {qtd_potencia_alta} ({pct_potencia_alta:.2f}% da amostra)")

# 5. Calcule a corrente média da amostra
corrente_media = df['Corrente'].mean()
print(f"\nCorrente Média da amostra: {corrente_media:.2f} A")

# 6. Criar segundo DataFrame com duplo critério: Potência > 75% E Corrente > Média
df_critico = df[(df['Potencia_Ativa'] > limiar_75) & (df['Corrente'] > corrente_media)]

qtd_critico = df_critico.shape[0]
pct_critico = (qtd_critico / total_amostra) * 100

print(f"Registros com Potência > 75% E Corrente > Média: {qtd_critico} ({pct_critico:.2f}% da amostra)")

# Resumo Final
print("\n==================================================")
print("--- Resumo Comparativo ---")
print("==================================================")
print(f"Apenas Potência Elevada (> 75%): {qtd_potencia_alta} registros ({pct_potencia_alta:.2f}%)")
print(f"Potência Elevada + Corrente Acima da Média: {qtd_critico} registros ({pct_critico:.2f}%)")