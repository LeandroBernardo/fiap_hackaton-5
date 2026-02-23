ANALYSIS_PROMPT = """
[REGRA DE VALIDAÇÃO DE ENTRADA]
1. Avalie a imagem fornecida. Ela contém múltiplos ícones de serviços tecnológicos interconectados (por linhas, setas ou agrupamentos visuais) representando um fluxo de sistema?
2. Se a imagem for APENAS um logotipo isolado, uma tela de interface de usuário (UI), um painel de métricas (dashboard) ou texto puro, RESPONDA EXATAMENTE COM: "ERRO_VALIDACAO: A imagem fornecida não contém um diagrama de arquitetura de infraestrutura ou software válido." e encerre a análise.
3. Se for um diagrama válido (mesmo que com baixa resolução, desenhado à mão, inclinado ou misturando provedores), prossiga. NÃO invente componentes que não estejam visíveis.

[ANÁLISE DE ARQUITETURA]
Atue como um Arquiteto de Software Cloud Agnostic. Identifique os elementos visíveis na imagem, independentemente de serem AWS, Azure, GCP ou On-Premise, agrupando-os pelas seguintes categorias:

1. **Camada de Perímetro**: Serviços de borda, firewalls (WAF), balanceadores de carga, CDNs e gateways de API.
2. **Processamento e Lógica**: Componentes de computação (Serverless, Containers, VMs) e seus papéis (Handlers, Workers, Orquestradores).
3. **Persistência e Cache**: Bancos de dados (Relacionais e NoSQL), sistemas de busca e camadas de cache in-memory.
4. **Comunicação e Mensageria**: Fluxos assíncronos (Filas, Tópicos, Event Buses, Pub/Sub).
5. **Zonas de Confiança e Identidade**: Fronteiras de rede (VPCs, Subnets virtuais) e mecanismos de controle de acesso (IAM, IdP, Cognito, Entra ID).

Ao final, descreva sucintamente o fluxo de dados principal (ex: como uma requisição externa chega até a persistência de dados).
"""

STRIDE_PROMPT = """
[VALIDAÇÃO] Se a imagem não for um diagrama de arquitetura válido (apenas um logo ou tela sem conexões), responda APENAS "ERRO_VALIDACAO" e encerre.

[MODELAGEM STRIDE] Sendo um diagrama válido, utilize os componentes visíveis na imagem para aplicar a modelagem de ameaças (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).

Para cada letra do STRIDE, forneça ESTRITAMENTE o seguinte formato:
- **Alvo**: O componente específico da imagem mais vulnerável a essa ameaça.
- **Risco**: O vetor de ataque detalhado focado no fluxo de dados visível.
- **Severidade**: Baixa, Média ou Alta.
- **Mitigação**: Contramedida técnica recomendada aplicável à arquitetura (ex: mTLS, RBAC, WAF Tuning).
"""