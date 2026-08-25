import pandas as pd

# ==============================================================================
# ETAPA A — Simulando o Orange Data Mining (Carga, Filtro e Amostragem 15%)
# ==============================================================================

df_original = pd.read_csv('TetuanCityPowerConsumption.csv')

print("--- [ETAPA A] Dataset Original Carregado ---")
print(f"Dimensões originais: {df_original.shape}")

# 2. Seleção de Colunas (Select Columns)
colunas_selecionadas = [
    'Zone 1 Power Consumption',
    'Zone 2  Power Consumption', # Atente-se ao duplo espaço no dataset original UCI se necessário
    'Zone 3  Power Consumption',
    'Temperature',
    'Humidity',
    'Wind Speed'
]

# Normalização de nomes de colunas para evitar erros de espaço duplo
df_original.columns = df_original.columns.str.strip().str.replace(r'\s+', ' ', regex=True)

colunas_corrigidas = [
    'Zone 1 Power Consumption',
    'Zone 2 Power Consumption',
    'Zone 3 Power Consumption',
    'Temperature',
    'Humidity',
    'Wind Speed'
]

df_filtrado = df_original[colunas_corrigidas].copy()

# 3. Verificação de Nulos
print("\n--- Verificação de Valores Ausentes ---")
print(df_filtrado.isnull().sum())

# 4. Amostra de 15% (Data Sampler)
amostra = df_filtrado.sample(frac=0.15, random_state=42).reset_index(drop=True)
print(f"\nTamanho da amostra (15%): {amostra.shape}")

# 5. Exportar CSV (Save Data)
amostra.to_csv("amostra_tetouan_15pct.csv", index=False)
print("Amostra salva como 'amostra_tetouan_15pct.csv' com sucesso!\n")


# ==============================================================================
# ETAPA B — Análise com Pandas
# ==============================================================================

# 1. Carregar amostra e renomear colunas
df = pd.read_csv("amostra_tetouan_15pct.csv")

df.rename(columns={
    'Zone 1 Power Consumption': 'Consumo_Zona_1',
    'Zone 2 Power Consumption': 'Consumo_Zona_2',
    'Zone 3 Power Consumption': 'Consumo_Zona_3',
    'Temperature': 'Temperatura',
    'Humidity': 'Umidade',
    'Wind Speed': 'Velocidade_Vento'
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

# 3. Picos de Consumo por Zona
max_z1 = df['Consumo_Zona_1'].max()
max_z2 = df['Consumo_Zona_2'].max()
max_z3 = df['Consumo_Zona_3'].max()

picos = {
    'Consumo_Zona_1': max_z1,
    'Consumo_Zona_2': max_z2,
    'Consumo_Zona_3': max_z3
}

zona_maior_pico = max(picos, key=picos.get)
maior_pico_valor = picos[zona_maior_pico]

print("\n--- Picos de Consumo Registrados ---")
print(f"Zona 1: {max_z1:.2f} kW")
print(f"Zona 2: {max_z2:.2f} kW")
print(f"Zona 3: {max_z3:.2f} kW")
print(f"-> Maior pico: {zona_maior_pico} com {maior_pico_valor:.2f} kW")

# 4. Limiar de 70% na zona com maior pico
limiar_70 = 0.70 * maior_pico_valor
df_consumo_alto = df[df[zona_maior_pico] > limiar_70]

total_amostra = df.shape[0]
qtd_consumo_alto = df_consumo_alto.shape[0]
pct_consumo_alto = (qtd_consumo_alto / total_amostra) * 100

print(f"\nLimiar de 70% para {zona_maior_pico}: {limiar_70:.2f} kW")
print(f"Registros acima de 70%: {qtd_consumo_alto} ({pct_consumo_alto:.2f}% da amostra)")

# 5. Filtro Duplo: Consumo > 70% E Temperatura > Média
temp_media = df['Temperatura'].mean()
df_critico = df[(df[zona_maior_pico] > limiar_70) & (df['Temperatura'] > temp_media)]

qtd_critico = df_critico.shape[0]
pct_critico = (qtd_critico / total_amostra) * 100

print(f"\nTemperatura Média da Amostra: {temp_media:.2f} °C")
print(f"Registros com Consumo > 70% E Temp > Média: {qtd_critico} ({pct_critico:.2f}% da amostra)")

# 6. Resumo Comparativo
print("\n==================================================")
print("--- Comparação Final ---")
print("==================================================")
print(f"Apenas Consumo Elevado (>70%): {qtd_consumo_alto} registros")
print(f"Consumo Elevado + Temp > Média: {qtd_critico} registros")
print(f"Redução total: {qtd_consumo_alto - qtd_critico} registros a menos")