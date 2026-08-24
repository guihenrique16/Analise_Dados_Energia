import pandas as pd

# 1. Carregar os dados
# Certifique-se de que o arquivo 'SAMPLE_ENERGY_DATA.csv' esteja na mesma pasta deste arquivo .py
caminho_arquivo = 'SAMPLE_ENERGY_DATA.csv'
dados = pd.read_csv(caminho_arquivo)

print("--- Tipo do objeto ---")
print(type(dados))

print("\n--- Primeiros Registros ---")
print(dados.head())

print("\n--- Dimensões (Linhas, Colunas) ---")
print(dados.shape)
print(f"Total de linhas: {dados.shape[0]}")

print("\n--- Informações dos Atributos ---")
dados.info()  # .info() já imprime diretamente na tela

print("\n--- Estatísticas Descritivas ---")
print(dados.describe())

print("\n--- Rótulos das Colunas Originais ---")
print(dados.columns)

# 2. Renomear colunas
dados.rename(columns={
    'Date': 'Data',
    'Time': 'Hora',
    'Global_active_power': 'Potencia_Ativa',
    'Global_reactive_power': 'Potencia_Reativa',
    'Voltage': 'Tensao',
    'Global_intensity': 'Corrente',
    'Sub_metering_1': 'Consumo_1',
    'Sub_metering_2': 'Consumo_2',
    'Sub_metering_3': 'Consumo_3'
}, inplace=True)

print("\n--- Novas Colunas ---")
print(dados.columns)

# 3. Criar variações do DataFrame
df1 = dados.drop(columns=['Data', 'Hora'])
print("\n--- df1 (Sem Data e Hora) ---")
print(df1.head())

tensao = dados['Tensao']
print("\n--- Tipo da variável 'tensao' ---")
print(type(tensao))

df2 = dados[['Tensao', 'Corrente']]
print("\n--- df2 (Tensão e Corrente) ---")
print(df2.head())

df3 = dados.iloc[:, 0:4]
print("\n--- df3 (Primeiras 4 colunas) ---")
print(df3.head())

# 4. Análise da Demanda Máxima
PMAX = dados['Potencia_Ativa'].max()
print(f'\nA demanda máxima de potência é: {PMAX:.2f} kW')

P70 = 0.7 * PMAX
print(f'O limiar de 70% da demanda máxima é: {P70:.2f} kW')

df4 = dados[['Tensao', 'Corrente', 'Potencia_Ativa', 'Potencia_Reativa']]
df5 = df4[df4['Potencia_Ativa'] > P70]

print("\n--- Registros acima do limiar de 70% ---")
print(df5.head())

print(f'\nForam encontrados {df5.shape[0]} registros/consumidores com demanda energética acima de 70% de PMAX.')