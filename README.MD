**Projeto: Contador de Pessoas em Vídeo**

***Descrição:***

Uma aplicação web que permite ao usuário fazer o upload de um vídeo ou usar a câmera ao vico, e o sistema conta quantas pessoas passaram por determinado ponto da imagem
(como uma linha virtual em uma porta de entrada, por exemplo)


***Funcionalidades:***

1. Frontend (React):
    - Upload de vídeo
    - Botão para iniciar análise.
    - Visualização do vídeo com a contagem em tempo real
    - Dashboard simples mostrando:
        - Total de pessoas detectadas.
        - Gráfico com número de pessoas por minuto (usando chart.js ou recharts).
    - Exibição do vídeo processado com marcação(bounding boxes, linha de contagem, etc)
2.  Backend (Pyhton - Flask ou FastAPI):
    - Recebe o vídeo.
    - Usa OpenCV + modelo de detecção (pode começar com o cv2.HOGDescriptor() ou YOLO com ultralytics) para detectar pessoas.
    - Implementa lógica de linha virtual para contagem.
    - retorma
        - Total de pessoas.
        - Vídeo com anotações (pode ser por frames)
        - Dados estatísticos (timestamps, contagem parciais).
3.  Extras (opcional):
    - Suporte a câmera ao vivo.
    - Histórico de vídeos processados.
    - Detecção de direção (entrando ou saindo).

**Tecnologinas Sugeridas:**
    - Frontend: React, Axio, Recharts, Bootstrap ou Tailwind.
    - Backend: Python, Flask ou FastAPI, OpenCV, ultralytics (YOLOv8).
    - Integração: API REST para comunicação entre frontend e backend.
    - Armazenamento temporário: arquivos em /tmp ou uso de Redis se quiser escalar.

**Primeiros Passos:**

1. Crie a API com Flask para aceitar o vídeo e devolver JSON com as contagens.
2. No React, crie o formulário de upload e consuma a API
3. Faça a contagem de pessoas com lógica simples (linha no meio do frame + detecção)
4. Retorne os resultados e desenhe o gráfico