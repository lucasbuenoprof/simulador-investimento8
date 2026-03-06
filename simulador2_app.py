import streamlit as st
import pandas as pd

# ----------------------------
# Título do app
# ----------------------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Simulador de Investimento 💰</h1>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# Entradas do usuário
# ----------------------------
st.subheader("Parâmetros do investimento")

aporte_inicial = st.number_input("Aporte Inicial (R$)", value=14000, step=100)
aporte_mensal = st.number_input("Aporte Mensal (R$)", value=1000, step=100)
rentabilidade_mensal = st.number_input("Rentabilidade Mensal (%)", value=1.0, step=0.1) / 100
meses = st.number_input("Número de Meses", value=12, step=1)

# ----------------------------
# Botão de cálculo
# ----------------------------
if st.button("Calcular"):
    
    acumulado = aporte_inicial
    juros_acumulados = 0
    resultado = []

    for mes in range(1, meses + 1):
        if mes == 1:
            juros_mes = 0
            acumulado += aporte_mensal
        else:
            juros_mes = acumulado * rentabilidade_mensal
            acumulado += aporte_mensal + juros_mes

        juros_acumulados += juros_mes

        resultado.append([
            mes,
            round(juros_mes, 2),
            round(acumulado, 2),
            round(juros_acumulados, 2)
        ])

    df = pd.DataFrame(
        resultado,
        columns=["Mês", "Juros", "Acumulado", "Juros Acumulado"]
    )

    # ----------------------------
    # Mostrar tabela
    # ----------------------------
    st.subheader("📊 Tabela de Evolução")
    st.dataframe(df)

# ----------------------------
# Rodapé
# ----------------------------
st.markdown("---")
st.markdown("Comece onde você está, use o que você tem e faça o que você pode. — Arthur Ashe 📚")
