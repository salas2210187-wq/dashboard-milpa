import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------
st.set_page_config(
    page_title="Dashboard BI - Milpa Urbana",
    layout="wide"
)

# ---------------------------------------------------
# TÍTULO PRINCIPAL
# ---------------------------------------------------
st.title("🌱 Dashboard BI — Milpa Urbana en Zonas Industriales")

st.markdown("""
Sistema de monitoreo para indicadores ambientales, sociales y financieros
del Producto Mínimo Viable (PMV) del proyecto Milpa Urbana.
""")

st.markdown("---")

# ---------------------------------------------------
# TABS
# ---------------------------------------------------
tabs = st.tabs([
    "Resumen",
    "KPIs",
    "CAPEX",
    "Impacto Regional",
    "ODS 8",
    "Concentrado General"
])

# ---------------------------------------------------
# TAB 1 — RESUMEN
# ---------------------------------------------------

with tabs[0]:

    st.header("📋 Resumen")

    st.markdown("""
    El dashboard presenta indicadores relacionados con sostenibilidad,
    mitigación térmica, eficiencia social y validación del proyecto
    Milpa Urbana en Zonas Industriales.

    La propuesta busca reducir el impacto de las islas de calor urbanas
    mediante infraestructura verde y sistemas agroecológicos aplicados
    en zonas industriales de Tijuana.
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Reducción térmica",
        "4.2 °C"
    )

    col2.metric(
        "Trabajadores beneficiados",
        "140"
    )

    col3.metric(
        "Eficiencia social",
        "87%"
    )

# ---------------------------------------------------
# TAB 2 — KPIs
# ---------------------------------------------------

with tabs[1]:

    st.header("📊 KPIs y Eficiencia Social")

    st.markdown("""
    El indicador de eficiencia social integra variables de bienestar laboral,
    acceso a alimentos frescos y reducción del estrés térmico.
    """)

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=87,
        title={'text': "Eficiencia Social"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, 50], 'color': "#ffcccc"},
                {'range': [50, 75], 'color': "#fff4cc"},
                {'range': [75, 100], 'color': "#ccffcc"}
            ]
        }
    ))

    st.plotly_chart(
        fig_gauge,
        use_container_width=True
    )

# ---------------------------------------------------
# TAB 3 — CAPEX
# ---------------------------------------------------

with tabs[2]:

    st.header("💰 CAPEX y Validación")

    st.markdown("""
    La inversión inicial contempla infraestructura tecnológica,
    herramientas de monitoreo ambiental y recursos para validación
    del Producto Mínimo Viable (PMV).
    """)

    capex = pd.DataFrame({
        "Concepto": [
            "Licencias",
            "Software BI",
            "Sistema de riego",
            "Sensores ambientales",
            "Prototipo agrícola",
            "Validación en campo"
        ],
        "Costo": [
            8000,
            12000,
            15000,
            10000,
            18000,
            7000
        ]
    })

    fig_capex = px.bar(
        capex,
        x="Concepto",
        y="Costo",
        title="Distribución de inversión inicial",
        text_auto=True
    )

    st.plotly_chart(
        fig_capex,
        use_container_width=True
    )

# ---------------------------------------------------
# TAB 4 — IMPACTO REGIONAL
# ---------------------------------------------------

with tabs[3]:

    st.header("🌡️ Impacto Regional")

    st.markdown("""
    El mapa de calor representa el comportamiento térmico proyectado
    en las principales zonas industriales intervenidas.
    """)

    heat = pd.DataFrame({
        "Zona": [
            "Otay",
            "Florido",
            "Pacífico"
        ],
        "Temperatura Inicial": [
            38,
            37,
            36
        ],
        "Temperatura Final": [
            33,
            34,
            32
        ]
    })

    fig_heatmap = px.imshow(
        heat.set_index("Zona"),
        text_auto=True,
        aspect="auto",
        title="Comparación térmica por zona industrial"
    )

    st.plotly_chart(
        fig_heatmap,
        use_container_width=True
    )

# ---------------------------------------------------
# TAB 5 — ODS 8
# ---------------------------------------------------

with tabs[4]:

    st.header("🎯 Alineación con el ODS 8")

    st.markdown("""
    Los indicadores muestran cómo el proyecto contribuye al Objetivo
    de Desarrollo Sostenible 8 mediante bienestar laboral,
    sostenibilidad e innovación social.
    """)

    ods = pd.DataFrame({
        "Indicador": [
            "Bienestar laboral",
            "Reducción de estrés térmico",
            "Acceso a alimentos frescos",
            "Participación comunitaria"
        ],
        "Cumplimiento": [
            85,
            82,
            78,
            90
        ]
    })

    fig_ods = px.bar(
        ods,
        x="Indicador",
        y="Cumplimiento",
        title="Cumplimiento proyectado del ODS 8",
        text_auto=True
    )

    st.plotly_chart(
        fig_ods,
        use_container_width=True
    )

# ---------------------------------------------------
# TAB 6 — CONCENTRADO GENERAL
# ---------------------------------------------------

with tabs[5]:

    st.header("📌 Dashboard General")

    st.markdown("""
    Visualización estratégica consolidada de los indicadores
    financieros, ambientales y sociales del proyecto.
    """)

    st.markdown("---")


    # KPIs SUPERIORES

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            label="Eficiencia Social",
            value="87%"
        )

    with kpi2:
        st.metric(
            label="Reducción térmica",
            value="4.2 °C"
        )

    with kpi3:
        st.metric(
            label="Inversión PMV",
            value="$70,000"
        )

    with kpi4:
        st.metric(
            label="Impacto ODS 8",
            value="84%"
        )

    st.markdown("---")

    # FILA 1


    col1, col2 = st.columns([1, 2])

    # GAUGE
    with col1:

        st.subheader("Eficiencia Social")

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=87,
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, 50], 'color': "#ffcccc"},
                    {'range': [50, 75], 'color': "#fff4cc"},
                    {'range': [75, 100], 'color': "#ccffcc"}
                ]
            }
        ))

        st.plotly_chart(
            fig_gauge,
            use_container_width=True
        )

    # BARRAS CAPEX
    with col2:

        st.subheader("Distribución CAPEX")

        fig_capex = px.bar(
            capex,
            x="Concepto",
            y="Costo",
            text_auto=True,
            color="Costo"
        )

        st.plotly_chart(
            fig_capex,
            use_container_width=True
        )

    st.markdown("---")

    # FILA 2


    col3, col4 = st.columns([1.3, 1])

    # HEATMAP
    with col3:

        st.subheader("Impacto Regional")

        fig_heat = px.imshow(
            heat.set_index("Zona"),
            text_auto=True,
            aspect="auto",
            color_continuous_scale="Greens"
        )

        st.plotly_chart(
            fig_heat,
            use_container_width=True
        )

    # ODS
    with col4:

        st.subheader("ODS 8")

        fig_ods = px.bar(
            ods,
            x="Indicador",
            y="Cumplimiento",
            text_auto=True,
            color="Cumplimiento"
        )

        st.plotly_chart(
            fig_ods,
            use_container_width=True
        )

    st.markdown("---")

    st.success("Dashboard BI cargado correctamente")