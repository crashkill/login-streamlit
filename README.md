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
git clone [URL_DO_REPOSITÓRIO]
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas:
- streamlit
- supabase
- streamlit_lottie
- streamlit_extras
- toml
- requests

## ⚙️ Configuração

1. Configure o arquivo `.streamlit/config.toml` com as credenciais locais:
```toml
[credentials]
[[credentials.users]]
username = "admin"
password = "admin123"

[[credentials.users]]
username = "user"
password = "user123"
```

2. Configure o Supabase (opcional):
   - URL: https://zgdmuerecyrbcjbarltn.supabase.co
   - Configure suas credenciais no Supabase

## 🎨 Características do Design

- Layout moderno e centralizado
- Campos de entrada com ícones intuitivos
- Animação Lottie para melhor experiência do usuário
- Feedback visual para ações do usuário
- Design responsivo para diferentes tamanhos de tela
- Temas claros com suporte a personalização

## 🚀 Executando o projeto

Para iniciar o aplicativo, execute:
```bash
streamlit run login.py
```

## 🛠️ Estrutura do Projeto

```
├── .streamlit/          # Configurações do Streamlit e credenciais
│   └── config.toml     # Configurações de tema e usuários
├── pages/              # Páginas adicionais do aplicativo
├── login.py           # Página principal de login
└── README.md         # Documentação
```

## 🔒 Segurança

- Múltiplos métodos de autenticação
- Credenciais locais armazenadas em arquivo seguro
- Integração com Supabase para autenticação robusta
- Proteção contra acesso não autorizado
- Sessões gerenciadas pelo Streamlit

## 🎯 Recursos da Interface

- Campos de entrada estilizados
- Botões com efeitos hover
- Mensagens de feedback claras
- Animação de carregamento
- Layout responsivo e adaptável
- Navegação intuitiva

## 👥 Credenciais de Exemplo

### Local
- Usuário: admin / Senha: admin123
- Usuário: user / Senha: user123

### Supabase
- Use suas credenciais do Supabase

## 📞 Suporte

Para suporte, entre em contato através de:
- Email: [seu-email]
- Issue no repositório

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
