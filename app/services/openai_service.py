from openai import OpenAI
import os
import base64
import io
from dotenv import load_dotenv
# Certifique-se de que os nomes dos arquivos e caminhos coincidem com sua estrutura
from prompts.security_prompts import ANALYSIS_PROMPT, STRIDE_PROMPT

load_dotenv()

class OpenAIService:
    def __init__(self):
        """
        Inicializa o cliente OpenAI utilizando a chave do arquivo .env.
        A classe foi projetada para ser resiliente e econômica.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")
        
        self.client = OpenAI(api_key=api_key)
        # Definimos o gpt-4o-mini como padrão para maximizar o uso do seu crédito de $5
        self.model_id = "gpt-4o-mini"

    def analyze_architecture(self, pil_image):
            try:
                # Mantemos um tamanho bom para leitura de ícones
                if pil_image.width > 1600 or pil_image.height > 1600:
                    pil_image.thumbnail((1600, 1600))

                buffered = io.BytesIO()
                pil_image.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

                # Ajuste no prompt para evitar gatilhos de recusa da IA
                context_prompt = (
                    "Você é um especialista em segurança cibernética analisando um diagrama de arquitetura de nuvem para fins acadêmicos e profissionais. "
                    "Por favor, identifique os componentes técnicos e realize a modelagem de ameaças STRIDE para os itens visíveis na imagem."
                )

                response = self.client.chat.completions.create(
                    model=self.model_id,
                    messages=[
                        {
                            "role": "system",
                            "content": context_prompt
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text", 
                                    "text": f"TAREFA 1: {ANALYSIS_PROMPT}\n\n---DIVISOR---\n\nTAREFA 2: {STRIDE_PROMPT}"
                                },
                                {
                                    "type": "image_url", 
                                    "image_url": {
                                        "url": f"data:image/png;base64,{img_str}",
                                        "detail": "auto" # 'auto' permite que a IA decida o nível de zoom necessário
                                    }
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
                
                return {"success": True, "analysis": "Análise Gerada:", "stride": full_content}
                
            except Exception as e:
                return {"success": False, "error": f"Erro na OpenAI: {str(e)}"}