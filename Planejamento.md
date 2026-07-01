# Planejamento do Projeto — ConectaConcursos RS

Checklist de progresso do desenvolvimento. Marque `[x]` conforme for concluindo cada etapa. As fases seguem a ordem recomendada de execução (backend com dados mockados → frontend real → scraping → persistência → polimento → deploy).

Estado no início deste planejamento: apenas `DetalhesTecnicos.md` (especificação), um mockup estático em `frontend/` (`code.html` + `DESIGN.md`, sem projeto React real) e `backend/entities/concurso.py` vazio.

---

## Fase 0 — Preparação do Ambiente

- [ ] Inicializar repositório Git na raiz do projeto (se ainda não houver) e criar `.gitignore` (Python + Node)
- [ ] Criar ambiente virtual Python (`venv`) dentro de `backend/`
- [ ] Definir estrutura de pastas do backend: `entities/`, `routers/`, `services/`, `scrapers/`, `db/`, `schemas/`
- [ ] Criar `requirements.txt` inicial (fastapi, uvicorn, pydantic, sqlalchemy, python-dotenv)
- [ ] Decidir e documentar o banco de dados de desenvolvimento (SQLite local) vs produção (PostgreSQL)

## Fase 1 — Backend: Modelo de Dados e API com Dados Mockados

Objetivo: ter um contrato de API estável antes de investir tempo em scraping.

- [ ] Implementar modelo `Concurso` (Pydantic schema + SQLAlchemy model) conforme o esquema em `DetalhesTecnicos.md` (seção 5)
- [ ] Implementar modelo `Vaga` (relacionado a `Concurso`, 1:N)
- [ ] Criar enum de `status` (`Inscricoes_Abertas`, `Aguardando_Edital`, `Finalizado`)
- [ ] Criar enum de `escolaridade` (`Fundamental`, `Medio`, `Tecnico`, `Superior`)
- [ ] Popular uma base de dados mockada (fixtures/seed) com 8-10 concursos fictícios cobrindo cidades diferentes (Porto Alegre, Canoas, Pelotas, Caxias do Sul, Santa Maria)
- [ ] Configurar app FastAPI (`main.py`), CORS habilitado para o frontend local
- [ ] Endpoint `GET /api/concursos` — listagem com filtros (`cidade`, `palavra_chave`, `faixa_salarial`, `status`) e paginação
- [ ] Endpoint `GET /api/concursos/{id}` — detalhe de um concurso específico
- [ ] Endpoint `GET /api/concursos/estatisticas` — KPIs (total de vagas abertas, maior salário, inscrições encerrando na semana) e agregações para gráficos (média salarial por área, distribuição por escolaridade)
- [ ] Validar documentação automática do Swagger (`/docs`) e revisar tipos de resposta
- [ ] Escrever testes básicos dos endpoints (pytest + httpx/TestClient)

## Fase 2 — Frontend: Migração do Mockup para Projeto React Real

Objetivo: sair do HTML estático com Tailwind via CDN para uma SPA de verdade.

- [ ] Criar projeto com Vite (`npm create vite@latest frontend -- --template react`) — decidir se reaproveita a pasta atual ou cria nova e migra os arquivos de referência
- [ ] Instalar e configurar TailwindCSS localmente (não via CDN), portando as cores/tipografia definidas em `DESIGN.md`
- [ ] Instalar Recharts (ou Chart.js) e Axios
- [ ] Estruturar pastas: `src/components`, `src/pages`, `src/hooks`, `src/services` (cliente da API)
- [ ] Criar layout base: `TopNavBar`, `Sidebar` (lista de cidades), `MainContent`, `ComparisonTray` — portando o HTML de `code.html` para componentes React
- [ ] Componente `KpiCard` reutilizável (total de vagas, maior salário, encerrando na semana)
- [ ] Componente `ConcursoDetailCard` (dados financeiros, requisitos, datas, cargos)
- [ ] Componente `ExamListItem` (linha da lista de cidades/editais)
- [ ] Componente `ComparisonSlot` (card preenchido + slot vazio com estado dashed)
- [ ] Componente de tabela de busca avançada com paginação e filtros (palavra-chave, faixa salarial, município)
- [ ] Gráfico: média salarial por área (TI, Administração, Saúde, Educação)
- [ ] Gráfico: distribuição de vagas por nível de escolaridade
- [ ] Hook/serviço para consumir a API (`useConcursos`, `useEstatisticas`) usando Axios/Fetch
- [ ] Gerenciamento de estado dos filtros e da seleção de itens no comparativo (Context API ou estado local elevado)
- [ ] Conectar todos os componentes aos dados reais vindos do backend (Fase 1), substituindo os dados fixos do mockup
- [ ] Estados de loading (skeletons) e de erro (mensagem + retry) em todas as chamadas de API
- [ ] Responsividade: validar layout em mobile/tablet (o mockup atual é fixo para desktop)

