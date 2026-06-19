Weather Project

Pipeline de dados end-to-end que coleta dados meteorológicos em tempo real, armazena em banco de dados na nuvem e envia relatórios automáticos por email.

🏗️ Arquitetura

OpenWeather API
      ↓
Apache Airflow (Docker/Astronomer) — coleta a cada 2 min
      ↓
Supabase (PostgreSQL)
      ↓
Streamlit Dashboard
      ↓
Flask API + ngrok
      ↓
N8N → Email automático diário

🛠️ Stack

CamadaTecnologiaOrquestraçãoApache Airflow 3.x (Astronomer)ContainerizaçãoDockerBanco de dadosSupabase (PostgreSQL)DashboardStreamlit + PlotlyAutomaçãoN8N CloudExposiçãoFlask + ngrokLinguagemPython 3.12

📦 Estrutura do Projeto

AI Weather Project/
├── dags/
│   ├── weather_pipeline.py   # DAG do Airflow (ETL)
│   └── app.py                # Dashboard Streamlit
├── exports/                  # Imagens geradas para email
├── api.py                    # API Flask para exportação
├── screenshot.py             # Captura do dashboard
├── export.py                 # Exportação de gráficos
├── requirements.txt
├── Dockerfile
└── .env

⚙️ Como Rodar

Pré-requisitos


Docker Desktop
Astronomer CLI (astro)
Python 3.12
Conta Supabase
Conta OpenWeatherMap
ngrok


1. Clone o repositório

bashgit clone https://github.com/seu-usuario/ai-weather-project
cd ai-weather-project

2. Configure o .env

envOPENWEATHER_API_KEY=sua_chave
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=seu_host.supabase.com
DB_PORT=6543
DB_DBNAME=postgres

3. Suba o Airflow

powershellastro dev start

Acesse: http://localhost:8080 (admin/admin)

4. Rode o Dashboard

powershellstreamlit run dags/app.py

Acesse: http://localhost:8501

5. Rode a API de exportação

powershellpython api.py
ngrok http 5000

6. Configure o N8N


Cron Trigger → HTTP Request (/export) → Gmail


🔄 Pipeline ETL

Extract → Coleta dados da API OpenWeatherMap (temperatura, umidade, pressão, vento)

Transform → Normaliza os dados, converte Kelvin para Celsius, adiciona timestamps

Load → Insere no Supabase com schema dedicado (weather.weather_data)

📊 Dashboard


Temperatura atual e sensação térmica
Condição climática com ícone
Gráfico de umidade por hora
Métricas de vento e pressão
Auto-refresh a cada 2 minutos


📧 Automação de Email

Todos os dias um relatório com screenshot do dashboard é enviado automaticamente via N8N + Gmail.

📝 Licença

MIT