# Sistema de Login com Streamlit e Supabase

Sistema moderno de autenticação com suporte a múltiplos métodos de login, desenvolvido com Streamlit e integrado ao Supabase.

## 🚀 Funcionalidades

- Autenticação Local e Supabase
- Interface moderna com animações Lottie
- Design responsivo e intuitivo
- Validação de credenciais em tempo real
- Sistema de gerenciamento de sessão
- Redirecionamento pós-login
- Suporte a múltiplos usuários

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/crashkill/login-streamlit.git
cd login-streamlit
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

1. Configure o Streamlit:
   - Copie `.streamlit/config.toml.example` para `.streamlit/config.toml`
   - Ajuste as configurações e credenciais locais conforme necessário

2. Configure o Supabase:
   - Copie `.streamlit/secrets.toml.example` para `.streamlit/secrets.toml`
   - Adicione suas credenciais do Supabase no arquivo `secrets.toml`

### Exemplo de config.toml
```toml
[theme]
primaryColor = "#4F46E5"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[credentials]
[[credentials.users]]
username = "seu_usuario"
password = "sua_senha"
```

### Exemplo de secrets.toml
```toml
SUPABASE_URL = "sua_url_do_supabase"
SUPABASE_KEY = "sua_chave_do_supabase"
```

## 🚀 Executando o projeto

Para iniciar o aplicativo, execute:
```bash
streamlit run login.py
```

## 🛠️ Estrutura do Projeto

```
├── .streamlit/
│   ├── config.toml.example    # Exemplo de configuração do Streamlit
│   └── secrets.toml.example   # Exemplo de configuração do Supabase
├── pages/                     # Páginas adicionais do aplicativo
├── login.py                   # Página principal de login
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação
```

## 🔒 Segurança

- Múltiplos métodos de autenticação
- Credenciais armazenadas em arquivos seguros
- Integração com Supabase para autenticação robusta
- Proteção contra acesso não autorizado
- Sessões gerenciadas pelo Streamlit

## 🎯 Recursos da Interface

- Campos de entrada estilizados com ícones
- Botões com efeitos hover
- Mensagens de feedback claras
- Animação de carregamento
- Layout responsivo e adaptável
- Navegação intuitiva

## 📝 Notas Importantes

- Nunca compartilhe seus arquivos `config.toml` e `secrets.toml`
- Mantenha suas credenciais do Supabase seguras
- Use senhas fortes para usuários locais
- Faça backup regular das configurações

## 📞 Suporte

Para suporte:
- Abra uma issue no repositório
- Entre em contato através do GitHub

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
