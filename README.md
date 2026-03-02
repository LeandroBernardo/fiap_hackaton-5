# 🛡️ FIAP Security - AI Threat Modeling (MVP)

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Streamlit](https://img.shields.io/badge/frontend-streamlit-red.svg)
![OpenAI](https://img.shields.io/badge/AI-GPT--4o--mini-green.svg)

MVP (Minimum Viable Product) desenvolvido para o **Hackathon da Fase 5 da FIAP - Software Architecture**. Esta aplicação utiliza Inteligência Artificial Generativa e Visão Computacional para automatizar a modelagem de ameaças em arquiteturas de software, aplicando a metodologia **STRIDE**.

---

## 📑 Índice
1. [O Desafio](#-o-desafio)
2. [A Solução](#-a-solução)
3. [Arquitetura e Engenharia de Prompts](#-arquitetura-e-engenharia-de-prompts)
4. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
5. [Como Executar o Projeto](#-como-executar-o-projeto)
6. [Deploy em Produção](#-deploy-em-produção-streamlit-cloud)
7. [Estrutura de Diretórios](#-estrutura-de-diretórios)
8. [Exemplos de Uso](#-exemplos-de-uso)

---

## 🎯 O Desafio
A modelagem de ameaças tradicional é um processo manual, custoso e que exige especialistas em AppSec (Application Security). O desafio proposto pela FIAP consistiu em criar uma ferramenta que recebesse diagramas de arquitetura (AWS, Azure, GCP ou On-Premise) e, de forma automatizada, identificasse os componentes e listasse as potenciais vulnerabilidades de segurança utilizando o framework STRIDE.

---

## 💡 A Solução
Nossa ferramenta atua como um **Arquiteto de Segurança Cloud**. O usuário faz o upload de uma imagem contendo a topologia do sistema, e o motor de IA processa o diagrama para gerar um relatório unificado contendo:

- **Escopo e Premissas**: Mapeamento de zonas de confiança, perímetros de rede, processamento e persistência.
- **Matriz STRIDE**: Identificação detalhada de ameaças nas categorias:
    - **S**poofing (Falsificação de identidade)
    - **T**ampering (Adulteração de dados)
    - **R**epudiation (Repúdio)
    - **I**nformation Disclosure (Divulgação de informações)
    - **D**enial of Service (Negação de serviço)
    - **E**levation of Privilege (Elevação de privilégio)
- **Quick Risk Rating**: Resumo executivo dos riscos classificados por criticidade (Crítico, Alto, Médio, Baixo).
- **Contramedidas**: Recomendações acionáveis de mitigação (ex: mTLS, WAF tuning, RBAC, criptografia at-rest).

---

## 🧠 Arquitetura e Engenharia de Prompts
O diferencial deste MVP está na robustez da engenharia aplicada ao modelo LLM:

1. **Cloud Agnostic**: Os prompts foram desenhados para não dependerem de um provedor específico.
2. **Gatekeeper Anti-Alucinação**: Implementamos uma barreira de validação heurística para fotos não relacionadas a arquitetura.
3. **Mega Prompt Unificado**: Análise visual e STRIDE em uma única chamada de API.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.13+
- **Frontend**: Streamlit
- **Motor de IA**: OpenAI GPT-4o-mini
- **Gestão de Dependências**: Poetry

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.13+ e Poetry instalados.

### Passo a Passo (Execução Local)

1. **Clone o repositório:**
   git clone https://github.com/LeandroBernardo/fiap_hackaton-5.git
   cd fiap_hackaton-5

2. **Instale as dependências:**
   poetry install

3. **Configuração de Ambiente:**
   Crie um arquivo .env na raiz com sua chave:
   OPENAI_API_KEY=sk-proj-sua-chave-aqui

4. **Inicie a Aplicação:**
   poetry run streamlit run app/main.py

---

## ☁️ Deploy em Produção (Streamlit Cloud)
Configure em Settings > Secrets:
OPENAI_API_KEY = "chave_no_pdf"

---

## 📁 Estrutura de Diretórios
```text
fiap_hackaton-5/
├── app/
│   ├── main.py                # Interface Streamlit
│   ├── services/
│   │   └── openai_service.py  # Integração com API
│   └── prompts/
│       └── security_prompts.py # Engenharia de Prompts
├── .env_example               # Template de env
├── pyproject.toml             # Configurações Poetry
└── README.md                  # Documentação