# Guia Git para iniciantes

Material criado durante meus estudos de programacao. Sou professor em transicao para a area de TI e compartilho aqui o que aprendo no caminho — nao como especialista, mas como alguem que ainda lembra das dificuldades iniciais.

**Se so lembrar de 3 comandos hoje:** `git status`, `git add .`, `git commit -m "mensagem"`.

---

## Indice

- [Objetivo](#objetivo)
- [Como usar](#como-usar)
- [Guia visual](#guia-visual)
- [Configuracao inicial](#configuracao-inicial)
- [Stage](#1-stage-area-de-preparacao)
- [Commits](#2-commits-salvando-alteracoes)
- [Branches](#3-branches-linhas-de-trabalho)
- [Merge](#4-mesclando-merge)
- [Envio e atualizacao](#5-envio-e-atualizacao-github)
- [Clone vs pull vs fetch](#clone-vs-pull-vs-fetch)
- [Fluxo recomendado](#fluxo-de-trabalho-recomendado)
- [Pull Request](#pull-request)
- [Conceitos importantes](#conceitos-importantes)
- [Boas praticas](#boas-praticas)
- [Comandos de emergencia](#comandos-de-emergencia)
- [Erros comuns](#erros-comuns)
- [Exercicio pratico](#exercicio-pratico)
- [Resumo rapido](#resumo-rapido)

---

## Objetivo

- Servir de referencia rapida para quem esta comecando com Git
- Complementar o guia visual com texto pesquisavel e comandos copiaveis
- Documentar erros comuns e um fluxo pratico de trabalho

---

## Como usar

1. Consulte a **imagem** abaixo para ter uma visao geral do fluxo
2. Use as **tabelas** deste README para copiar comandos no terminal
3. Em caso de erro, va direto para a secao [Erros comuns](#erros-comuns)
4. Pratique com o [Exercicio pratico](#exercicio-pratico) usando este repositorio

---

## Guia visual

![Git - Guia completo para iniciantes](./Git%20Guia%20completo.png)

---

## Configuracao inicial

Antes do primeiro commit, configure seu nome e e-mail (faca uma vez por maquina):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

Para baixar um repositorio pela primeira vez:

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

---

## 1. Stage (area de preparacao)

Area intermediaria onde voce escolhe o que vai entrar no proximo commit.

| Comando | Funcao |
|---------|--------|
| `git add arquivo.py` | Adiciona um arquivo especifico ao stage |
| `git add .` | Adiciona todos os arquivos modificados ao stage |
| `git status` | Mostra o que foi modificado e o que esta no stage |
| `git restore --staged arquivo.py` | Remove um arquivo do stage |

---

## 2. Commits (salvando alteracoes)

Cada commit e um "ponto de salvamento" no historico do projeto.

| Comando | Funcao |
|---------|--------|
| `git commit -m "mensagem"` | Salva as alteracoes do stage com uma mensagem |
| `git log` | Mostra o historico detalhado de commits |
| `git log --oneline` | Mostra o historico de forma resumida |
| `git diff` | Mostra diferencas ainda nao adicionadas ao stage |

---

## 3. Branches (linhas de trabalho)

Branches permitem trabalhar em funcionalidades em paralelo, sem misturar tudo na branch principal.

| Comando | Funcao |
|---------|--------|
| `git branch` | Lista todas as branches |
| `git branch nome-da-branch` | Cria uma nova branch |
| `git checkout nome-da-branch` | Troca para a branch indicada |
| `git switch nome-da-branch` | Troca para a branch (comando mais recente) |
| `git checkout -b nome-da-branch` | Cria e troca para a nova branch |

---

## 4. Mesclando (merge)

Juntar o trabalho de uma branch em outra (geralmente na `main`).

```bash
git checkout main
git merge nome-da-branch
```

---

## 5. Envio e atualizacao (GitHub)

Sincronizar seu repositorio local com o remoto (GitHub).

| Comando | Funcao |
|---------|--------|
| `git push -u origin nome-da-branch` | Envia a branch para o GitHub (primeira vez) |
| `git push` | Envia os commits da branch atual para o GitHub |
| `git pull` | Baixa e aplica alteracoes do GitHub no projeto local |
| `git fetch` | Baixa alteracoes do remoto sem aplicar (so informacao) |

**Dica:** sempre rode `git pull` antes de comecar a trabalhar, para evitar conflitos.

---

## Clone vs pull vs fetch

| Comando | Quando usar | O que faz |
|---------|-------------|-----------|
| `git clone` | Primeira vez, repo ainda nao existe na maquina | Copia o repositorio inteiro |
| `git pull` | Repo ja existe; voce quer atualizar e aplicar | Baixa e mescla alteracoes do remoto |
| `git fetch` | Quer ver o que mudou antes de aplicar | Baixa sem mesclar |

---

## Fluxo de trabalho recomendado

1. Atualize a branch principal: `git checkout main && git pull`
2. Crie uma branch para a funcionalidade: `git checkout -b nome-da-funcionalidade`
3. Faca suas alteracoes nos arquivos
4. Verifique o status: `git status`
5. Adicione ao stage: `git add .`
6. Faca o commit: `git commit -m "mensagem clara"`
7. Envie a branch: `git push -u origin nome-da-funcionalidade`
8. Abra um Pull Request no GitHub
9. Apos aprovacao, faca merge na `main`
10. Apague a branch (local e remota) se nao for mais necessaria

---

## Pull Request

Pull Request (PR) nao e um comando Git — e uma funcionalidade do GitHub.

1. Voce envia sua branch com `git push`
2. No GitHub, abre um PR pedindo para mesclar sua branch na `main`
3. Outra pessoa (ou voce mesmo) revisa as alteracoes
4. Apos aprovacao, o merge e feito pela interface do GitHub

---

## Conceitos importantes

| Conceito | Significado |
|----------|-------------|
| **Repositorio** | Pasta do projeto com historico de versoes |
| **Commit** | Registro de uma alteracao salva |
| **Branch** | Linha independente de desenvolvimento |
| **Merge** | Juntar alteracoes de uma branch em outra |
| **Stage** | Area onde voce prepara o que vai commitar |
| **Push** | Enviar commits locais para o remoto |
| **Pull** | Baixar e aplicar commits do remoto |
| **Remoto (remote)** | Versao do projeto hospedada (ex.: GitHub) |

---

## Boas praticas

- Faca commits frequentes, com mensagens claras
- Use uma branch por funcionalidade ou correcao
- Mantenha a branch `main` estavel
- Rode `git pull` antes de comecar a trabalhar
- Revise com `git status` antes de cada commit

---

## Comandos de emergencia

| Comando | Funcao |
|---------|--------|
| `git restore arquivo.py` | Descarta alteracoes nao commitadas no arquivo |
| `git reset --soft HEAD~1` | Desfaz o ultimo commit, mantendo alteracoes no stage |
| `git reset --hard HEAD~1` | Desfaz o ultimo commit e apaga alteracoes (**perigoso**) |

**Atencao:** `git reset --hard` apaga alteracoes de forma permanente. Use apenas se tiver certeza.

---

## Erros comuns

| Erro | Causa provavel | O que fazer |
|------|----------------|-------------|
| `fatal: not a git repository` | Voce nao esta dentro de uma pasta Git | Use `cd` ate a pasta do projeto |
| `Please tell me who you are` | Git sem nome/e-mail configurados | `git config --global user.name` e `user.email` |
| `rejected (fetch first)` | O remoto tem commits que voce ainda nao tem | Rode `git pull` antes do `git push` |
| `merge conflict` | Mesmo arquivo editado em lugares diferentes | Resolva manualmente, depois `git add` e `git commit` |
| `error: failed to push some refs` | Branch remota mais atualizada | `git pull --rebase` ou `git pull`, resolva conflitos, tente de novo |

### Exemplo de conflito de merge

```
<<<<<<< HEAD
seu codigo
=======
codigo do remoto
>>>>>>> branch-remota
```

Escolha o que manter (ou combine), remova os marcadores (`<<<<`, `====`, `>>>>`), depois:

```bash
git add arquivo.py
git commit -m "resolve conflito de merge"
```

---

## Exercicio pratico

Pratique o fluxo Git usando este repositorio:

1. Clone o repositorio (se ainda nao tiver):

```bash
git clone https://github.com/GustaFranz/exercicios_python.git
cd exercicios_python
```

2. Crie uma branch de teste:

```bash
git checkout -b teste-git-seu-nome
```

3. Faca uma alteracao pequena (ex.: uma linha em qualquer README).

4. Verifique, adicione e commite:

```bash
git status
git add .
git commit -m "teste: praticando fluxo git"
```

5. Envie para o GitHub:

```bash
git push -u origin teste-git-seu-nome
```

6. Abra um Pull Request no GitHub. Se for so treino, voce pode fechar depois sem fazer merge.

---

## Resumo rapido

Comandos mais usados no dia a dia:

```bash
git status
git add .
git commit -m "mensagem"
git push
git pull
git checkout -b nome-da-branch
git checkout main
git merge nome-da-branch
```

---

[Voltar ao README principal](../../README.md)
