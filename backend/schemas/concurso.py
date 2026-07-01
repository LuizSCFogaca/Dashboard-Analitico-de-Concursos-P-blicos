from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from entities.concurso import AreaVaga, Escolaridade, StatusConcurso


class VagaBase(BaseModel):
    cargo: str
    area: AreaVaga
    escolaridade: Escolaridade
    vagas_imediatas: int = Field(ge=0)
    cadastro_reserva: bool = False
    salario_base: float = Field(ge=0)
    carga_horaria: int = Field(gt=0)


class VagaRead(VagaBase):
    model_config = ConfigDict(from_attributes=True)

    id: str


class ConcursoBase(BaseModel):
    orgao_emissor: str
    banca_organizadora: str
    cidade: str
    status: StatusConcurso
    link_oficial: str
    data_publicacao: date
    data_encerramento_inscricao: datetime
    data_prova: date | None = None


class ConcursoRead(ConcursoBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    vagas: list[VagaRead] = []


class ConcursoListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[ConcursoRead]


class MediaSalarialPorArea(BaseModel):
    area: AreaVaga
    media_salarial: float


class DistribuicaoPorEscolaridade(BaseModel):
    escolaridade: Escolaridade
    total_vagas: int


class EstatisticasResponse(BaseModel):
    total_vagas_abertas: int
    maior_salario: float
    inscricoes_encerrando_na_semana: int
    media_salarial_por_area: list[MediaSalarialPorArea]
    distribuicao_por_escolaridade: list[DistribuicaoPorEscolaridade]
