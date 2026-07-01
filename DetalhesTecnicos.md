# ConectaConcursos RS: Dashboard Analítico de Concursos Públicos

Este documento define o escopo, a arquitetura e as especificações técnicas para o desenvolvimento de uma plataforma analítica voltada ao monitoramento de concursos públicos no estado do Rio Grande do Sul, com foco especial na região de Porto Alegre e municípios adjacentes.



## 1. Visão Geral e Objetivo
O objetivo principal do projeto é consolidar, estruturar e analisar dados de editais de concursos públicos. A plataforma automatiza a recolha de dados que frequentemente estão espalhados em múltiplos portais de bancas organizadoras, extrai informações cruciais (prazos, salários, cargos) e apresenta insights estatísticos interativos para ajudar os candidatos a tomarem decisões informadas.



## 2. Funcionalidades Principais

### Fase 1: MVP (Produto Mínimo Viável)
* **Web Scraping Automatizado:** Recolha periódica de editais de portais oficiais e principais bancas da região sul (ex: Fundatec, FAURGS, Objetiva).
* **Pipeline de Extração de Dados:** Processamento de textos brutos dos editais usando Expressões Regulares (Regex) em Python para capturar:
    * Salário inicial e benefícios.
    * Carga horária e nível de escolaridade exigido.
    * Período de inscrições e data da prova escrita.
* **API RESTful:** Disponibilização dos dados limpos e estruturados via endpoints HTTP.
* **Painel Visual (Dashboard):**
    * *Métricas de Destaque (KPIs):* Total de vagas abertas, maior salário disponível, inscrições que encerram na semana.
    * *Gráficos Interativos:* Média salarial por área (TI, Administração, Saúde, Educação), distribuição de vagas por nível de escolaridade.
    * *Busca Avançada:* Tabela interativa com paginação, filtros por palavra-chave, faixa salarial e município.

### Fase 2: Expansão (Opcional)
* **Notificações via Telegram:** Bot que alerta o utilizador quando um novo edital contendo palavras-chave específicas (ex: "Ciência da Computação", "Analista") for publicado.


## 3. Arquitetura do Sistema

O sistema adota uma arquitetura clássica desacoplada (Decoupled Architecture), separando a camada de processamento e persistência da camada de apresentação.

```text
┌────────────────────────────────────────────────────────┐
│                   Camada de Recolha                    │
│   (Scripts Python / Scrapers -> Agendamento Cron)      │
└───────────────────────────┬────────────────────────────┘
                            │ (JSON / Dicionários)
                            ▼
┌────────────────────────────────────────────────────────┐
│                   Backend (API)                        │
│   (Python + FastAPI / Flask + SQLAlchemy / Postgres)   │
└───────────────────────────┬────────────────────────────┘
                            │ (JSON REST API)
                            ▼
┌────────────────────────────────────────────────────────┐
│                   Frontend (UI)                        │
│   (React + Vite + TailwindCSS + Recharts)              │
└────────────────────────────────────────────────────────┘
```

### Detalhamento dos Componentes:
1. **Pipeline de Recolha (Camada de Dados):** Scripts em Python isolados que extraem a árvore HTML das páginas alvo, analisam (parse) as informações relevantes e normalizam os dados.
2. **Camada de Serviço (Backend):** Uma API desenvolvida em Python encarregada de receber os payloads dos scrapers, validar os esquemas e disponibilizar rotas seguras de leitura para a interface.
3. **Camada de Visualização (Frontend):** Uma Single Page Application (SPA) em React otimizada para o consumo ágil da API, focada na renderização de tabelas densas e gráficos responsivos.


## 4. Stack Tecnológica

### Backend (Processamento e Inteligência)
* **Linguagem:** Python 3.11+
* **Framework de API:** FastAPI (escolhido pela performance nativa assíncrona e documentação Swagger automática).
* **Bibliotecas de Scraping e Parsing:** BeautifulSoup4, Requests e `re` (Regex estruturado).
* **Manipulação de Dados:** Pandas (útil caso queira gerar relatórios agregados complexos em memória).
* **Banco de Dados:** PostgreSQL ou SQLite (para desenvolvimento ágil local).

### Frontend (Riqueza de Interface)
* **Ecossistema:** Node.js + React (Vite para build rápido).
* **Estilização:** TailwindCSS (classes utilitárias para um design limpo e responsivo).
* **Visualização de Dados:** Recharts ou Chart.js (bibliotecas de alta performance para gráficos baseados em componentes React).
* **Consumo de API:** Axios ou Fetch API nativo.


## 5. Modelo de Dados Proposto (Esquema Simplificado)

### Entidade: `Concurso`
```json
{
  "id": "UUID",
  "orgao_emissor": "String (ex: Prefeitura de Porto Alegre)",
  "banca_organizadora": "String (ex: Fundatec)",
  "status": "Enum [Inscricoes_Abertas, Aguardando_Edital, Finalizado]",
  "link_oficial": "String (URL)",
  "data_publicacao": "Date",
  "data_encerramento_inscricao": "DateTime",
  "data_prova": "Date",
  "vagas": [
    {
      "cargo": "String (ex: Analista de TI)",
      "escolaridade": "Enum [Fundamental, Medio, Tecnico, Superior]",
      "vagas_imediatas": "Integer",
      "cadastro_reserva": "Boolean",
      "salario_base": "Float",
      "carga_horaria": "Integer"
    }
  ]
}
```

## 6. Plano de Execução & Roadmap

### Semana 1: Estruturação do Backend & Recolha
1. Configurar o ambiente virtual Python (`venv`) e o repositório Git.
2. Desenvolver o script de scraping para capturar dados de pelo menos uma banca organizadora ativa.
3. Implementar as expressões regulares para extrair valores monetários (salários) e datas do texto.

### Semana 2: API & Banco de Dados
1. Modelar a tabela de concursos no banco de dados escolhido.
2. Criar os endpoints básicos no FastAPI:
    * `GET /api/concursos` (Listagem com filtros)
    * `GET /api/concursos/estatisticas` (Métricas de média salarial e totais)

### Semana 3: Interface em React
1. Iniciar o projeto React com Vite e instalar TailwindCSS + Recharts.
2. Construir os cartões de KPI superiores e a tabela principal de dados.
3. Conectar os componentes de gráficos aos dados retornados pelo endpoint de estatísticas da API.

### Semana 4: Polimento do Portfólio
1. Tratar estados de carregamento (Loaders/Skeletons) e erros na interface.
2. Escrever um `README.md` abrangente para a raiz do repositório contendo instruções de execução e imagens do painel.


## 7. Diferenciais Técnicos para Destacar no GitHub
* **Sanitização de Dados:** Demonstrar como o backend trata dados inconsistentes vindos da web (ex: converter o texto `"R$ 4.500,50 + benefícios"` para o float `4500.50`).
* **Componentização Limpa:** No React, separar filtros, gráficos e tabelas em componentes puros e reutilizáveis, mantendo uma gestão de estado previsível.
* **Arquitetura Clara:** Manter uma divisão de pastas intuitiva no repositório (ex: `/backend` e `/frontend`), facilitando a leitura por recrutadores.