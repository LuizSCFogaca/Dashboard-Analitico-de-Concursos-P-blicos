from datetime import date, datetime, timedelta

from sqlalchemy.orm import Session

from entities.concurso import AreaVaga, Concurso, Escolaridade, StatusConcurso, Vaga


def _concurso(**kwargs) -> Concurso:
    return Concurso(**kwargs)


def _vaga(**kwargs) -> Vaga:
    return Vaga(**kwargs)


def build_mock_concursos(hoje: date) -> list[Concurso]:
    return [
        _concurso(
            orgao_emissor="Prefeitura Municipal de Porto Alegre",
            banca_organizadora="FUNDATEC",
            cidade="Porto Alegre",
            status=StatusConcurso.INSCRICOES_ABERTAS,
            link_oficial="https://fundatec.org.br/editais/poa-01-2024",
            data_publicacao=hoje - timedelta(days=10),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=3), datetime.min.time()),
            data_prova=hoje + timedelta(days=60),
            vagas=[
                _vaga(
                    cargo="Analista de Sistemas",
                    area=AreaVaga.TI,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=5,
                    cadastro_reserva=True,
                    salario_base=8500.00,
                    carga_horaria=40,
                ),
                _vaga(
                    cargo="Desenvolvedor Backend",
                    area=AreaVaga.TI,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=3,
                    cadastro_reserva=True,
                    salario_base=7800.00,
                    carga_horaria=40,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Prefeitura Municipal de Canoas",
            banca_organizadora="Objetiva Concursos",
            cidade="Canoas",
            status=StatusConcurso.INSCRICOES_ABERTAS,
            link_oficial="https://objetivaconcursos.com.br/editais/canoas-02-2024",
            data_publicacao=hoje - timedelta(days=20),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=10), datetime.min.time()),
            data_prova=hoje + timedelta(days=75),
            vagas=[
                _vaga(
                    cargo="Agente Administrativo",
                    area=AreaVaga.ADMINISTRACAO,
                    escolaridade=Escolaridade.MEDIO,
                    vagas_imediatas=10,
                    cadastro_reserva=True,
                    salario_base=2800.00,
                    carga_horaria=30,
                ),
                _vaga(
                    cargo="Enfermeiro",
                    area=AreaVaga.SAUDE,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=4,
                    cadastro_reserva=False,
                    salario_base=5200.00,
                    carga_horaria=36,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Prefeitura Municipal de Pelotas",
            banca_organizadora="FAURGS",
            cidade="Pelotas",
            status=StatusConcurso.AGUARDANDO_EDITAL,
            link_oficial="https://faurgs.ufrgs.br/editais/pelotas-01-2024",
            data_publicacao=hoje - timedelta(days=2),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=30), datetime.min.time()),
            data_prova=None,
            vagas=[
                _vaga(
                    cargo="Professor de Educação Básica",
                    area=AreaVaga.EDUCACAO,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=20,
                    cadastro_reserva=True,
                    salario_base=4300.00,
                    carga_horaria=20,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Prefeitura Municipal de Caxias do Sul",
            banca_organizadora="FUNDATEC",
            cidade="Caxias do Sul",
            status=StatusConcurso.INSCRICOES_ABERTAS,
            link_oficial="https://fundatec.org.br/editais/caxias-03-2024",
            data_publicacao=hoje - timedelta(days=5),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=1), datetime.min.time()),
            data_prova=hoje + timedelta(days=45),
            vagas=[
                _vaga(
                    cargo="Fiscal de Obras",
                    area=AreaVaga.OUTROS,
                    escolaridade=Escolaridade.TECNICO,
                    vagas_imediatas=2,
                    cadastro_reserva=False,
                    salario_base=3900.00,
                    carga_horaria=40,
                ),
                _vaga(
                    cargo="Analista de Suporte de TI",
                    area=AreaVaga.TI,
                    escolaridade=Escolaridade.TECNICO,
                    vagas_imediatas=1,
                    cadastro_reserva=True,
                    salario_base=4500.00,
                    carga_horaria=40,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Prefeitura Municipal de Santa Maria",
            banca_organizadora="Objetiva Concursos",
            cidade="Santa Maria",
            status=StatusConcurso.FINALIZADO,
            link_oficial="https://objetivaconcursos.com.br/editais/santa-maria-01-2023",
            data_publicacao=hoje - timedelta(days=400),
            data_encerramento_inscricao=datetime.combine(hoje - timedelta(days=370), datetime.min.time()),
            data_prova=hoje - timedelta(days=340),
            vagas=[
                _vaga(
                    cargo="Auxiliar Administrativo",
                    area=AreaVaga.ADMINISTRACAO,
                    escolaridade=Escolaridade.MEDIO,
                    vagas_imediatas=6,
                    cadastro_reserva=False,
                    salario_base=2400.00,
                    carga_horaria=30,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Governo do Estado do Rio Grande do Sul",
            banca_organizadora="FUNDATEC",
            cidade="Porto Alegre",
            status=StatusConcurso.INSCRICOES_ABERTAS,
            link_oficial="https://fundatec.org.br/editais/rs-saude-01-2024",
            data_publicacao=hoje - timedelta(days=15),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=5), datetime.min.time()),
            data_prova=hoje + timedelta(days=90),
            vagas=[
                _vaga(
                    cargo="Médico Plantonista",
                    area=AreaVaga.SAUDE,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=8,
                    cadastro_reserva=True,
                    salario_base=12000.00,
                    carga_horaria=24,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Prefeitura Municipal de Gravataí",
            banca_organizadora="FAURGS",
            cidade="Gravataí",
            status=StatusConcurso.AGUARDANDO_EDITAL,
            link_oficial="https://faurgs.ufrgs.br/editais/gravatai-01-2024",
            data_publicacao=hoje - timedelta(days=1),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=25), datetime.min.time()),
            data_prova=None,
            vagas=[
                _vaga(
                    cargo="Assistente Social",
                    area=AreaVaga.SAUDE,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=3,
                    cadastro_reserva=True,
                    salario_base=4800.00,
                    carga_horaria=30,
                ),
            ],
        ),
        _concurso(
            orgao_emissor="Prefeitura Municipal de Novo Hamburgo",
            banca_organizadora="Objetiva Concursos",
            cidade="Novo Hamburgo",
            status=StatusConcurso.INSCRICOES_ABERTAS,
            link_oficial="https://objetivaconcursos.com.br/editais/novo-hamburgo-02-2024",
            data_publicacao=hoje - timedelta(days=8),
            data_encerramento_inscricao=datetime.combine(hoje + timedelta(days=2), datetime.min.time()),
            data_prova=hoje + timedelta(days=50),
            vagas=[
                _vaga(
                    cargo="Professor de Informática",
                    area=AreaVaga.EDUCACAO,
                    escolaridade=Escolaridade.SUPERIOR,
                    vagas_imediatas=2,
                    cadastro_reserva=True,
                    salario_base=3600.00,
                    carga_horaria=20,
                ),
                _vaga(
                    cargo="Técnico em TI",
                    area=AreaVaga.TI,
                    escolaridade=Escolaridade.TECNICO,
                    vagas_imediatas=2,
                    cadastro_reserva=False,
                    salario_base=3200.00,
                    carga_horaria=40,
                ),
            ],
        ),
    ]


def seed_if_empty(db: Session) -> None:
    if db.query(Concurso).first() is not None:
        return

    concursos = build_mock_concursos(date.today())
    db.add_all(concursos)
    db.commit()
