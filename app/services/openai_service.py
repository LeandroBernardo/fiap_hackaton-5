import os
import io
import base64
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from prompts.security_prompts import ANALYSIS_PROMPT, STRIDE_PROMPT

# Carrega o .env apenas para execução local
load_dotenv()

class OpenAIService:
    def __init__(self):
            """
            Inicialização resiliente para rodar Local e na Nuvem sem erros.
            """
            api_key = None

            # 1. Tenta buscar nos Secrets do Streamlit (Nuvem)
            try:
                if "OPENAI_API_KEY" in st.secrets:
                    api_key = st.secrets["OPENAI_API_KEY"]
            except Exception:
                # Se der erro de "No secrets found" (Local), apenas ignora e segue
                pass

            # 2. Se não encontrou no Streamlit, busca no .env (Local)
            if not api_key:
                api_key = os.getenv("OPENAI_API_KEY")

            if not api_key:
                raise ValueError("Erro: OPENAI_API_KEY não configurada no .env ou Streamlit Secrets.")

            self.client = OpenAI(api_key=api_key)
            self.model_id = "gpt-4o-mini"

    def analyze_architecture(self, pil_image):
        try:
            # Otimização de imagem para custo e visão
            if pil_image.width > 1600 or pil_image.height > 1600:
                pil_image.thumbnail((1600, 1600))

            buffered = io.BytesIO()
            pil_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

            # Contexto Sênior para desarmar filtros de segurança da IA
            system_msg = (
                "Você é um Especialista em Segurança Cibernética Sênior. "
                "Sua tarefa é analisar diagramas de arquitetura técnica para fins de "
                "auditoria e modelagem de ameaças profissional."
            )

            response = self.client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "system", "content": system_msg},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": f"TAREFA 1: {ANALYSIS_PROMPT}\n\n---DIVISOR---\n\nTAREFA 2: {STRIDE_PROMPT}"},
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/png;base64,{img_str}", "detail": "auto"}
                            }
                        ],
                    }
                ],
                max_tokens=2500,
                temperature=0.1
            )

            full_content = response.choices[0].message.content
            
            if "---DIVISOR---" in full_content:
                parts = full_content.split("---DIVISOR---")
                return {"success": True, "analysis": parts[0].strip(), "stride": parts[1].strip()}
            
            return {"success": True, "analysis": "Relatório Gerado:", "stride": full_content}
            
        except Exception as e:
            return {"success": False, "error": f"Erro técnico: {str(e)}"}