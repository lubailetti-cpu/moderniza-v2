"""Reemplaza 'agente(s)' por 'flujo(s) automático(s)' en los HTMLs de Moderniza.
Preserva URL de backend Modal y nombre 'Mo'."""
import re

ARCHIVOS = [
    r'C:/Users/LUCIA/Proyecto Moderniza/moderniza-v2/index.html',
    r'C:/Users/LUCIA/Proyecto Moderniza/moderniza-v2/mockup.html',
]

# Protected strings: reemplazar por placeholder antes, restaurar al final
PROTECTED = [
    'moderniza-agentes-fastapi-app',  # URL de backend Modal — NO tocar
]

REEMPLAZOS = [
    # Botones CTA — "Usar agente" → "Usar" (debe ir antes de los reemplazos generales)
    ('Usar agente ', 'Usar '),  # con espacio para no pisar "Usar agente<cosa>"

    # Plurales primero
    ('Galería de agentes', 'Galería de flujos automáticos'),
    ('galería de agentes', 'galería de flujos automáticos'),
    ('Los agentes usan', 'Los flujos automáticos usan'),
    ('los agentes usan', 'los flujos automáticos usan'),
    ('Todos los agentes incluyen', 'Todos los flujos incluyen'),
    ('todos los agentes incluyen', 'todos los flujos incluyen'),
    ('nuestros agentes de inteligencia artificial', 'nuestros flujos automáticos con inteligencia artificial'),
    ('tus agentes de IA', 'tus flujos automáticos con IA'),
    ('los agentes de la plataforma', 'los flujos automáticos de la plataforma'),
    ('trabajo con los agentes', 'trabajo con los flujos automáticos'),
    ('Agentes activos', 'Flujos activos'),
    ('Tus agentes', 'Tus flujos'),
    ('ABC de los Agentes de IA', 'ABC de los Flujos con IA'),

    # Singulares
    ('Elige un agente', 'Elige un flujo'),
    ('el agente hace el resto', 'el flujo lo hace todo'),
    ('Cuando el agente tiene dudas', 'Cuando el flujo tiene dudas'),
    ('cuando el agente tiene dudas', 'cuando el flujo tiene dudas'),
    ('Si el agente tiene dudas', 'Si el flujo tiene dudas'),
    ('guíar al agente', 'guiar el flujo'),  # también corrige "guíar" mal tildeado
    ('guiar al agente', 'guiar el flujo'),
    ('Indicaciones para el agente', 'Indicaciones para el flujo'),
    ('este agente', 'este flujo'),
]

total_cambios = 0

for path in ARCHIVOS:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Proteger strings
    for i, prot in enumerate(PROTECTED):
        content = content.replace(prot, f'__PROTECTED_{i}__')

    # 2. Aplicar reemplazos
    cambios_archivo = 0
    for viejo, nuevo in REEMPLAZOS:
        count = content.count(viejo)
        if count > 0:
            content = content.replace(viejo, nuevo)
            cambios_archivo += count

    # 3. Restaurar strings protegidos
    for i, prot in enumerate(PROTECTED):
        content = content.replace(f'__PROTECTED_{i}__', prot)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'{path.split("/")[-1]}: {cambios_archivo} reemplazos')
    total_cambios += cambios_archivo

print(f'\nTotal: {total_cambios} reemplazos hechos.')
print('URL de backend Modal preservada: moderniza-agentes-fastapi-app')
