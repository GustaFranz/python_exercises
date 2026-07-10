# 20 - Zip: consolidar tres listas

## Objetivo

Consolidar listas paralelas em registros estruturados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | AgroData Cooperativa |
| **Setor** | Agronegocio / cooperativa escolar rural |
| **Solicitacao** | Unificar dados de safra para envio ao sistema da cooperativa. |

## Enunciado

fazendas = ["Sitio Sol", "Fazenda Verde", "Chacara Norte"]
producoes_t = [12.5, 8.0, 15.2]   # toneladas
qualidades = ["A", "B", "A"]
Consolide em lista de dicionarios:
[{"fazenda": ..., "producao_t": ..., "qualidade": ...}, ...]
Use zip e dict comprehension ou loop.
Exiba registros e total de producao das fazendas qualidade A.

## Como executar

```bash
cd "20_zip_consolidar_tres_listas"
python main.py
```
