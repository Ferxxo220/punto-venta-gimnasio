from datetime import date

import pytest

from app.reglas import EstadoMembresia, calcular_vencimiento, estado_membresia

HOY = date(2026, 6, 10)


def test_calcular_vencimiento_sin_membresia_previa_parte_de_hoy():
    assert calcular_vencimiento(None, HOY, 30) == date(2026, 7, 10)


def test_calcular_vencimiento_vigente_extiende_desde_su_vencimiento():
    assert calcular_vencimiento(date(2026, 6, 20), HOY, 30) == date(2026, 7, 20)


def test_calcular_vencimiento_vencido_parte_de_hoy():
    assert calcular_vencimiento(date(2026, 6, 1), HOY, 30) == date(2026, 7, 10)


@pytest.mark.parametrize(
    ("vencimiento", "esperado"),
    [
        (None, EstadoMembresia.SIN_MEMBRESIA),
        (date(2026, 6, 9), EstadoMembresia.VENCIDO),
        (HOY, EstadoMembresia.POR_VENCER),
        (date(2026, 6, 15), EstadoMembresia.POR_VENCER),
        (date(2026, 6, 16), EstadoMembresia.ACTIVO),
    ],
)
def test_estado_membresia(vencimiento, esperado):
    assert estado_membresia(vencimiento, HOY, dias_por_vencer=5) == esperado
