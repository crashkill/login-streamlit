"""
Sistema de Login com Autenticação Local e Supabase

Este módulo implementa uma interface de login segura com duas opções de autenticação:
1. Local: Utiliza credenciais armazenadas no arquivo config.toml
2. Supabase: Utiliza autenticação via serviço Supabase

Características:
- Interface moderna e responsiva
- Animação Lottie para melhor experiência do usuário
- Validação de credenciais
- Redirecionamento após login bem-sucedido
- Suporte a múltiplos métodos de autenticação

Credenciais de exemplo:
Local:
- Usuário: admin, Senha: admin123
- Usuário: user, Senha: user123

Configuração:
As credenciais locais são armazenadas em .streamlit/config.toml
"""

import streamlit as st
import toml
from supabase import create_client, Client
import os
from streamlit_extras.switch_page_button import switch_page
import base64
from streamlit_lottie import st_lottie
import requests

# Função para carregar animação Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Login",
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

# CSS personalizado
st.markdown("""
<style>
    /* Estilos para o input e sua div container */
    div[data-baseweb="base-input"] {
        background-color: #F9FAFB !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 0.5rem !important;
        margin-bottom: 1rem !important;
        transition: all 0.2s ease-in-out !important;
        height: 42px !important;
        display: flex !important;
        align-items: center !important;
    }

    div[data-baseweb="base-input"]:focus-within {
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }

    div[data-baseweb="base-input"] input {
        background-color: transparent !important;
        border: none !important;
        height: 100% !important;
        padding: 0 1rem !important;
        font-size: 1rem !important;
        color: #111827 !important;
        width: 100% !important;
        line-height: 42px !important;
    }

    div[data-baseweb="base-input"] input:focus {
        box-shadow: none !important;
        outline: none !important;
    }

    div[data-baseweb="base-input"] input::placeholder {
        color: #9CA3AF !important;
        line-height: 42px !important;
    }

    /* Estilos do botão */
    .stButton>button {
        width: 100%;
        background-color: #4F46E5;
        color: white;
        border-radius: 0.375rem;
        padding: 0.75rem 1rem;
        border: none;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        background-color: #4338CA;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    /* Container centralizado */
    .centered-container {
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: white;
        border-radius: 1rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }

    /* Estilo para o radio button */
    .stRadio>div {
        background-color: #F9FAFB;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    }

    /* Título e subtítulo */
    h1 {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #111827;
        margin-bottom: 1rem !important;
        text-align: center;
    }
    .subtitle {
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }

    /* Form container */
    .form-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }

    /* Labels dos inputs */
    .stTextInput>label {
        color: #374151 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Configurações do Supabase
supabase_client = create_client(
    supabase_url=st.secrets["SUPABASE_URL"],
    supabase_key=st.secrets["SUPABASE_KEY"]
)

# Função para carregar usuários do arquivo TOML
def load_users():
    try:
        config = toml.load(".streamlit/config.toml")
        return config.get("credentials", {}).get("users", [])
    except:
        return []

# Função para verificar credenciais locais
def check_local_credentials(username, password):
    users = load_users()
    return any(
        user["username"] == username and user["password"] == password
        for user in users
    )

# Função para verificar credenciais no Supabase
def check_supabase_credentials(email, password):
    try:
        res = supabase_client.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return True if res.user else False
    except Exception as e:
        st.error(f"Erro ao autenticar com Supabase: {str(e)}")
        return False

# Interface do usuário
st.markdown('<div class="centered-container">', unsafe_allow_html=True)

# Carregar e exibir a animação Lottie
lottie_url = "https://assets3.lottiefiles.com/packages/lf20_06a6pf9i.json"
lottie_animation = load_lottieurl(lottie_url)

if lottie_animation is not None:
    st_lottie(
        lottie_animation,
        height=180,
        key="financial_animation"
    )

st.title("🔐 Login")
st.markdown('<p class="subtitle">Faça login para acessar o sistema</p>', unsafe_allow_html=True)

# Tabs para escolher o método de autenticação
auth_method = st.radio("Escolha o método de autenticação:", ["Local", "Supabase"], horizontal=True)

if auth_method == "Local":
    with st.form("login_form_local", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        username = st.text_input("👤 Usuário", placeholder="Digite seu usuário")
        password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")
        submit = st.form_submit_button("Entrar")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submit:
            if check_local_credentials(username, password):
                st.session_state["authenticated"] = True
                st.success("Login realizado com sucesso!")
                switch_page("home")
            else:
                st.error("Credenciais inválidas!")

else:
    with st.form("login_form_supabase", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        email = st.text_input("📧 E-mail", placeholder="Digite seu e-mail")
        password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")
        submit = st.form_submit_button("Entrar")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submit:
            if check_supabase_credentials(email, password):
                st.session_state["authenticated"] = True
                st.success("Login realizado com sucesso!")
                switch_page("home")
            else:
                st.error("Credenciais inválidas!")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style='position: fixed; bottom: 0; left: 0; right: 0; text-align: center; padding: 1rem; background-color: #F9FAFB; border-top: 1px solid #E5E7EB;'>
    <p style='color: #6B7280; font-size: 0.875rem;'> 2024 Seu Sistema. Todos os direitos reservados.</p>
</div>
""", unsafe_allow_html=True)
