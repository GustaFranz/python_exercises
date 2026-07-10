# Estrategias Python — Material de Estudo Pessoal

> **AVISO IMPORTANTE**
>
> Este material foi produzido **apenas para fins de estudo pessoal**. Ele ainda nao passou
> por revisao final nem pela organizacao visual dos guias publicados em
> `04_study_materials/python/`. Posteriormente, o conteudo sera **desmembrado, revisado e publicado**
> de forma mais organizada no repositorio.
>
> **Autor:** Prof. Gustavo Franz (Science/Biology) · Python Developer in Progress
>
> **Legenda dos blocos neste material:**
> - 📋 **ENUNCIADO** — o que o exercicio pede
> - 👤 **SUA SOLUCAO** — codigo que voce ja escreveu no repositorio
> - ⚡ **COM A ESTRATEGIA** — mesma logica, usando o recurso estudado
> - 💡 **QUANDO USAR / EVITAR** — orientacao pratica
> - ⚠️ **ERROS COMUNS** — armadilhas frequentes
> - 🎯 **MINI-DESAFIO** — pratique antes de ver o gabarito

---

## Indice

1. [Matriz de decisao rapida](#matriz-de-decisao-rapida)
2. [Checklist de revisao](#checklist-de-revisao)
3. [Bonus: max, min e sorted](#bonus-max-min-e-sorted)
4. [1. Funcoes built-in: sum, any, all](#1-funcoes-built-in-sum-any-all)
5. [2. Operador ternario](#2-operador-ternario-if-inline)
6. [3. enumerate](#3-enumerate)
7. [4. zip](#4-zip)
8. [5. Desempacotamento (unpacking)](#5-desempacotamento-unpacking)
9. [6. Context manager (with)](#6-context-manager-with)
10. [7. List comprehension](#7-list-comprehension)
11. [8. Dict comprehension](#8-dict-comprehension)
12. [9. Lambda](#9-lambda)
13. [10. *args e **kwargs](#10-args-e-kwargs)
14. [Glossario](#glossario)

---

## Matriz de decisao rapida

| Preciso de... | Use... | Evite... |
|---------------|--------|----------|
| Somar todos os valores de uma lista | `sum(lista)` | `for` com acumulador manual |
| Saber se **algum** item atende condicao | `any(...)` | `for` com flag e `break` |
| Saber se **todos** atendem condicao | `all(...)` | varios `if` espalhados |
| Escolher entre 2 valores simples | operador ternario | `if/else` de 4 linhas |
| Indice + valor ao percorrer lista | `enumerate()` | `range(len(lista))` |
| Percorrer duas listas juntas | `zip()` | indice manual `lista1[i], lista2[i]` |
| Separar valores de tupla/lista | unpacking `a, b = tupla` | acessar `[0]`, `[1]` repetidamente |
| Abrir arquivo com seguranca | `with open(...) as f` | `open()` sem fechar |
| Criar lista filtrada/transformada | list comprehension | `for` + `append` |
| Criar dicionario a partir de dados | dict comprehension | `for` + atribuicao manual |
| Funcao pequena para `sorted`/`filter` | `lambda` | `def` com nome usado 1 vez |
| Funcao com quantidade variavel de args | `*args`, `**kwargs` | muitos parametros opcionais |

---

## Checklist de revisao

Marque quando conseguir fazer **sem olhar**:

- [ ] Reescrever a solucao do exercicio 37 so com `sum`, `min`, `max`
- [ ] Reescrever o exercicio 68 com list comprehension
- [ ] Reescrever o exercicio 67 com e sem `enumerate` (comparar)
- [ ] Explicar a diferenca entre `any` e `all` com exemplo proprio
- [ ] Converter um `if/else` do exercicio 41 em ternario
- [ ] Usar `zip` para juntar nomes e notas do exercicio 58
- [ ] Desempacotar tupla do exercicio 57 em 1 linha
- [ ] Explicar por que `with open` e mais seguro que `open` sozinho
- [ ] Criar dict comprehension a partir do estoque do exercicio 82
- [ ] Usar lambda em `sorted` como no exercicio 99
- [ ] Criar funcao com `*args` que soma quantos numeros forem passados

---

## Bonus: max, min e sorted

Voce ja usa `max`, `min` e `sum` no exercicio **37** e `sorted` no **65**. Eles formam a **familia de agregacao/ordenacao** do Python.

```python
notas = [7.5, 3.2, 8.0, 6.5, 4.0]
print(sum(notas) / len(notas))   # media
print(max(notas))                # maior
print(min(notas))                # menor
print(sorted(notas))             # nova lista ordenada (original intacta)
print(sorted(notas, reverse=True))
```

| Funcao | Retorna | Altera original? |
|--------|---------|------------------|
| `sum()` | soma | nao |
| `max()` / `min()` | extremo | nao |
| `sorted()` | lista ordenada | nao |
| `.sort()` (metodo) | None | **sim**, altera a lista |

---

# 1. Funcoes built-in: sum, any, all

## O que e

Funcoes prontas do Python que operam sobre iteraveis (listas, tuplas etc.) sem voce escrever loops manualmente.

**Sintaxe minima:**

```python
sum(iteravel)           # soma numeros
any(iteravel)           # True se pelo menos um for True
all(iteravel)           # True se todos forem True
```

---

### Exemplo 1 — Exercicio 37 (Nivel 1: comparacao direta)

📋 **ENUNCIADO (ex. 37):** Turma com 8 alunos. Digitar notas e obter media, maior nota, menor nota e quantidade acima de 6.

👤 **SUA SOLUCAO (trecho relevante):**

```python
notas = []
for a in range(1, 9):
    aluno = float(input(f'Nota do aluno {a}: ').replace(',', '.'))
    notas.append(aluno)

media = sum(notas) / len(notas)
print(f'A menor nota da turma foi {min(notas):.1f}')
print(f'A maior nota da turma foi {max(notas):.1f}')

notas_acima_6 = 0
for n in notas:
    if n > 6:
        notas_acima_6 += 1
```

**Linha a linha (sua solucao):**
| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 1 | `notas = []` | Cria lista vazia para guardar as 8 notas |
| 2-4 | `for` + `input` + `append` | Repete 8 vezes: le nota, troca virgula por ponto, adiciona na lista |
| 6 | `sum(notas) / len(notas)` | **Ja usa built-in `sum`**: soma todas e divide pela quantidade |
| 7-8 | `min(notas)`, `max(notas)` | Built-ins que encontram menor e maior sem loop manual |
| 10-13 | contador com `for` | Percorre de novo para contar quantas notas sao > 6 |

⚡ **COM A ESTRATEGIA (`any`/`all` + `sum`):**

```python
notas = [float(input(f'Nota do aluno {a}: ').replace(',', '.')) for a in range(1, 9)]
media = sum(notas) / len(notas)
acima_6 = sum(1 for n in notas if n > 6)  # conta True como 1
tem_nota_maxima = any(n == 10 for n in notas)
todos_acima_4 = all(n >= 4 for n in notas)
```

**Linha a linha (com estrategia):**
| Linha | Explicacao |
|-------|------------|
| `sum(notas)` | Soma total — voce ja domina |
| `sum(1 for n in notas if n > 6)` | Generator: conta elementos que passam no filtro |
| `any(n == 10 for n in notas)` | Retorna `True` se **existe** pelo menos uma nota 10 |
| `all(n >= 4 for n in notas)` | Retorna `True` se **todas** as notas forem >= 4 |

```
┌─ Sua forma (contar > 6) ──────┐    ┌─ Com sum + generator ────────┐
│  for + if + contador = 4 linhas│ →  │  sum(1 for n in ... if ...)  │
└────────────────────────────────┘    └──────────────────────────────┘
```

---

### Exemplo 2 — Exercicio 68 (Nivel 1)

📋 **ENUNCIADO (ex. 68):** Classificar notas em aprovados (>=6), recuperacao (4-5.9), reprovados (<4) e calcular media.

👤 **SUA SOLUCAO:**

```python
notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]
media = sum(notas) / len(notas)
list_aprovados = []
for c in notas:
    if c >= 6:
        list_aprovados.append(c)
    elif c >= 4:
        list_recuperacao.append(c)
    else:
        list_reprovados.append(c)
```

⚡ **COM `any`/`all` (verificacoes rapidas apos classificar):**

```python
media = sum(notas) / len(notas)
list_aprovados = [c for c in notas if c >= 6]
list_recuperacao = [c for c in notas if 4 <= c < 6]
list_reprovados = [c for c in notas if c < 4]

turma_tem_reprovado = any(n < 4 for n in notas)
turma_toda_aprovada = all(n >= 6 for n in notas)
algum_tirou_dez = any(n == 10 for n in notas)
```

| Verificacao | Funcao | Resultado com a lista do ex. 68 |
|-------------|--------|----------------------------------|
| Tem reprovado? | `any(n < 4 ...)` | `True` (2.8, 3.2) |
| Todos aprovados? | `all(n >= 6 ...)` | `False` |
| Alguem tirou 10? | `any(n == 10 ...)` | `True` |

---

### Exemplo 3 — Exercicio 60 (Nivel 1)

📋 **ENUNCIADO (ex. 60):** Catalogo em tuplas `(produto, preco)`. Exibir soma total e produto mais caro.

👤 **SUA SOLUCAO (acumulador manual):**

```python
for i, (produto, preco) in enumerate(catalogo):
    if i == 0:
        total_precos = preco
        preco_mais_caro = preco
        produto_mais_caro = produto
    else:
        total_precos += preco
        if preco > preco_mais_caro:
            produto_mais_caro = produto
            preco_mais_caro = preco
```

⚡ **COM `sum` e `max`:**

```python
catalogo = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90), ("lapis", 1.50)]
precos = [preco for _, preco in catalogo]
total = sum(precos)
produto_mais_caro, preco_mais_caro = max(catalogo, key=lambda item: item[1])
```

| Linha | Explicacao |
|-------|------------|
| `precos = [preco for _, preco in catalogo]` | List comprehension extrai so os precos |
| `sum(precos)` | Soma direta — substitui o acumulador do loop |
| `max(catalogo, key=lambda item: item[1])` | Encontra tupla com maior preco (indice 1) |

---

### Exemplo 4 — Nivel 2: combinando conceitos (ex. 41 — presencas simuladas)

📋 Contexto: lista fixa de presencas (sem input) para estudar logica.

```python
presencas = ["S", "S", "N", "S", "S", "S", "S", "S", "S", "S", "S", "S"]
```

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 1 | `presencas = [...]` | 12 respostas simuladas (S=presente, N=falta) |
| 2 | `sum(1 for p in presencas if p == "S")` | Conta quantos "S" existem (11) |
| 3 | `>= 9` | Verifica se atingiu minimo (75% de 12 = 9) |
| 4 | `all(p == "S" for p in presencas)` | True so se **nenhuma** falta |
| 5 | `any(p == "N" for p in presencas)` | True se **existe** pelo menos uma falta |

```python
total_presencas = sum(1 for p in presencas if p == "S")
frequentou_minimo = total_presencas >= 9
todas_presentes = all(p == "S" for p in presencas)
alguma_falta = any(p == "N" for p in presencas)
print(total_presencas, frequentou_minimo, todas_presentes, alguma_falta)
# 11 True False True
```

---

### Exemplo 5 — Nivel 2: contexto escolar

```python
notas_bimestre = [6.0, 7.5, 4.0, 8.0, 5.5]
media_bim = sum(notas_bimestre) / len(notas_bimestre)
precisa_atencao = any(n < 5 for n in notas_bimestre)
pode_parabenizar = all(n >= 7 for n in notas_bimestre)
```

---

### Exemplo 6 — Nivel 3: GeoExplorer (ex. 49)

```python
list_coordenadas = [("Serra da Capivara", -8.67, -42.55), ("Teresina", -5.09, -42.80)]
media_lat = sum(lat for _, lat, _ in list_coordenadas) / len(list_coordenadas)
tem_ponto_norte = any(lat > 0 for _, lat, _ in list_coordenadas)
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| `sum` para somar numeros de lista | `sum` em strings (use `"".join`) |
| `any` para "existe algum?" | loop so para achar 1 item — use `any` |
| `all` para validar regras globais | `all` em lista vazia (retorna `True`!) |

**Onde aparece mais:** analise de notas, estatisticas simples, validacao de formularios, dashboards educacionais.

---

### ⚠️ Erros comuns

1. `all([])` retorna `True` — cuidado com listas vazias.
2. `sum` so funciona com numeros; para concatenar strings use join.
3. Confundir `any` (basta um) com `all` (precisa todos).

---

### 🎯 Mini-desafio

Dada `temperaturas = [68, 72, 85, 91, 70]`, escreva uma linha com `any` que detecte se alguma temperatura e critica (>70).

<details>
<summary>Gabarito</summary>

```python
critico = any(t > 70 for t in temperaturas)  # True
```
</details>

**Resumo:** `sum` agrega; `any`/`all` respondem perguntas logicas sobre colecoes.

---

# 2. Operador ternario (if inline)

## O que e

Forma compacta de escolher entre **dois valores** com base em uma condicao.

**Sintaxe:** `valor_se_true if condicao else valor_se_false`

---

### Exemplo 1 — Exercicio 41 (Nivel 1)

📋 **ENUNCIADO (ex. 41):** 12 aulas. Contar presencas. Aprovado se frequencia >= 75%.

👤 **SUA SOLUCAO:**

```python
percentual_presenca = (cont_presenca * 100) / total_aulas
if percentual_presenca >= 75:
    print(f'ALUNO APROVADO COM {percentual_presenca:.1f}% DE PRESENÇA')
else:
    print(f'ALUNO REPROVADO COM {percentual_presenca:.1f}% DE PRESENÇA')
```

⚡ **COM TERNARIO:**

```python
percentual_presenca = (cont_presenca * 100) / total_aulas
situacao = "APROVADO" if percentual_presenca >= 75 else "REPROVADO"
cor = "green" if percentual_presenca >= 75 else "red"
print(f'ALUNO {situacao} COM {percentual_presenca:.1f}% DE PRESENÇA')
```

| Linha | Explicacao |
|-------|------------|
| `situacao = "APROVADO" if ... else "REPROVADO"` | Se >= 75, guarda "APROVADO"; senao "REPROVADO" |
| Expressao inteira e **um valor** atribuido a uma variavel | Substitui bloco if/else de 4 linhas por 1 |

---

### Exemplo 2 — Exercicio 58 (Nivel 1)

📋 **ENUNCIADO (ex. 58):** Tuplas `(nome, nota1, nota2)`. Exibir media de cada aluno.

👤 **SUA SOLUCAO:**

```python
for i, (aluno, nota1, nota2) in enumerate(alunos):
    media = (nota1 + nota2) / 2
    if media >= 7:
        print(f"... //green/Média: {media:.2f}/green")
    else:
        print(f"... //red/Média: {media:.2f}/red")
```

⚡ **COM TERNARIO:**

```python
for i, (aluno, nota1, nota2) in enumerate(alunos):
    media = (nota1 + nota2) / 2
    cor = "green" if media >= 7 else "red"
    status = "Adequado" if media >= 7 else "Atenção"
    print(f"{i+1} | Aluno: {aluno} | //{cor}/Média: {media:.2f} ({status})/{cor}")
```

---

### Exemplo 3 — Exercicio 45 (Nivel 1)

📋 **ENUNCIADO (ex. 45):** Monitor de temperatura. Normal (0-70), critico (>70), negativo encerra.

👤 **SUA SOLUCAO:** `if/elif/else` com 3 ramos e mensagens longas.

⚡ **COM TERNARIO (apenas classificacao, nao substitui logica de parada):**

```python
temperatura = float(input("Temperatura: ").replace(",", "."))
if temperatura < 0:
    print("Falha no sensor!")
else:
    estado = "critico" if temperatura > 70 else "normal"
    msg = f"CRÍTICO: {temperatura}°C" if temperatura > 70 else f"Normal: {temperatura}°C"
    print(msg)
```

> Ternario funciona bem para **2 opcoes**. Com 3+ estados, `if/elif` continua mais legivel.

---

### Exemplo 4 — Nivel 2

```python
nota = 5.5
conceito = "A" if nota >= 9 else "B" if nota >= 7 else "C" if nota >= 5 else "D"
# Encadeado possivel, mas fica denso — prefira if/elif para 4+ faixas
```

---

### Exemplo 5 — Nivel 2

```python
estoque = 0
status_loja = "Disponível" if estoque > 0 else "Esgotado"
```

---

### Exemplo 6 — Nivel 3

```python
curtidas = 250
nivel = "alto" if curtidas > 300 else "medio" if curtidas > 100 else "baixo"
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Escolha entre 2 strings/valores | Logica com efeitos colaterais (print, append) |
| Atribuir status, cor, rotulo | Mais de 2-3 ramos encadeados |
| Expressoes curtas dentro de f-string | Ternario dentro de ternario dentro de ternario |

---

### ⚠️ Erros comuns

1. Usar ternario para executar `print` nos dois lados — fica ilegivel.
2. Encadear muitos `if else` — volte ao `if/elif`.
3. Esquecer que ternario **retorna valor**, nao substitui blocos com varias linhas.

---

### 🎯 Mini-desafio

Com `idade = 15`, atribua `"menor"` ou `"maior"` em uma linha.

<details><summary>Gabarito</summary>

```python
categoria = "menor" if idade < 18 else "maior"
```
</details>

**Resumo:** ternario = atalho para decisao binaria simples.

---

# 3. enumerate()

## O que e

Entrega **indice + valor** ao percorrer uma sequencia, sem `range(len())`.

**Sintaxe:** `for indice, valor in enumerate(lista, start=0):`

---

### Exemplo 1 — Exercicio 67 (Nivel 1) — sua solucao JA usa enumerate

📋 **ENUNCIADO:** Listar disciplinas com numero comecando em 1.

👤 **SUA SOLUCAO:**

```python
disciplinas = ["Matematica", "Portugues", "Ciencias", "Historia", "Geografia"]
for i, (d) in enumerate(disciplinas, start=1):
    print(f"{i:<5}| {d}")
```

| Linha | Explicacao |
|-------|------------|
| `enumerate(disciplinas, start=1)` | Gera pares (1,"Matematica"), (2,"Portugues")... |
| `i, (d)` | `i` = numero; `d` = nome da disciplina |
| `{i:<5}` | Formata indice alinhado a esquerda com 5 caracteres |

⚡ **Forma antiga (sem enumerate) — para comparar:**

```python
for i in range(len(disciplinas)):
    print(f"{i+1:<5}| {disciplinas[i]}")
```

Voce **ja domina** enumerate. A comparacao mostra por que e melhor: menos indices manuais, menos erro off-by-one.

---

### Exemplo 2 — Exercicio 57 (Nivel 2)

📋 **ENUNCIADO (ex. 57):** Lista de tuplas `(nome, idade, cidade)`. Exibir cada registro.

👤 **SUA SOLUCAO:**

```python
for i, (nome, idade, cidade) in enumerate(usuarios):
    print(f"{i + 1} | Nome: {nome} ... | Idade: {idade} | Cidade: {cidade}")
```

| Linha | Explicacao |
|-------|------------|
| `enumerate(usuarios)` | Indice comeca em 0 por padrao |
| `(nome, idade, cidade)` | Unpacking da tupla dentro do for |
| `i + 1` | Converte indice 0-based para exibicao 1-based |

⚡ **Com `start=1` (elimina o +1):**

```python
for num, (nome, idade, cidade) in enumerate(usuarios, start=1):
    print(f"{num} | Nome: {nome} | Idade: {idade} | Cidade: {cidade}")
```

---

### Exemplo 3 — Exercicio 49 (Nivel 3)

👤 **SUA SOLUCAO (GeoExplorer):**

```python
for i, (nome, latitude, longitude) in enumerate(list_coordenadas, start=1):
    print(f"{i:02d}. {nome} │ Latitude: {latitude} │ Longitude: {longitude}")
```

| Linha | Explicacao |
|-------|------------|
| `start=1` | Numeracao humana (1, 2, 3...) |
| `{i:02d}` | Indice com 2 digitos e zero a esquerda (01, 02...) |
| unpacking de 3 valores | Acessa nome e coordenadas sem indices |

---

### Exemplo 4 — Nivel 2: encontrar posicao de item

```python
disciplinas = ["Matematica", "Portugues", "Ciencias"]
for i, d in enumerate(disciplinas):
    if d == "Ciencias":
        print(f"Ciencias esta na posicao {i}")  # posicao 2 (0-based)
```

---

### Exemplo 5 — Nivel 2: numerar ranking

```python
notas_ordenadas = sorted([8, 6, 9, 7], reverse=True)
for posicao, nota in enumerate(notas_ordenadas, start=1):
    print(f"{posicao}o lugar: nota {nota}")
```

---

### Exemplo 6 — Nivel 3: mapa Folium (ex. 49)

```python
for i, (nome, lat, long) in enumerate(list_coordenadas, start=1):
    cor = "green" if i == 1 else "red" if i == len(list_coordenadas) else "blue"
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Precisa do indice E do valor | So precisa dos valores (use `for item in lista`) |
| Numeracao customizada (`start=1`) | Indice complexo derivado de outra logica |

---

### ⚠️ Erros comuns

1. Esquecer `start=1` e somar 1 manualmente (funciona, mas e redundante).
2. Confundir indice enumerate (0-based) com "numero da questao" sem ajuste.
3. Usar `enumerate` quando so precisa do valor.

---

### 🎯 Mini-desafio

Exiba `1. Ana`, `2. Bruno` para `nomes = ["Ana", "Bruno"]`.

<details><summary>Gabarito</summary>

```python
for n, nome in enumerate(nomes, start=1):
    print(f"{n}. {nome}")
```
</details>

**Resumo:** enumerate = indice + valor no mesmo loop.

---

# 4. zip()

## O que e

Combina **duas ou mais listas** elemento a elemento, como um "zipper".

**Sintaxe:** `for a, b in zip(lista1, lista2):`

---

### Exemplo 1 — Exercicio 58 (Nivel 1)

📋 **ENUNCIADO:** Tuplas `(nome, nota1, nota2)`. Voce usou tuplas; zip aparece quando listas estao **separadas**.

👤 **Forma equivalente com listas separadas (como voce poderia receber dados):**

```python
nomes = ["Ana", "Bruno", "Carla"]
nota1 = [8.0, 5.0, 9.0]
nota2 = [6.0, 7.0, 10.0]
for i in range(len(nomes)):
    media = (nota1[i] + nota2[i]) / 2
    print(f"{nomes[i]}: {media:.2f}")
```

⚡ **COM zip + enumerate:**

```python
for i, (nome, n1, n2) in enumerate(zip(nomes, nota1, nota2), start=1):
    media = (n1 + n2) / 2
    status = "Adequado" if media >= 7 else "Atenção"
    print(f"{i} | {nome}: {media:.2f} ({status})")
```

| Linha | Explicacao |
|-------|------------|
| `zip(nomes, nota1, nota2)` | Junta ("Ana",8.0,6.0), ("Bruno",5.0,7.0)... |
| `enumerate(..., start=1)` | Adiciona numeracao |
| unpacking `(nome, n1, n2)` | Separa os 3 valores de cada "fileira" |

---

### Exemplo 2 — Exercicio 68 (Nivel 1)

📋 **ENUNCIADO:** Classificar notas em listas.

👤 **SUA SOLUCAO:** um `for c in notas` com append.

⚡ **Com zip (quando ha nomes junto):**

```python
alunos = ["A","B","C","D","E","F","G","H","I","J"]
notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]
for nome, nota in zip(alunos, notas):
    if nota >= 6:
        print(f"{nome}: aprovado ({nota})")
```

---

### Exemplo 3 — Exercicio 60 (Nivel 1)

📋 **ENUNCIADO:** Catalogo `(produto, preco)`.

⚡ **zip separando colunas:**

```python
catalogo = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90)]
produtos, precos = zip(*catalogo)  # unzip!
print(sum(precos))
print(max(produtos, key=lambda p: catalogo[[x[0] for x in catalogo].index(p)]))
# Forma mais simples para max preco:
print(max(catalogo, key=lambda x: x[1]))
```

| Linha | Explicacao |
|-------|------------|
| `zip(*catalogo)` | Desempacota lista de tuplas em duas tuplas |
| `produtos` | ("caderno", "caneta", "mochila") |
| `precos` | (24.90, 2.50, 89.90) |

---

### Exemplo 4 — Nivel 2: dicionario com zip

```python
alunos = ["Ana", "Bruno", "Carla"]
notas = [8.0, 6.5, 9.0]
boletim = dict(zip(alunos, notas))
# {'Ana': 8.0, 'Bruno': 6.5, 'Carla': 9.0}
```

---

### Exemplo 5 — Nivel 2: percorrer duas listas de tamanhos diferentes

```python
list(zip([1,2,3], ["a","b"]))  # [(1,'a'), (2,'b')] — para na menor!
```

---

### Exemplo 6 — Nivel 3: coordenadas (ex. 49)

```python
nomes = [n for n, _, _ in list_coordenadas]
lats = [lat for _, lat, _ in list_coordenadas]
for nome, lat in zip(nomes, lats):
    print(f"{nome}: lat {lat}")
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Duas listas paralelas (nomes + notas) | Dados ja estao em tuplas/dicionarios |
| Criar dict com `dict(zip(keys, vals))` | Listas de tamanhos muito diferentes (corta!) |

---

### ⚠️ Erros comuns

1. `zip` para na lista **menor** — pode perder dados silenciosamente.
2. Usar indice manual quando `zip` resolveria.
3. Esquecer que `zip` retorna iterador (no Py3) — converta para lista se precisar reusar.

---

### 🎯 Mini-desafio

Junte `disciplinas = ["Mat","Por"]` e `carga = [4,3]` e exiba "Mat: 4h".

<details><summary>Gabarito</summary>

```python
for d, h in zip(disciplinas, carga):
    print(f"{d}: {h}h")
```
</details>

**Resumo:** zip = percorrer listas "lado a lado".

---

# 5. Desempacotamento (unpacking)

## O que e

Atribuir multiplos valores de uma tupla/lista a variaveis de uma vez.

**Sintaxe:** `a, b, c = tupla` ou `primeiro, *meio, ultimo = lista`

---

### Exemplo 1 — Exercicio 57 (Nivel 1)

📋 **ENUNCIADO:** `pessoa = ("Ana", 30, "Recife")` → tres variaveis.

👤 **SUA SOLUCAO (comentada no codigo + loop):**

```python
# nome, idade, cidade = pessoa
for i, (nome, idade, cidade) in enumerate(usuarios):
    print(f"{i+1} | Nome: {nome} | Idade: {idade} | Cidade: {cidade}")
```

| Linha | Explicacao |
|-------|------------|
| `(nome, idade, cidade)` | Parenteses no for indicam unpacking da tupla interna |
| Cada iteracao | `usuarios[i]` e uma tupla de 3 — desmontada em 3 vars |

⚡ **Unpacking direto (enunciado original):**

```python
pessoa = ("Ana", 30, "Recife")
nome, idade, cidade = pessoa
print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
```

---

### Exemplo 2 — Exercicio 58 (Nivel 1)

👤 **SUA SOLUCAO:**

```python
for i, (aluno, nota1, nota2) in enumerate(alunos):
    media = (nota1 + nota2) / 2
```

| Parte | Explicacao |
|-------|------------|
| `(aluno, nota1, nota2)` | Desempacota tupla de 3 elementos |
| `media = (nota1 + nota2) / 2` | Usa variaveis ja separadas |

---

### Exemplo 3 — Exercicio 49 (Nivel 3)

👤 **SUA SOLUCAO:**

```python
for nome, latitude, longitude in list_coordenadas:
    dados.append({"nome": nome, "latitude": latitude, "longitude": longitude})

media_lat = sum(lat for _, lat, _ in list_coordenadas) / len(list_coordenadas)
```

| Linha | Explicacao |
|-------|------------|
| `for nome, latitude, longitude in ...` | Unpacking no loop |
| `_` em generator | Ignora nome e longitude — so quer latitude |

---

### Exemplo 4 — Nivel 2: troca de variaveis

```python
a, b = 10, 20
a, b = b, a  # troca sem variavel temporaria
```

---

### Exemplo 5 — Nivel 2: *resto

```python
notas = [7.5, 8.0, 6.5, 9.0, 4.0]
primeira, *resto, ultima = notas
# primeira=7.5, resto=[8.0,6.5,9.0], ultima=4.0
```

---

### Exemplo 6 — Nivel 3: zip + unpacking

```python
produto, preco = ("mochila", 89.90)
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Tuplas com poucos campos fixos | Estruturas com campos variaveis (use dict) |
| `_` para valores ignorados | Unpacking com quantidade errada (ValueError!) |

---

### ⚠️ Erros comuns

1. `a, b = (1, 2, 3)` → erro: muitos valores.
2. Esquecer parenteses no `for`: `for x, y in lista_de_tuplas`.
3. Nao usar `_` por convencao para "nao vou usar este valor".

---

### 🎯 Mini-desafio

Desempacote `(10, 20, 30)` em `x, y, z`.

<details><summary>Gabarito</summary>

```python
t = (10, 20, 30)
x, y, z = t
```
</details>

**Resumo:** unpacking = desmontar tupla/lista em variaveis nomeadas.

---

# 6. Context manager (with)

## O que e

Garante que recursos (arquivo, conexao) sejam **fechados automaticamente**, mesmo se der erro.

**Sintaxe:** `with open(caminho, "r") as arquivo:`

---

### Exemplo 1 — Exercicio 49 (Nivel 3) — voce JA usa with

📋 **ENUNCIADO (ex. 49):** Salvar coordenadas em JSON.

👤 **SUA SOLUCAO:**

```python
with open(caminho_json, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
```

| Linha | Explicacao |
|-------|------------|
| `with open(...) as arquivo` | Abre arquivo e garante fechamento ao sair do bloco |
| `"w"` | Modo escrita (write) |
| `encoding="utf-8"` | Suporta acentos (São Luís, etc.) |
| `json.dump(dados, arquivo, ...)` | Escreve dict/lista Python como JSON no arquivo |
| `indent=4` | JSON formatado (legivel) |
| `ensure_ascii=False` | Mantem caracteres especiais |

⚡ **SEM with (nao recomendado):**

```python
arquivo = open(caminho_json, "w", encoding="utf-8")
json.dump(dados, arquivo)
arquivo.close()  # se der erro antes, arquivo pode ficar aberto/corrompido
```

---

### Exemplo 2 — Exercicio 125 (Nivel 1 — enunciado do repo)

📋 **ENUNCIADO (ex. 125):** Ler arquivo de texto com tratamento de erro.

⚡ **COM with + try/except:**

```python
while True:
    nome = input("Nome do arquivo: ")
    try:
        with open(nome, "r", encoding="utf-8") as f:
            conteudo = f.read()
        print(conteudo)
        break
    except FileNotFoundError:
        print("Arquivo nao encontrado. Tente novamente.")
```

| Linha | Explicacao |
|-------|------------|
| `try` | Tenta executar bloco |
| `with open(...) as f` | Abre e fecha automaticamente |
| `f.read()` | Le todo o conteudo |
| `except FileNotFoundError` | Captura erro de arquivo inexistente |

---

### Exemplo 3 — Comparacao com exercicio 49 (leitura do JSON)

⚡ **Ler o JSON que voce salvou:**

```python
with open(caminho_json, "r", encoding="utf-8") as f:
    dados_carregados = json.load(f)
for ponto in dados_carregados:
    print(ponto["nome"], ponto["latitude"])
```

---

### Exemplo 4 — Nivel 2: escrever relatorio de turma

```python
with open("relatorio.txt", "w", encoding="utf-8") as f:
    f.write("RELATORIO DE NOTAS\n")
    f.write("-" * 30 + "\n")
    for linha in linhas_relatorio:
        f.write(linha + "\n")
```

---

### Exemplo 5 — Nivel 2: with em outros contextos

```python
# easyansi.activate() tambem e um contexto de configuracao
# with funciona com qualquer objeto que implemente __enter__ e __exit__
```

---

### Exemplo 6 — Nivel 3: padrao completo GeoExplorer

Fluxo do seu ex. 49: cadastro → monta `dados` → `with open` → `json.dump` → Folium gera HTML.

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Sempre com `open()` | `open()` sem fechar em scripts longos |
| Leitura/escrita de JSON, CSV, txt | Quando biblioteca ja abstrai (pandas, etc.) |

---

### ⚠️ Erros comuns

1. Esquecer `encoding="utf-8"` no Windows → acentos quebram.
2. Modo `"w"` apaga arquivo existente sem aviso.
3. Ler arquivo fora do bloco `with` (arquivo ja fechado).

---

### 🎯 Mini-desafio

Escreva "Ola" em `teste.txt` com `with`.

<details><summary>Gabarito</summary>

```python
with open("teste.txt", "w", encoding="utf-8") as f:
    f.write("Ola")
```
</details>

**Resumo:** with = abrir, usar, fechar com seguranca.

---

# 7. List comprehension

## O que e

Cria uma **nova lista** em uma linha a partir de um loop + filtro/transformacao.

**Sintaxe:** `[expressao for item in lista if condicao]`

---

### Exemplo 1 — Exercicio 68 (Nivel 1)

📋 **ENUNCIADO:** Separar aprovados, recuperacao, reprovados.

👤 **SUA SOLUCAO (loop + append):**

```python
list_aprovados = []
for c in notas:
    if c >= 6:
        list_aprovados.append(c)
    elif c >= 4:
        list_recuperacao.append(c)
    else:
        list_reprovados.append(c)
```

⚡ **COM list comprehension:**

```python
list_aprovados = [c for c in notas if c >= 6]
list_recuperacao = [c for c in notas if 4 <= c < 6]
list_reprovados = [c for c in notas if c < 4]
```

| Linha | Explicacao |
|-------|------------|
| `[c for c in notas if c >= 6]` | Para cada nota, se >=6, inclui na nova lista |
| `c` antes do `for` | O que entra na lista (pode ser transformado: `c*2`) |
| `if` no final | Filtro opcional |

```
┌─ for + append (3 listas) ─────┐    ┌─ 3 comprehensions ──────────┐
│  ~12 linhas                   │ →  │  3 linhas                   │
└───────────────────────────────┘    └─────────────────────────────┘
```

---

### Exemplo 2 — Exercicio 72 (Nivel 1)

👤 **SUA SOLUCAO:**

```python
for c in curtidas:
    if c >= 0 and c <= 100:
        baixo.append(c)
    elif c >= 101 and c <= 300:
        medio.append(c)
    else:
        alto.append(c)
```

⚡ **COM comprehension:**

```python
baixo = [c for c in curtidas if 0 <= c <= 100]
medio = [c for c in curtidas if 101 <= c <= 300]
alto = [c for c in curtidas if c > 300]
```

---

### Exemplo 3 — Exercicio 37 (Nivel 1)

👤 **Contagem acima de 6 com loop:**

```python
notas_acima_6 = 0
for n in notas:
    if n > 6:
        notas_acima_6 += 1
```

⚡ **Com comprehension:**

```python
notas_acima_6 = len([n for n in notas if n > 6])
# ou: sum(1 for n in notas if n > 6)
```

---

### Exemplo 4 — Nivel 2: transformacao

```python
notas = [7.5, 8.0, 6.0]
notas_inteiro = [int(n) for n in notas]  # [7, 8, 6]
```

---

### Exemplo 5 — Nivel 2: strings

```python
nomes = ["  ana  ", " BRUNO "]
nomes_limpos = [n.strip().title() for n in nomes]
```

---

### Exemplo 6 — Nivel 3: extrair latitudes (ex. 49)

```python
lats = [lat for _, lat, _ in list_coordenadas]
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Filtrar/transformar listas | Efeitos colaterais (print, input) |
| 1 nivel de loop | Comprehension aninhada (dificil de ler) |
| Resultado e uma lista | Logica muito longa (use funcao + loop) |

---

### ⚠️ Erros comuns

1. Comprehension aninhada demais → volte ao for.
2. Esquecer colchetes `[]` — `( )` cria generator, nao lista.
3. Modificar lista original dentro da comprehension — crie nova lista.

---

### 🎯 Mini-desafio

De `[1,2,3,4,5]`, crie lista so de pares.

<details><summary>Gabarito</summary>

```python
pares = [n for n in [1,2,3,4,5] if n % 2 == 0]  # [2, 4]
```
</details>

**Resumo:** comprehension = loop + filtro compacto para listas.

---

# 8. Dict comprehension

## O que e

Cria um **dicionario** de forma compacta, como list comprehension para dicts.

**Sintaxe:** `{chave: valor for item in iteravel if condicao}`

---

### Exemplo 1 — Exercicio 77 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 77):** `notas = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}` — percorrer.

⚡ **Dict comprehension — filtrar aprovados:**

```python
notas = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
aprovados = {aluno: n for aluno, n in notas.items() if n >= 7}
# {'Ana': 8.0, 'Carla': 9.0}
```

| Linha | Explicacao |
|-------|------------|
| `{aluno: n for ...}` | Chave = nome, valor = nota |
| `notas.items()` | Pares (aluno, nota) |
| `if n >= 7` | Filtro |

---

### Exemplo 2 — Exercicio 82 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 82):** Atualizar estoque apos vendas.

👤 **Forma com loop (como voce faria):**

```python
estoque = {"camiseta": 20, "calca": 15, "tenis": 10}
vendas = {"camiseta": 3, "calca": 5, "tenis": 2}
for produto, qtd_vendida in vendas.items():
    if produto in estoque:
        estoque[produto] = max(0, estoque[produto] - qtd_vendida)
```

⚡ **COM dict comprehension:**

```python
estoque_atualizado = {
    p: max(0, estoque[p] - vendas.get(p, 0))
    for p in estoque
}
```

---

### Exemplo 3 — Exercicio 49 (Nivel 3)

👤 **SUA SOLUCAO (loop + append dicts):**

```python
dados = []
for nome, latitude, longitude in list_coordenadas:
    dados.append({"nome": nome, "latitude": latitude, "longitude": longitude})
```

⚡ **List comprehension de dicts (padrao similar):**

```python
dados = [
    {"nome": n, "latitude": lat, "longitude": lon}
    for n, lat, lon in list_coordenadas
]
```

---

### Exemplo 4 — Nivel 2: inverter chave-valor

```python
notas = {"Ana": 8.0, "Bruno": 6.5}
# Cuidado: valores duplicados perdem chaves
# Boletim reverso so se valores forem unicos
```

---

### Exemplo 5 — Nivel 2: contagem de frequencia

```python
presencas = ["S","S","N","S","N"]
freq = {p: presencas.count(p) for p in set(presencas)}
```

---

### Exemplo 6 — Nivel 3: zip + dict comprehension

```python
alunos = ["Ana", "Bruno"]
notas = [8.0, 6.5]
boletim = {a: n for a, n in zip(alunos, notas)}
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Filtrar/transformar dicionarios | Logica complexa com muitos elif |
| Criar dict a partir de listas (`zip`) | Dict comprehension ilegivel (quebre em funcao) |

---

### ⚠️ Erros comuns

1. Usar `{x for x in ...}` — isso e **set**, nao dict (falta `:`).
2. Modificar dict durante comprehension do mesmo dict.
3. Comprehension muito longa — prefira loop explicito.

---

### 🎯 Mini-desafio

De `{"a":1,"b":2,"c":3}`, crie dict so com valores pares.

<details><summary>Gabarito</summary>

```python
d = {"a":1,"b":2,"c":3}
pares = {k: v for k, v in d.items() if v % 2 == 0}  # {'b': 2}
```
</details>

**Resumo:** dict comprehension = montar/filtrar dicionarios em uma expressao.

---

# 9. Lambda

## O que e

Funcao **anonima** de uma linha, util para operacoes rapidas (sort, filter, map).

**Sintaxe:** `lambda parametros: expressao`

---

### Exemplo 1 — Exercicio 100 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 100):** Filtrar notas >= 6 com `filter()` + lambda.

⚡ **SOLUCAO COM LAMBDA:**

```python
notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]
aprovados = list(filter(lambda n: n >= 6, notas))
print(aprovados)
print(len(aprovados))
```

| Linha | Explicacao |
|-------|------------|
| `lambda n: n >= 6` | Funcao que retorna True/False para cada nota |
| `filter(funcao, notas)` | Mantem elementos onde funcao retorna True |
| `list(...)` | Converte iterador em lista |

👤 **SUA FORMA EQUIVALENTE (ex. 68, sem lambda):**

```python
list_aprovados = [c for c in notas if c >= 6]
```

Ambas resolvem — lambda brilha com `filter`/`sorted`; comprehension e mais "pythonica" para filtrar.

---

### Exemplo 2 — Exercicio 99 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 99):** Ordenar produtos `(nome, preco)` pelo preco.

⚡ **COM lambda em sorted:**

```python
produtos = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90)]
baratos = sorted(produtos, key=lambda item: item[1])
caros = sorted(produtos, key=lambda item: item[1], reverse=True)
```

| Linha | Explicacao |
|-------|------------|
| `key=lambda item: item[1]` | Diz ao sorted: "ordene pelo indice 1 (preco)" |
| `reverse=True` | Do maior para menor |

👤 **SUA REFERENCIA (ex. 65 — sorted sem lambda):**

```python
sorted(numeros)  # lista simples — nao precisa de key
```

---

### Exemplo 3 — Exercicio 98 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 98):** Lambda com condicao.

⚡ **Exemplo:**

```python
classificar = lambda n: "aprovado" if n >= 6 else "recuperacao" if n >= 4 else "reprovado"
print(classificar(7.5))  # aprovado
```

---

### Exemplo 4 — Exercicio 96 (Nivel 1)

📋 **ENUNCIADO:** Lambda `dobro`.

```python
dobro = lambda x: x * 2
print(dobro(5), dobro(10), dobro(25))
```

---

### Exemplo 5 — Nivel 2: map + lambda

```python
notas = [7.5, 8.0, 6.0]
arredondadas = list(map(lambda n: round(n), notas))
```

---

### Exemplo 6 — Nivel 3: max no catalogo (ex. 60)

```python
catalogo = [("caderno", 24.90), ("mochila", 89.90)]
produto, preco = max(catalogo, key=lambda x: x[1])
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| `key=` em sorted | Logica de 5+ linhas |
| filter/map pontuais | Funcao reutilizada em varios lugares (use def) |
| Callback simples | Lambda que confunde quem le |

---

### ⚠️ Erros comuns

1. Tentar multiplas linhas na lambda (nao pode).
2. Usar lambda onde list comprehension e mais clara.
3. Esquecer `list()` no resultado de filter/map.

---

### 🎯 Mini-desafio

Ordene `[("b",2),("a",3)]` pela letra.

<details><summary>Gabarito</summary>

```python
sorted([("b",2),("a",3)], key=lambda t: t[0])
```
</details>

**Resumo:** lambda = funcao descartavel de 1 expressao.

---

# 10. *args e **kwargs

## O que e

Permitem funcoes aceitarem **quantidade variavel** de argumentos.

- `*args` → tupla de argumentos posicionais extras
- `**kwargs` → dicionario de argumentos nomeados extras

---

### Exemplo 1 — Exercicio 91 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 91):** Funcoes separadas: media, situacao, maior, menor nota.

👤 **Forma modular (como pedido):**

```python
def calcular_media(notas):
    return sum(notas) / len(notas)

def maior_nota(notas):
    return max(notas)

def menor_nota(notas):
    return min(notas)
```

⚡ **Funcao generica com *args (soma qualquer quantidade):**

```python
def somar(*args):
    return sum(args)

print(somar(7.5, 3.2, 8.0))  # 18.7
print(somar(1, 2, 3, 4, 5))  # 15
```

| Linha | Explicacao |
|-------|------------|
| `*args` | Agrupa todos os argumentos posicionais em tupla |
| `sum(args)` | Soma a tupla |

---

### Exemplo 2 — Exercicio 88 (Nivel 1 — enunciado)

📋 **ENUNCIADO (ex. 88):** `def saudacao(nome):`

⚡ **Generalizando com *args:**

```python
def saudacao(*nomes):
    for nome in nomes:
        print(f"Ola, {nome}! Tudo bem?")

saudacao("Ana", "Bruno", "Carla")
```

---

### Exemplo 3 — Exercicio 49 (Nivel 3)

👤 **SUA FUNCAO `ler_coordenada(tipo)`** — 1 parametro fixo.

⚡ **Versao com **kwargs para configuracao:**

```python
def exibir_alerta(mensagem, **kwargs):
    cor = kwargs.get("cor", "cyan")
    negrito = kwargs.get("negrito", False)
    prefixo = "//bold-" if negrito else "//"
    print(f"{prefixo}{cor}/{mensagem}/{cor}")

exibir_alerta("Coordenada salva!", cor="green", negrito=True)
```

| Linha | Explicacao |
|-------|------------|
| `**kwargs` | Captura argumentos nomeados extras como dict |
| `kwargs.get("cor", "cyan")` | Valor padrao se nao passou |

---

### Exemplo 4 — Nivel 2: combinando *args e **kwargs

```python
def relatorio(*args, **kwargs):
    print("Notas:", args)
    print("Turma:", kwargs.get("turma", "N/A"))

relatorio(7.5, 8.0, 6.5, turma="9A", professor="Gustavo")
```

---

### Exemplo 5 — Nivel 2: encaminhar argumentos

```python
def calcular_media(*notas):
    return sum(notas) / len(notas) if notas else 0
```

---

### Exemplo 6 — Nivel 3: wrapper educacional

```python
def registrar_ponto(nome, *coordenadas, **meta):
    lat, lon = coordenadas
    return {"nome": nome, "lat": lat, "lon": lon, **meta}

p = registrar_ponto("Serra da Capivara", -8.67, -42.55, tipo="turismo")
```

---

### 💡 Quando usar / evitar

| Use | Evite |
|-----|-------|
| Funcoes flexiveis (utilitarios) | Funcoes com contrato fixo e claro |
| Wrappers e bibliotecas | Excesso de *args/**kwargs sem documentacao |
| Valores padrao via kwargs.get | Parametros obrigatorios escondidos |

---

### ⚠️ Erros comuns

1. Ordem errada: `def f(**kwargs, *args)` — invalido.
2. Nao documentar o que kwargs aceita.
3. Usar *args quando parametros nomeados seriam mais claros.

Ordem correta: `def f(a, b, *args, **kwargs)`

---

### 🎯 Mini-desafio

Crie funcao `multiplicar(*args)` que multiplica todos os numeros passados.

<details><summary>Gabarito</summary>

```python
def multiplicar(*args):
    resultado = 1
    for n in args:
        resultado *= n
    return resultado
```
</details>

**Resumo:** *args = varios posicionais; **kwargs = varios nomeados.

---

## Glossario

| Termo | Significado rapido |
|-------|-------------------|
| **Built-in** | Funcao nativa do Python (sum, len, max...) |
| **Comprehension** | Sintaxe compacta para criar list/dict/set |
| **Generator** | Iterador lazy (`x for x in lista`) |
| **Iterable** | Objeto que pode ser percorrido (lista, tupla, dict) |
| **Unpacking** | Desmontar sequencia em variaveis |
| **Context manager** | Objeto usado com `with` (gerencia recurso) |
| **Lambda** | Funcao anonima de uma expressao |
| **Key function** | Funcao que diz "por qual criterio ordenar" |

---

## Checklist final — voce terminou o material?

- [ ] Li todas as 10 estrategias
- [ ] Comparei pelo menos 3 exercicios meus em cada secao
- [ ] Fiz os 10 mini-desafios
- [ ] Consigo explicar a matriz de decisao de memoria
- [ ] Sei quando NAO usar cada recurso

---

<p align="center">
<strong>Material de estudo pessoal — Prof. Gustavo Franz</strong><br>
<em>Python Developer in Progress · github.com/GustaFranz</em>
</p>
