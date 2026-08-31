# Análise de Dados de Energia

Projeto acadêmico desenvolvido na disciplina **Soluções em Energias Renováveis e Sustentáveis**, do curso de **Ciência da Computação**.

O objetivo da atividade é aplicar técnicas de preparação, inspeção, filtragem, análise estatística e interpretação de dados em diferentes contextos do setor energético, utilizando **Python, Pandas, Google Colab e Orange Data Mining**.

O trabalho foi dividido em duas partes principais:

1. **Desafio Final — Análise de carga elétrica com API pública do ONS**
2. **Análise de diferentes datasets do setor de energia**

---

## Parte 1 — Análise de carga elétrica do ONS

O notebook `CP4_Desafio_Final_Energia_ONS_API_Final.ipynb` realiza uma análise de dados reais de carga elétrica da região de **São Paulo (SP)**, obtidos por meio da API pública do **Operador Nacional do Sistema Elétrico (ONS)**.

### Principais etapas

- consulta à API pública do ONS;
- criação e inspeção do DataFrame;
- organização e tratamento dos dados;
- cálculo de carga mínima, máxima, média e mediana;
- identificação de períodos de alta demanda;
- criação de DataFrames derivados;
- cálculo de percentuais;
- construção de gráficos;
- análise do comportamento da carga;
- síntese dos resultados;
- elaboração e validação crítica de relatório técnico.

### Fonte dos dados

- **ONS — Carga de Energia Verificada:**  
  https://dados.ons.org.br/dataset/carga-energia-verificada

- **Portal de Dados Abertos do ONS:**  
  https://dados.ons.org.br/

---

## Parte 2 — Análise de datasets de energia

A segunda parte da atividade utiliza seis conjuntos de dados relacionados a consumo e geração de energia.

O objetivo é realizar inspeção, preparação, criação de filtros, cálculo de indicadores e interpretação dos resultados utilizando Python e Pandas.

| Dataset | Contexto | Fonte |
|---|---|---|
| **Appliances Energy Prediction** | Consumo de eletrodomésticos associado a temperatura, umidade e condições ambientais | UCI Machine Learning Repository |
| **Steel Industry Energy Consumption** | Consumo energético de uma indústria siderúrgica, potência reativa, fator de potência e classificação de carga | UCI Machine Learning Repository |
| **Power Consumption of Tetouan City** | Consumo elétrico de três zonas de Tétouan associado a variáveis meteorológicas | UCI Machine Learning Repository |
| **Solar Power Generation Data** | Dados de geração e inversores de usinas fotovoltaicas | Kaggle |
| **Wind & Solar Energy Production Dataset** | Comparação entre geração solar e geração eólica | Kaggle |
| **Individual Household Electric Power Consumption** | Consumo elétrico residencial, tensão, corrente, potência ativa, potência reativa e submedições | UCI Machine Learning Repository |

---

## Fontes dos datasets

### 1. Appliances Energy Prediction

UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction

---

### 2. Steel Industry Energy Consumption

UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption

---

### 3. Power Consumption of Tetouan City

UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/849/power+consumption+of+tetouan+city

---

### 4. Solar Power Generation Data

Kaggle

https://www.kaggle.com/datasets/anikannal/solar-power-generation-data

---

### 5. Wind & Solar Energy Production Dataset

Kaggle

https://www.kaggle.com/datasets/ahmeduzaki/wind-and-solar-energy-production-dataset

---

### 6. Individual Household Electric Power Consumption

UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption

---

## Estrutura do repositório

```text
Analise_Dados_Energia/
│
├── CP4_Desafio_Final_Energia_ONS_API_Final.ipynb
│
├── Appliances_EnergyPrediction/
├── SteelIndustry_EnergyConsumption/
├── TetouanCity_PowerConsumption/
├── SolarPower_GenerationData/
├── WindAndSolar_EnergyProduction/
├── HouseHold_EletricPowerConsumption/
└── Aula_AnaliseDeDados/
