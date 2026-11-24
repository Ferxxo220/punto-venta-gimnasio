from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.crud import planes as crud_planes
from app.database import get_db
from app.schemas import PlanCrear, PlanLeer

router = APIRouter(prefix="/planes", tags=["planes"])


@router.post("", response_model=PlanLeer, status_code=status.HTTP_201_CREATED)
def crear_plan(datos: PlanCrear, db: Session = Depends(get_db)):
    try:
        return crud_planes.crear_plan(db, **datos.model_dump())
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un plan con ese nombre",
        )


@router.get("", response_model=list[PlanLeer])
def listar_planes(db: Session = Depends(get_db)):
    return crud_planes.listar_planes(db)
