# 🛡️ FIAP Security - AI Threat Modeling (MVP)

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.42.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![Poetry](https://img.shields.io/badge/poetry-package%20manager-cyan)

Este repositório contém o MVP (Minimum Viable Product) desenvolvido para o **Hackathon da Fase 5 da FIAP - Software Architecture**. 

O objetivo da solução é automatizar a identificação de componentes de arquitetura de software e realizar a **Modelagem de Ameaças baseada no framework STRIDE** utilizando Inteligência Artificial Generativa com capacidade de Visão Computacional.

## 🎯 O Problema e a Solução

A modelagem de ameaças tradicional é um processo manual, demorado e que exige alto nível de especialização em AppSec. 
Nossa ferramenta otimiza este processo permitindo que arquitetos e desenvolvedores façam o upload de um diagrama de arquitetura (AWS, Azure, GCP ou On-Premise). O motor de IA analisa visualmente o diagrama e gera um relatório unificado contendo:

1. **Escopo e Premissas**: Identificação de perímetros, processamento, persistência e zonas de confiança.
2. **Matriz STRIDE**: Tabela detalhada com ameaças de Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service e Elevation of Privilege focadas nos componentes visíveis.
3. **Quick Risk Rating**: Resumo de riscos prioritários (Críticos a Baixos).
4. **Recomendações Arquiteturais**: Mitigações técnicas (ex: mTLS, WAF tuning, RBAC).

## ✨ Principais Funcionalidades (Features)

- **Cloud Agnostic**: O modelo foi treinado via *Prompt Engineering* para reconhecer ícones e padrões arquiteturais das principais nuvens do mercado, sem viés para um único provedor.
- **Gatekeeper Anti-Alucinação**: Implementação de restritores lógicos no prompt. Se a imagem enviada for apenas um logotipo, texto ou não apresentar uma topologia válida, o sistema aborta a análise elegantemente, evitando falsos positivos e economizando tokens.
- **Gestão Híbrida de Segredos**: O código suporta execução local segura (via `.env` isolado do controle de versão) e execução em nuvem (via `st.secrets` no Streamlit Cloud).

## 🛠️ Stack Tecnológico

- **Backend / Frontend**: [Python 3.13](https://www.python.org/) + [Streamlit](https://streamlit.io/)
- **Inteligência Artificial**: [OpenAI GPT-4o-mini](https://openai.com/) (Escolhido pelo excelente balanço entre precisão multimodal e eficiência de custos / FinOps).
- **Gestão de Dependências**: [Poetry](https://python-poetry.org/)

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.13 instalado.
- Poetry instalado na máquina (`pip install poetry`).
- Uma chave de API válida da OpenAI.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/LeandroBernardo/fiap_hackaton-5.git](https://github.com/LeandroBernardo/fiap_hackaton-5.git)
   cd fiap_hackaton-5