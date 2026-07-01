from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session, selectinload

from entities.concurso import Concurso, StatusConcurso, Vaga
from schemas.concurso import (
    DistribuicaoPorEscolaridade,
    EstatisticasResponse,
    MediaSalarialPorArea,
)


def list_concursos(
    db: Session,
    cidade: str | None = None,
    palavra_chave: str | None = None,
    salario_min: float | None = None,
    salario_max: float | None = None,
    status: StatusConcurso | None = None,
    page: int = 1,
    page_size: int = 10,
) -> tuple[list[Concurso], int]:
    query = db.query(Concurso).options(selectinload(Concurso.vagas))

    if cidade:
        query = query.filter(Concurso.cidade.ilike(f"%{cidade}%"))
    if status:
        query = query.filter(Concurso.status == status)
    if palavra_chave:
        like = f"%{palavra_chave}%"
        query = query.filter(
            Concurso.orgao_emissor.ilike(like)
            | Concurso.banca_organizadora.ilike(like)
            | Concurso.vagas.any(Vaga.cargo.ilike(like))
        )
    if salario_min is not None:
        query = query.filter(Concurso.vagas.any(Vaga.salario_base >= salario_min))
    if salario_max is not None:
        query = query.filter(Concurso.vagas.any(Vaga.salario_base <= salario_max))

    total = query.distinct().count()
    items = (
        query.distinct()
        .order_by(Concurso.data_publicacao.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return items, total


def get_concurso(db: Session, concurso_id: str) -> Concurso | None:
    return (
        db.query(Concurso)
        .options(selectinload(Concurso.vagas))
        .filter(Concurso.id == concurso_id)
        .first()
    )


def get_estatisticas(db: Session) -> EstatisticasResponse:
    total_vagas_abertas = (
        db.query(func.coalesce(func.sum(Vaga.vagas_imediatas), 0))
        .join(Concurso)
        .filter(Concurso.status == StatusConcurso.INSCRICOES_ABERTAS)
        .scalar()
    ) or 0

    maior_salario = db.query(func.coalesce(func.max(Vaga.salario_base), 0.0)).scalar() or 0.0

    agora = datetime.now()
    daqui_a_7_dias = agora + timedelta(days=7)
    inscricoes_encerrando_na_semana = (
        db.query(func.count(Concurso.id))
        .filter(
            Concurso.status == StatusConcurso.INSCRICOES_ABERTAS,
            Concurso.data_encerramento_inscricao <= daqui_a_7_dias,
            Concurso.data_encerramento_inscricao >= agora,
        )
        .scalar()
    ) or 0

    media_por_area_rows = (
        db.query(Vaga.area, func.avg(Vaga.salario_base)).group_by(Vaga.area).all()
    )
    media_salarial_por_area = [
        MediaSalarialPorArea(area=area, media_salarial=round(media or 0.0, 2))
        for area, media in media_por_area_rows
    ]

    distribuicao_rows = (
        db.query(Vaga.escolaridade, func.coalesce(func.sum(Vaga.vagas_imediatas), 0))
        .group_by(Vaga.escolaridade)
        .all()
    )
    distribuicao_por_escolaridade = [
        DistribuicaoPorEscolaridade(escolaridade=escolaridade, total_vagas=total or 0)
        for escolaridade, total in distribuicao_rows
    ]

    return EstatisticasResponse(
        total_vagas_abertas=int(total_vagas_abertas),
        maior_salario=float(maior_salario),
        inscricoes_encerrando_na_semana=int(inscricoes_encerrando_na_semana),
        media_salarial_por_area=media_salarial_por_area,
        distribuicao_por_escolaridade=distribuicao_por_escolaridade,
    )
