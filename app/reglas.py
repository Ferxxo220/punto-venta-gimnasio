from datetime import date, timedelta
from enum import StrEnum


class EstadoMembresia(StrEnum):
    SIN_MEMBRESIA = "sin_membresia"
    ACTIVO = "activo"
    POR_VENCER = "por_vencer"
    VENCIDO = "vencido"


def calcular_vencimiento(
    vencimiento_actual: date | None,
    hoy: date,
    duracion_dias: int,
) -> date:
    # Si la membresía sigue vigente, el pago extiende desde su vencimiento actual.
    inicio = hoy if vencimiento_actual is None else max(hoy, vencimiento_actual)
    return inicio + timedelta(days=duracion_dias)


def estado_membresia(
    vencimiento: date | None,
    hoy: date,
    dias_por_vencer: int,
) -> EstadoMembresia:
    # El día de vencimiento todavía cuenta como vigente.
    if vencimiento is None:
        return EstadoMembresia.SIN_MEMBRESIA
    if vencimiento < hoy:
        return EstadoMembresia.VENCIDO
    if (vencimiento - hoy).days <= dias_por_vencer:
        return EstadoMembresia.POR_VENCER
    return EstadoMembresia.ACTIVO
