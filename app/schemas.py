from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class PlanCrear(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    precio: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    duracion_dias: int = Field(gt=0)


class PlanLeer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    precio: Decimal
    duracion_dias: int