## Fase 3 — Pipeline de Coleta de Dados (Web Scraping)

- [ ] Escolher a primeira banca organizadora alvo (ex: Fundatec) e mapear a estrutura HTML das páginas de editais
- [ ] Implementar scraper inicial com `requests` + `BeautifulSoup4` para essa banca
- [ ] Implementar extração via Regex: valores monetários (ex: `"R$ 4.500,50 + benefícios"` → `float 4500.50`), datas, carga horária, escolaridade
- [ ] Criar camada de sanitização/normalização dos dados extraídos (tratar inconsistências, valores ausentes, formatos variados)
- [ ] Persistir os dados coletados no banco via camada de serviço (não diretamente do scraper)
- [ ] Adicionar tratamento de erros de rede/parsing (timeouts, HTML mudou, página fora do ar) com logging
- [ ] Escrever testes unitários para as funções de extração/regex com casos variados de texto de edital
- [ ] Expandir para a 2ª e 3ª banca (ex: FAURGS, Objetiva), reaproveitando a camada de sanitização
- [ ] Configurar agendamento periódico da coleta (cron local ou `APScheduler`/`schedule` no próprio backend)

## Fase 4 — Persistência Definitiva e Integração Completa

- [ ] Migrar de SQLite (dev) para PostgreSQL (ou confirmar SQLite para produção, se for portfólio simples)
- [ ] Criar migrações de banco (Alembic)
- [ ] Substituir dados mockados da Fase 1 pelos dados reais coletados na Fase 3
- [ ] Validar que os endpoints da API continuam consistentes com dados reais (casos extremos: concurso sem vaga, sem salário definido, cadastro reserva puro)
- [ ] Testar o fluxo ponta a ponta: scraper → banco → API → frontend

## Fase 5 — Fase 2 do Escopo Original (Opcional/Expansão)

- [ ] Criar bot de Telegram para notificações
- [ ] Implementar sistema de assinatura de palavras-chave por usuário (ex: "Ciência da Computação", "Analista")
- [ ] Job que compara novos editais coletados contra as assinaturas e dispara notificação

## Fase 6 — Polimento para Portfólio

- [ ] Revisar consistência visual do frontend com o `DESIGN.md` (cores, espaçamento, tipografia)
- [ ] Adicionar tratamento de estados vazios (nenhum concurso encontrado, comparativo vazio)
- [ ] Revisar acessibilidade básica (contraste, labels em inputs, navegação por teclado)
- [ ] Escrever `README.md` na raiz do repositório: descrição do projeto, prints do dashboard, instruções de instalação/execução (backend e frontend), variáveis de ambiente necessárias
- [ ] Documentar a arquitetura (diagrama já existe em `DetalhesTecnicos.md` — trazer para o README)
- [ ] Revisar e organizar a estrutura de pastas final (`/backend`, `/frontend`) para leitura fácil por recrutadores
- [ ] Adicionar testes de cobertura mínima (backend obrigatório; frontend se houver tempo)

## Fase 7 — Deploy (Opcional, mas recomendado para portfólio)

- [ ] Escolher hospedagem do backend (ex: Render, Railway, Fly.io)
- [ ] Escolher hospedagem do frontend (ex: Vercel, Netlify)
- [ ] Configurar variáveis de ambiente de produção (URL da API, string de conexão do banco)
- [ ] Configurar banco de dados gerenciado em produção (ex: Neon, Supabase, Railway Postgres)
- [ ] Validar CORS e HTTPS entre frontend e backend em produção
- [ ] Testar aplicação completa em produção e atualizar o README com o link ao vivo

---

## Como usar este arquivo

- Atualize os checkboxes conforme for concluindo cada item.
- Se uma etapa mudar de escopo (ex: trocar de banca organizadora, pular o bot de Telegram), edite a lista em vez de deixar itens obsoletos.
- As Fases 0–2 são o caminho crítico para ter algo demonstrável rapidamente (API + frontend com dados mockados). Scraping real (Fase 3) pode vir depois sem bloquear o restante.
