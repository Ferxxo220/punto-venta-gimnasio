# Estado del proyecto

## Objetivo

Punto de venta para un gimnasio con FastAPI, SQLAlchemy, Pydantic y SQLite. Los módulos son socios, planes, pagos, membresías (alertas y morosos) y caja (turnos y corte).

## Estado actual

- Existen [requirements.txt](./requirements.txt), `.env`, [.gitignore](./.gitignore), [app/database.py](./app/database.py) y [app/main.py](./app/main.py).
- `/docs` funcionó con la aplicación FastAPI base.
- Falta `models.py`, `schemas.py`, `reglas.py`, `routers/`, `servicios/`, `crud/` y `tests/`.

## Estructura de carpetas

```
ServicioSocialPuntoDeVenta1/
├── .venv/                # Entorno virtual
├── app/
│   ├── __init__.py
│   ├── main.py           # Punto de entrada: FastAPI y routers
│   ├── database.py       # SQLite / SQLAlchemy (engine, sesión, get_db)
│   ├── models.py         # Tablas: Plan, Socio, Pago, Turno
│   ├── schemas.py        # Esquemas Pydantic (entrada y salida)
│   ├── reglas.py         # Reglas puras: calcular_vencimiento(), estado_membresia()
│   ├── routers/          # Solo reciben y devuelven
│   │   ├── __init__.py
│   │   ├── socios.py     # Registrar, buscar, consultar estado
│   │   ├── planes.py     # Crear y listar (llama directo a crud)
│   │   ├── pagos.py      # Registrar cobro e historial
│   │   ├── membresias.py # Alertas de vencimiento y morosos
│   │   └── caja.py       # Turno y cierre de caja
│   ├── servicios/        # Reglas + crud
│   │   ├── __init__.py
│   │   ├── socios.py     # registrar_socio(), buscar_socios()
│   │   ├── pagos.py      # registrar_pago(): un solo commit
│   │   ├── membresias.py # listar_morosos(), listar_por_vencer()
│   │   └── caja.py       # abrir_turno(), obtener_corte()
│   └── crud/             # Solo base de datos
│       ├── __init__.py
│       ├── socios.py     # Crear, obtener, listar, buscar; actualizar vencimiento
│       ├── planes.py     # Crear, obtener, listar
│       ├── pagos.py      # Crear; listar por socio, rango o turno
│       └── turnos.py     # Crear, obtener abierto, cerrar
├── tests/
│   └── test_reglas.py    # Prueba las reglas con fechas, sin FastAPI
├── .env                  # DATABASE_URL, DIAS_POR_VENCER
├── .gitignore            # .venv, .env, *.db
└── requirements.txt
```

## Estructura por capas

Cada capa solo habla con la de abajo.

1. `routers/`: reciben y devuelven datos HTTP, sin lógica.
2. `servicios/`: flujos de negocio completos; combinan reglas y CRUD. Aquí se hace el único `commit` de cada operación.
3. `reglas.py`: funciones puras como `calcular_vencimiento()` y `estado_membresia()`. No tocan la base de datos.
4. `crud/`: solo acceso a la base de datos.
5. `models.py`, `schemas.py` y `database.py`: tablas, validación de entrada y salida, y conexión.

Excepción: `routers/planes.py` llama directo a `crud`, porque no tiene reglas de negocio.

## Metodología

- Cada petición recibe su sesión con `Depends(get_db)`, y `get_db()` la cierra al terminar.
- `get_db()` no hace commit: lo hace el servicio.
- La configuración local va en `.env` (`DATABASE_URL`, `DIAS_POR_VENCER`), fuera de Git.
- Las reglas se prueban en `tests/test_reglas.py` con fechas, sin levantar FastAPI.
- El entorno es `.venv` con Python 3.11.

## Siguiente paso

`models.py` (Plan, Socio, Pago, Turno), luego `reglas.py` con sus pruebas, y después `crud`, `servicios` y `routers`.
