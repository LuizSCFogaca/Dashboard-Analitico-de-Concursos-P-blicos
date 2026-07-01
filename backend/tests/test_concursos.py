def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_listar_concursos_retorna_dados_seed(client):
    response = client.get("/api/concursos")
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 8
    assert len(body["items"]) == 8
    assert body["page"] == 1


def test_listar_concursos_filtra_por_cidade(client):
    response = client.get("/api/concursos", params={"cidade": "Porto Alegre"})
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 2
    assert all(item["cidade"] == "Porto Alegre" for item in body["items"])


def test_listar_concursos_filtra_por_palavra_chave(client):
    response = client.get("/api/concursos", params={"palavra_chave": "Analista"})
    assert response.status_code == 200
    body = response.json()
    assert body["total"] >= 1
    cargos = [vaga["cargo"] for item in body["items"] for vaga in item["vagas"]]
    assert any("Analista" in cargo for cargo in cargos)


def test_listar_concursos_filtra_por_faixa_salarial(client):
    response = client.get(
        "/api/concursos", params={"salario_min": 10000, "salario_max": 15000}
    )
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    salarios = [vaga["salario_base"] for vaga in body["items"][0]["vagas"]]
    assert any(10000 <= s <= 15000 for s in salarios)


def test_listar_concursos_paginacao(client):
    response = client.get("/api/concursos", params={"page": 1, "page_size": 3})
    assert response.status_code == 200
    body = response.json()
    assert len(body["items"]) == 3
    assert body["page_size"] == 3
    assert body["total"] == 8


def test_obter_concurso_por_id(client):
    listagem = client.get("/api/concursos").json()
    primeiro_id = listagem["items"][0]["id"]

    response = client.get(f"/api/concursos/{primeiro_id}")
    assert response.status_code == 200
    assert response.json()["id"] == primeiro_id


def test_obter_concurso_inexistente_retorna_404(client):
    response = client.get("/api/concursos/id-que-nao-existe")
    assert response.status_code == 404


def test_estatisticas_retorna_estrutura_esperada(client):
    response = client.get("/api/concursos/estatisticas")
    assert response.status_code == 200
    body = response.json()

    assert body["total_vagas_abertas"] > 0
    assert body["maior_salario"] == 12000.0
    assert isinstance(body["inscricoes_encerrando_na_semana"], int)
    assert len(body["media_salarial_por_area"]) > 0
    assert len(body["distribuicao_por_escolaridade"]) > 0
