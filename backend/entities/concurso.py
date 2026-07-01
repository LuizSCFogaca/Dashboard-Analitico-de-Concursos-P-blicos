import enum
import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class StatusConcurso(str, enum.Enum):
    INSCRICOES_ABERTAS = "Inscricoes_Abertas"
    AGUARDANDO_EDITAL = "Aguardando_Edital"
    FINALIZADO = "Finalizado"


class Escolaridade(str, enum.Enum):
    FUNDAMENTAL = "Fundamental"
    MEDIO = "Medio"
    TECNICO = "Tecnico"
    SUPERIOR = "Superior"


class AreaVaga(str, enum.Enum):
    TI = "TI"
    ADMINISTRACAO = "Administracao"
    SAUDE = "Saude"
    EDUCACAO = "Educacao"
    OUTROS = "Outros"


def _uuid() -> str:
    return str(uuid.uuid4())


class Concurso(Base):
    __tablename__ = "concursos"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    orgao_emissor: Mapped[str] = mapped_column(String(255), nullable=False)
    banca_organizadora: Mapped[str] = mapped_column(String(255), nullable=False)
    cidade: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    status: Mapped[StatusConcurso] = mapped_column(
        Enum(StatusConcurso), nullable=False, default=StatusConcurso.AGUARDANDO_EDITAL
    )
    link_oficial: Mapped[str] = mapped_column(String(500), nullable=False)
    data_publicacao: Mapped[date] = mapped_column(Date, nullable=False)
    data_encerramento_inscricao: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    data_prova: Mapped[date | None] = mapped_column(Date, nullable=True)

    vagas: Mapped[list["Vaga"]] = relationship(
        "Vaga", back_populates="concurso", cascade="all, delete-orphan"
    )


class Vaga(Base):
    __tablename__ = "vagas"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    concurso_id: Mapped[str] = mapped_column(ForeignKey("concursos.id"), nullable=False)
    cargo: Mapped[str] = mapped_column(String(255), nullable=False)
    area: Mapped[AreaVaga] = mapped_column(Enum(AreaVaga), nullable=False, default=AreaVaga.OUTROS)
    escolaridade: Mapped[Escolaridade] = mapped_column(Enum(Escolaridade), nullable=False)
    vagas_imediatas: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    cadastro_reserva: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    salario_base: Mapped[float] = mapped_column(Float, nullable=False)
    carga_horaria: Mapped[int] = mapped_column(Integer, nullable=False)

    concurso: Mapped["Concurso"] = relationship("Concurso", back_populates="vagas")
