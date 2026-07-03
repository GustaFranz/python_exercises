# Guia Git para iniciantes

**Link publico para compartilhar:** https://github.com/GustaFranz/exercicios_python/tree/main/materiais/git

Material criado durante meus estudos de programação. Sou professor em transição para a área de TI e compartilho aqui o que aprendo no caminho — não como especialista, mas como alguém que ainda lembra das dificuldades iniciais.

**Se só lembrar de 3 comandos hoje:** `git status`, `git add .`, `git commit -m "mensagem"`.

<p align="center">
  <a href="./Git_para_iniciantes.pdf">
    <img src="../assets/cards/git.png" alt="Git para iniciantes — preview do PDF" width="70%">
  </a>
  <br><br>
  <a href="./Git_para_iniciantes.pdf"><strong>Baixar Git_para_iniciantes.pdf</strong></a>
</p>

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

- Servir de referência rápida para quem está começando com Git
- Complementar o guia visual com texto pesquisável e comandos copiáveis
- Documentar erros comuns e um fluxo prático de trabalho

---

## Como usar

1. Baixe o **[PDF do guia](./Git_para_iniciantes.pdf)** para ter a visão geral do fluxo
2. Use as **tabelas** deste README para copiar comandos no terminal
3. Em caso de erro, vá direto para a seção [Erros comuns](#erros-comuns)
4. Pratique com o [Exercicio pratico](#exercicio-pratico) usando este repositório

---

## Guia em PDF (recomendado)

Material completo em alta qualidade, com texto selecionável e layout profissional:

**[Baixar Git_para_iniciantes.pdf](./Git_para_iniciantes.pdf)**

O PDF inclui: fluxo básico, stage, commits, branches, merge, push/pull, fluxo recomendado, conceitos, boas práticas e comandos de emergência.

---

## Guia visual (referencia rapida)

Use o PDF acima como material principal. As seções abaixo complementam com comandos copiáveis e exercício prático.

---

## Configuracao inicial

Antes do primeiro commit, configure seu nome e e-mail (faça uma vez por máquina):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

Para baixar um repositório pela primeira vez:

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

---

## 1. Stage (area de preparacao)

Área intermediária onde você escolhe o que vai entrar no próximo commit.

| Comando | Função |
|---------|--------|
| `git add arquivo.py` | Adiciona um arquivo específico ao stage |
| `git add .` | Adiciona todos os arquivos modificados ao stage |
| `git status` | Mostra o que foi modificado e o que está no stage |
| `git restore --staged arquivo.py` | Remove um arquivo do stage |

---

## 2. Commits (salvando alteracoes)

Cada commit é um "ponto de salvamento" no histórico do projeto.

| Comando | Função |
|---------|--------|
| `git commit -m "mensagem"` | Salva as alterações do stage com uma mensagem |
| `git log` | Mostra o histórico detalhado de commits |
| `git log --oneline` | Mostra o histórico de forma resumida |
| `git diff` | Mostra diferenças ainda não adicionadas ao stage |

---

## 3. Branches (linhas de trabalho)

Branches permitem trabalhar em funcionalidades em paralelo, sem misturar tudo na branch principal.

| Comando | Função |
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

Sincronizar seu repositório local com o remoto (GitHub).

| Comando | Função |
|---------|--------|
| `git push -u origin nome-da-branch` | Envia a branch para o GitHub (primeira vez) |
| `git push` | Envia os commits da branch atual para o GitHub |
| `git pull` | Baixa e aplica alterações do GitHub no projeto local |
| `git fetch` | Baixa alterações do remoto sem aplicar (só informação) |

**Dica:** sempre rode `git pull` antes de começar a trabalhar, para evitar conflitos.

---

## Clone vs pull vs fetch

| Comando | Quando usar | O que faz |
|---------|-------------|-----------|
| `git clone` | Primeira vez, repo ainda não existe na máquina | Copia o repositório inteiro |
| `git pull` | Repo já existe; você quer atualizar e aplicar | Baixa e mescla alterações do remoto |
| `git fetch` | Quer ver o que mudou antes de aplicar | Baixa sem mesclar |

---

## Fluxo de trabalho recomendado

1. Atualize a branch principal: `git checkout main && git pull`
2. Crie uma branch para a funcionalidade: `git checkout -b nome-da-funcionalidade`
3. Faça suas alterações nos arquivos
4. Verifique o status: `git status`
5. Adicione ao stage: `git add .`
6. Faça o commit: `git commit -m "mensagem clara"`
7. Envie a branch: `git push -u origin nome-da-funcionalidade`
8. Abra um Pull Request no GitHub
9. Após aprovação, faça merge na `main`
10. Apague a branch (local e remota) se não for mais necessária

---

## Pull Request

Pull Request (PR) não é um comando do Git. É um recurso do GitHub.

1. Você envia sua branch com `git push`
2. No GitHub, abre um PR pedindo para mesclar sua branch na `main`
3. Outra pessoa (ou você mesmo) revisa as alterações
4. Após aprovação, o merge é feito pela interface do GitHub

---

## Conceitos importantes

| Conceito | Significado |
|----------|-------------|
| **Repositorio** | Pasta do projeto com histórico de versões |
| **Commit** | Registro de uma alteração salva |
| **Branch** | Linha independente de desenvolvimento |
| **Merge** | Juntar alterações de uma branch em outra |
| **Stage** | Área onde você prepara o que vai commitar |
| **Push** | Enviar commits locais para o remoto |
| **Pull** | Baixar e aplicar commits do remoto |
| **Remoto (remote)** | Versão do projeto hospedada (ex.: GitHub) |

---

## Boas praticas

- Faça commits frequentes, com mensagens claras
- Use uma branch por funcionalidade ou correção
- Mantenha a branch `main` estável
- Rode `git pull` antes de começar a trabalhar
- Revise com `git status` antes de cada commit

---

## Comandos de emergencia

| Comando | Funcao |
|---------|--------|
| `git restore arquivo.py` | Descarta alterações não commitadas no arquivo |
| `git reset --soft HEAD~1` | Desfaz o último commit, mantendo alterações no stage |
| `git reset --hard HEAD~1` | Desfaz o último commit e apaga alterações (**perigoso**) |

**Atenção:** `git reset --hard` apaga alterações de forma permanente. Use apenas se tiver certeza.

---

## Erros comuns

| Erro | Causa provavel | O que fazer |
|------|----------------|-------------|
| `fatal: not a git repository` | Você não está dentro de uma pasta Git | Use `cd` até a pasta do projeto |
| `Please tell me who you are` | Git sem nome e e-mail configurados | Configure `user.name` e `user.email` |
| `rejected (fetch first)` | O remoto tem commits que você ainda não tem | Rode `git pull` antes do `git push` |
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

Pratique o fluxo Git usando este repositório:

1. Clone o repositório (se ainda não tiver):

```bash
git clone https://github.com/GustaFranz/exercicios_python.git
cd exercicios_python
```

2. Crie uma branch de teste:

```bash
git checkout -b teste-git-seu-nome
```

3. Faça uma alteração pequena (ex.: uma linha em qualquer README).

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

6. Abra um Pull Request no GitHub. Se for só treino, você pode fechar depois sem fazer merge.

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
