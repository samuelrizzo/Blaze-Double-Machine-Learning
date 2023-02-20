# Bot para sinais da Blaze Double

Script para ler os últimos resultados da blaze, verificar se bate com a estratégia e enviar sinal no Telegram.
## Instalação

Use o GIT para clonar o repositório:
```bash
git clone https://github.com/samuelrizzo/Blaze-Double-Machine-Learning
```
Crie o ambiente virtual com o Python
```bash
python -m venv venv - para Windows
python3 -m venv venv - para Linux
```

Ative o ambiente virtual com:
```bash
source venv/bin/activate - para Linux

cd venv/bin
activate
para Windows
```
Instale os requerimentos com o pip

```bash
pip install -r requirements.txt
```

## Utilização:

```bash
python3 prediction.py - para Linux
python prediction.py - para Windows
```

Você pode adicionar mais padrões e alterar a mensagem para ser enviada
#### Arquivo .env:

```bash
BLAZE_API_URL=https://blaze.com/api/roulette_games/recent
```
