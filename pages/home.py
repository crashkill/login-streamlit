import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.runtime.runtime import Runtime

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Home",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ocultar menu hamburguer e rodapé
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    header {visibility: hidden;}
    #stDecoration {display:none}
</style>
""", unsafe_allow_html=True)

# Verificar autenticação
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Por favor, faça login para acessar esta página")
    st.stop()

# CSS personalizado
st.markdown("""
<style>
    /* Tailwind-inspired styles */
    .stButton>button {
        background-color: #EF4444;
        color: white;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #DC2626;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .home-container {
        max-width: 800px;
        margin: auto;
        padding: 2rem;
    }
    .welcome-card {
        background-color: white;
        border-radius: 1rem;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }
    .stat-card {
        background-color: #F3F4F6;
        border-radius: 0.5rem;
        padding: 1.5rem;
        text-align: center;
    }
    .stat-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: #4F46E5;
        margin-bottom: 0.5rem;
    }
    .stat-label {
        color: #6B7280;
        font-size: 0.875rem;
    }
</style>
""", unsafe_allow_html=True)

# Interface do usuário
st.markdown('<div class="home-container">', unsafe_allow_html=True)

# Card de boas-vindas
st.markdown("""
<div class="welcome-card">
    <h1 style='font-size: 2rem; font-weight: 700; color: #111827; margin-bottom: 1rem;'>
        🏠 Bem-vindo ao Sistema
    </h1>
    <p style='color: #6B7280; font-size: 1.1rem;'>
        Este é o seu painel de controle. Aqui você pode gerenciar todas as suas atividades.
    </p>
</div>
""", unsafe_allow_html=True)

# Grid de estatísticas
st.markdown("""
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-value">150</div>
        <div class="stat-label">Usuários Ativos</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">85%</div>
        <div class="stat-label">Taxa de Sucesso</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">24/7</div>
        <div class="stat-label">Disponibilidade</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Seção de ações rápidas
st.markdown("""
<h2 style='font-size: 1.5rem; font-weight: 600; color: #111827; margin: 2rem 0 1rem;'>
    ⚡ Ações Rápidas
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.button("📊 Ver Relatórios")
with col2:
    st.button("👥 Gerenciar Usuários")
with col3:
    st.button("⚙️ Configurações")

# Botão de logout
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚪 Logout"):
    st.session_state["authenticated"] = False
    st.switch_page("login.py")

st.markdown('</div>', unsafe_allow_html=True)
