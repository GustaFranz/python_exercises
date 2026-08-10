# 119 - Refatoracao: renomear variaveis

## Objetivo

Substituir nomes confusos por nomes descritivos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / scripts |
| **Solicitacao** | Tornar script de verificacao de disco legivel para novo tecnico. |

## Enunciado

Refatore o script abaixo renomeando variaveis confusas (mantenha a mesma logica):

```python
x = 85
l = ["disco1", "disco2"]
i = 0
while i < len(l):
    print(l[i], "uso:", x, "%")
    if x > 80:
        print("ALERTA:", l[i])
    i += 1
```

Mapeamento sugerido:

- `x` → `uso_percentual`
- `l` → `discos`
- `i` → `indice`

Regra de negocio: exibir alerta se `uso_percentual > 80`.

Exiba o status de cada disco com os novos nomes.

## Como executar

```bash
cd "119_refatoracao_renomear_variaveis"
python main.py
```
