from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.database import get_db
from entities.concurso import StatusConcurso
from schemas.concurso import ConcursoListResponse, ConcursoRead, EstatisticasResponse
from services import concurso_service

router = APIRouter(prefix="/api/concursos", tags=["concursos"])


@router.get("/estatisticas", response_model=EstatisticasResponse)
def obter_estatisticas(db: Session = Depends(get_db)):
    return concurso_service.get_estatisticas(db)


@router.get("", response_model=ConcursoListResponse)
def listar_concursos(
    cidade: str | None = Query(default=None),
    palavra_chave: str | None = Query(default=None),
    salario_min: float | None = Query(default=None, ge=0),
    salario_max: float | None = Query(default=None, ge=0),
    status: StatusConcurso | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    items, total = concurso_service.list_concursos(
        db,
        cidade=cidade,
        palavra_chave=palavra_chave,
        salario_min=salario_min,
        salario_max=salario_max,
        status=status,
        page=page,
        page_size=page_size,
    )
    return ConcursoListResponse(total=total, page=page, page_size=page_size, items=items)


@router.get("/{concurso_id}", response_model=ConcursoRead)
def obter_concurso(concurso_id: str, db: Session = Depends(get_db)):
    concurso = concurso_service.get_concurso(db, concurso_id)
    if concurso is None:
        raise HTTPException(status_code=404, detail="Concurso não encontrado")
    return concurso
