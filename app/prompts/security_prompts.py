ANALYSIS_PROMPT = """
Aja como um especialista em arquitetura de nuvem. Analise a imagem enviada e:
1. Identifique e liste todos os componentes (Ex: Usuários, WAF, API Gateway, Bancos de Dados, etc). [cite: 8]
2. Descreva o fluxo de dados entre esses componentes.
"""

STRIDE_PROMPT = """
Realize uma modelagem de ameaças rigorosa baseada na metodologia STRIDE para a arquitetura na imagem: [cite: 5, 10]
- S (Spoofing): Ameaças de falsificação de identidade.
- T (Tampering): Modificação não autorizada de dados.
- R (Repudiation): Negar a realização de uma ação.
- I (Information Disclosure): Vazamento de informações confidenciais.
- D (Denial of Service): Ataques de negação de serviço.
- E (Elevation of Privilege): Ganho de acesso privilegiado.

Para cada ameaça, identifique o componente vulnerável e sugira uma contramedida específica. [cite: 14]
"""