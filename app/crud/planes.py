from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Plan


def crear_plan(db: Session, nombre: str, precio: Decimal, duracion_dias: int) -> Plan:
    plan = Plan(nombre=nombre, precio=precio, duracion_dias=duracion_dias)
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


def obtener_plan(db: Session, plan_id: int) -> Plan | None:
    return db.get(Plan, plan_id)


def listar_planes(db: Session) -> list[Plan]:
    return list(db.scalars(select(Plan).order_by(Plan.id)))
