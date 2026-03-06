import streamlit as st
import pandas as pd

# ----------------------------
# Configuração da página
# ----------------------------
st.set_page_config(
    page_title="Simulador de Investimento",
    page_icon="💰",
    layout="centered"
)

# ----------------------------
# Título
# ----------------------------
st.markdown("<h1 style='text-align:center; color:#2E8B57;'>💰 Simulador de Investimento</h1>", unsafe_allow_html=True)
st.markdown("Simule a evolução do seu investimento com aportes mensais e juros compostos.")
st.markdown("---")

# ----------------------------
# Entradas em colunas
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    aporte_inicial = st.number_input("Aporte Inicial (R$)", value=14000, step=100)

with col2:
    aporte_mensal = st.number_input("Aporte Mensal (R$)", value=1000, step=100)

col3, col4 = st.columns(2)

with col3:
    rentabilidade_mensal = st.number_input("Rentabilidade Mensal (%)", value=1.0, step=0.1) / 100

with col4:
    meses = st.number_input("Número de Meses", value=12, step=1)

st.markdown("")

# ----------------------------
# Botão
# ----------------------------
calcular = st.button("Calcular investimento")

# ----------------------------
# Cálculo
# ----------------------------
if calcular:

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
            juros_mes,
            acumulado,
            juros_acumulados
        ])

    df = pd.DataFrame(
        resultado,
        columns=["Mês", "Juros do Mês", "Total Acumulado", "Juros Acumulados"]
    )

    # ----------------------------
    # Métricas principais
    # ----------------------------
    st.markdown("### 📊 Resultado do investimento")

    total_aportado = aporte_inicial + (aporte_mensal * meses)
    patrimonio_final = acumulado

    m1, m2, m3 = st.columns(3)

    m1.metric("💵 Total Investido", f"R$ {total_aportado:,.2f}")
    m2.metric("💰 Juros Totais", f"R$ {juros_acumulados:,.2f}")
    m3.metric("🏦 Patrimônio Final", f"R$ {patrimonio_final:,.2f}")

    st.markdown("---")

    # ----------------------------
    # Formatar valores como moeda
    # ----------------------------
    df_formatado = df.copy()

    df_formatado["Juros do Mês"] = df_formatado["Juros do Mês"].map("R$ {:,.2f}".format)
    df_formatado["Total Acumulado"] = df_formatado["Total Acumulado"].map("R$ {:,.2f}".format)
    df_formatado["Juros Acumulados"] = df_formatado["Juros Acumulados"].map("R$ {:,.2f}".format)

    # ----------------------------
    # Tabela
    # ----------------------------
    st.subheader("📋 Evolução mês a mês")

    st.dataframe(
        df_formatado,
        use_container_width=True,
        hide_index=True
    )

# ----------------------------
# Rodapé
# ----------------------------
st.markdown("---")
st.markdown(
    "<center><i>Comece onde você está, use o que você tem e faça o que você pode. — Arthur Ashe 📚</i></center>",
    unsafe_allow_html=True
)
