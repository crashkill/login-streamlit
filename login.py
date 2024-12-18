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
import time
from streamlit_extras.switch_page_button import switch_page
import base64
from streamlit_lottie import st_lottie
import requests
import bcrypt

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
    body {
        font-family: 'Arial', sans-serif;
    }
    .error-message {
        color: red;
        font-weight: bold;
    }
    .loading-indicator {
        display: none;
        text-align: center;
        margin: 1rem 0;
    }
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
    .stButton>button {
        width: 100%;
        height: 42px;
        background-color: #4F46E5 !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        background-color: #4338CA !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .form-container {
        padding: 1rem;
        background-color: white;
        border-radius: 1rem;
    }
    .title-container {
        text-align: center !important;
        margin: 0 auto 2rem auto !important;
        max-width: 800px !important;
    }
    .title-container h1 {
        text-align: center !important;
        margin: 0 auto !important;
        display: block !important;
    }
    .main-content {
        max-width: 1200px !important;
        margin: 0 auto !important;
        padding: 0 2rem !important;
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

login_attempts = {}  # Inicializa o dicionário para rastrear tentativas de login

def register_user(username, password):
    """Registra um novo usuário e armazena suas credenciais."""
    store_user_credentials(username, password)
    st.success("Usuário registrado com sucesso!")

# Função para re-hash as senhas existentes
def rehash_existing_passwords():
    config = toml.load(".streamlit/config.toml")
    users = config.get("credentials", {}).get("users", [])
    for user in users:
        if not user["password"].startswith("$2b$"):  # Se a senha não estiver hashada
            user["password"] = bcrypt.hashpw(user["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    config["credentials"]["users"] = users
    with open(".streamlit/config.toml", "w") as f:
        toml.dump(config, f)

# Chama a função para re-hash as senhas existentes ao iniciar o script
rehash_existing_passwords()

# Função para verificar credenciais locais e Supabase
def authenticate_user(method, username=None, email=None, password=None):
    global login_attempts
    current_time = time.time()
    
    # Limitação de taxa
    if username in login_attempts:
        if login_attempts[username]['count'] >= 5 and (current_time - login_attempts[username]['timestamp'] < 300):
            st.error("Muitas tentativas de login. Tente novamente mais tarde.")
            return False
        else:
            login_attempts[username]['count'] += 1
    else:
        login_attempts[username] = {'count': 1, 'timestamp': current_time}
    
    if method == "Local":
        users = load_users()
        for user in users:
            if user["username"] == username:
                if user["password"] is not None and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
                    return True
                else:
                    st.error("Senha incorreta!")
                    return False
        st.error("Usuário não encontrado!")
        return False
    elif method == "Supabase":
        return check_supabase_credentials(email, password)

# Função para armazenar credenciais locais
def store_user_credentials(username, password):
    # Verifica se a senha já está hashada
    if not password.startswith("$2b$"):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    else:
        hashed = password.encode('utf-8')  # Mantém a senha já hashada
    try:
        config = toml.load(".streamlit/config.toml")
        users = config.get("credentials", {}).get("users", [])
        users.append({"username": username, "password": hashed.decode('utf-8')})
        config["credentials"]["users"] = users
        with open(".streamlit/config.toml", "w") as f:
            toml.dump(config, f)
    except Exception as e:
        st.error(f"Erro ao armazenar credenciais: {str(e)}")

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
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Container para centralizar o título
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.title("🔐 Login")
st.markdown('</div>', unsafe_allow_html=True)

# Create two columns for the main content
col1, col2 = st.columns([1, 1])

with col1:
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
                if username and password:
                    if authenticate_user("Local", username=username, password=password):
                        st.session_state["authenticated"] = True
                        st.success("Login realizado com sucesso!")
                        switch_page("home")
                    else:
                        st.error("Credenciais inválidas!")
                else:
                    st.error("Por favor, preencha todos os campos.")

    else:
        with st.form("login_form_supabase", clear_on_submit=True):
            st.markdown('<div class="form-container">', unsafe_allow_html=True)
            email = st.text_input("📧 E-mail", placeholder="Digite seu e-mail")
            password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")
            submit = st.form_submit_button("Entrar")
            st.markdown('</div>', unsafe_allow_html=True)
            
            if submit:
                if email and password:
                    if authenticate_user("Supabase", email=email, password=password):
                        st.session_state["authenticated"] = True
                        st.success("Login realizado com sucesso!")
                        switch_page("home")
                    else:
                        st.error("Credenciais inválidas!")
                else:
                    st.error("Por favor, preencha todos os campos.")

        # Adicionar botão "Esqueci minha senha"
        st.markdown("<a href='#' style='color: #4F46E5;'>Esqueci minha senha</a>", unsafe_allow_html=True)

with col2:
    # Add some vertical spacing to align with the form
    st.markdown("<div style='padding-top: 3.5rem;'></div>", unsafe_allow_html=True)
    
    # Carregar e exibir a animação Lottie
    lottie_url = "https://assets3.lottiefiles.com/packages/lf20_06a6pf9i.json"
    lottie_animation = load_lottieurl(lottie_url)

    if lottie_animation is not None:
        st_lottie(
            lottie_animation,
            height=250,
            key="financial_animation"
        )

st.markdown('</div>', unsafe_allow_html=True)  # Close main-content div
