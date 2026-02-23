import streamlit as st
from PIL import Image
# Agora o import faz sentido técnico
from services.openai_service import OpenAIService

st.set_page_config(page_title="FIAP Security - AI Modelagem", layout="wide", page_icon="🛡️")

# CSS para o estilo "Telegram/Chat"
st.markdown("""
    <style>
    .chat-bubble {
        background-color: #262730;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #464b5d;
        color: #ffffff;
    }
    .label { color: #00f2ff; font-weight: bold; margin-bottom: 10px; font-size: 1.1em; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Análise Supervisionada de Ameaças")
st.write("MVP para validação de modelagem de ameaças utilizando IA - Hackaton 5 -FIAP.")

uploaded_file = st.file_uploader("Faça o upload do Diagrama de Arquitetura", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Arquitetura para Análise", width=600)
    
    if st.button("🚀 Gerar Relatórios"):
        # Mensagem atualizada para refletir o uso da OpenAI
        with st.spinner("Analisando a arquitetura e gerando o relatório STRIDE..."):
            try:
                # Instancia o serviço que configuramos com a API Key paga
                service = OpenAIService() 
                result = service.analyze_architecture(img)
                
                if result["success"]:
                    # Caixa 1: Análise de Componentes (Requisito do MVP)
                    st.markdown('<div class="chat-bubble">', unsafe_allow_html=True)
                    st.markdown('<div class="label">🔍 COMPONENTES E ARQUITETURA</div>', unsafe_allow_html=True)
                    st.markdown(result["analysis"])
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Caixa 2: Relatório STRIDE (Requisito do MVP)
                    st.markdown('<div class="chat-bubble">', unsafe_allow_html=True)
                    st.markdown('<div class="label">📊 RELATÓRIO STRIDE & CONTRAMEDIDAS</div>', unsafe_allow_html=True)
                    st.markdown(result["stride"])
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.success("Análise concluída com sucesso!")
                else:
                    st.error(f"Erro no processamento: {result['error']}")
            except Exception as e:
                st.error(f"Erro crítico na aplicação: {str(e)}")

