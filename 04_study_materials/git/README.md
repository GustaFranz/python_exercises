# Guia Git para iniciantes

**Link público para compartilhar:** https://github.com/GustaFranz/python_exercises/tree/main/04_study_materials/git

Material criado durante meus estudos de programação. Sou professor em transição para a área de TI e compartilho aqui o que aprendo no caminho — não como especialista, mas como alguém que ainda lembra das dificuldades iniciais.

**Se só lembrar de 3 comandos hoje:** `git status`, `git add .`, `git commit -m "mensagem"`.

<p align="center">
  <a href="https://raw.githubusercontent.com/GustaFranz/python_exercises/main/04_study_materials/git/Git_para_iniciantes.pdf" download="Git_para_iniciantes.pdf">
    <img src="../assets/cards/git.png" alt="Git para iniciantes — preview do PDF" width="70%">
  </a>
  <br><br>
  <a href="https://raw.githubusercontent.com/GustaFranz/python_exercises/main/04_study_materials/git/Git_para_iniciantes.pdf" download="Git_para_iniciantes.pdf"><strong>Baixar Git_para_iniciantes.pdf</strong></a>
</p>

---

## Índice

- [Objetivo](#objetivo)
- [Como usar](#como-usar)
- [Guia visual](#guia-visual)
- [Configuração inicial](#configuração-inicial)
- [Stage](#1-stage-área-de-preparação)
- [Commits](#2-commits-salvando-alterações)
- [Branches](#3-branches-linhas-de-trabalho)
- [Merge](#4-mesclando-merge)
- [Envio e atualização](#5-envio-e-atualização-github)
- [Clone vs pull vs fetch](#clone-vs-pull-vs-fetch)
- [Fluxo recomendado](#fluxo-de-trabalho-recomendado)
- [Pull Request](#pull-request)
- [Conceitos importantes](#conceitos-importantes)
- [Boas práticas](#boas-práticas)
- [Comandos de emergência](#comandos-de-emergência)
- [Criar repo no GitHub pelo terminal](#como-criar-e-publicar-um-repositório-no-github-pelo-terminal)
- [Erros comuns](#erros-comuns)
- [Exercício prático](#exercício-prático)
- [Resumo rápido](#resumo-rápido)

---

## Objetivo

- Servir de referência rápida para quem está começando com Git
- Complementar o guia visual com texto pesquisável e comandos copiáveis
- Documentar erros comuns e um fluxo prático de trabalho

---

## Como usar

1. Baixe o **[PDF do guia](https://raw.githubusercontent.com/GustaFranz/python_exercises/main/04_study_materials/git/Git_para_iniciantes.pdf)** para ter a visão geral do fluxo
2. Use as **tabelas** deste README para copiar comandos no terminal
3. Em caso de erro, vá direto para a seção [Erros comuns](#erros-comuns)
4. Pratique com o [Exercício prático](#exercício-prático) usando este repositório

---

## Guia em PDF (recomendado)

Material completo em alta qualidade, com texto selecionável e layout profissional:

**[Baixar Git_para_iniciantes.pdf](https://raw.githubusercontent.com/GustaFranz/python_exercises/main/04_study_materials/git/Git_para_iniciantes.pdf)**

O PDF inclui: fluxo básico, stage, commits, branches, merge, push/pull, fluxo recomendado, conceitos, criação de repositório no GitHub pelo terminal (gh), boas práticas e comandos de emergência.

Para regenerar o PDF (layout unificado com os demais guias):

```bash
python 04_study_materials/gerar_todos.py
python 04_study_materials/_gerar_previews.py
```

Conteúdo editável em `04_study_materials/gerador/conteudo/git.py`.

---

## Guia visual (referência rápida)

Use o PDF acima como material principal. As seções abaixo complementam com comandos copiáveis e exercício prático.

---

## Configuração inicial

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

## 1. Stage (área de preparação)

Área intermediária onde você escolhe o que vai entrar no próximo commit.

| Comando | Função |
|---------|--------|
| `git add arquivo.py` | Adiciona um arquivo específico ao stage |
| `git add .` | Adiciona todos os arquivos modificados ao stage |
| `git status` | Mostra o que foi modificado e o que está no stage |
| `git restore --staged arquivo.py` | Remove um arquivo do stage |

---

## 2. Commits (salvando alterações)

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

## 5. Envio e atualização (GitHub)

Sincronizar seu repositório local com o remoto (GitHub).

| Comando | Função |
|---------|--------|
| `git push -u origin NOME_DA_BRANCH` | Envia a branch para o GitHub (primeira vez) |
| `git push` | Envia os commits da branch atual para o GitHub |
| `git pull` | Baixa e aplica alterações do GitHub no projeto local |
| `git fetch` | Baixa alterações do remoto sem aplicar (só informação) |

**Importante:** em `git push -u origin NOME_DA_BRANCH`, o último termo é o **nome da branch** que receberá o push — não é um comando fixo. Antes de enviar, rode `git status`: a linha `On branch ...` mostra em qual branch você está. No **primeiro push** de um repositório novo, essa branch costuma ser **`main`** (não `feature`).

```bash
git status                    # confira: On branch main
git push -u origin main       # primeiro push (repo novo)
# git push -u origin feature-login  # só se você ESTIVER nessa branch
```

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
| **Repositório** | Pasta do projeto com histórico de versões |
| **Commit** | Registro de uma alteração salva |
| **Branch** | Linha independente de desenvolvimento |
| **Merge** | Juntar alterações de uma branch em outra |
| **Stage** | Área onde você prepara o que vai commitar |
| **Push** | Enviar commits locais para o remoto |
| **Pull** | Baixar e aplicar commits do remoto |
| **Remoto (remote)** | Versão do projeto hospedada (ex.: GitHub) |
| **Origin** | Apelido padrão da conexão com o remoto |
| **CLI** | Interface de linha de comando (digitar no terminal) |
| **gh (GitHub CLI)** | Programa para usar o GitHub pelo terminal |

---

## Boas práticas

- Faça commits frequentes, com mensagens claras
- Use uma branch por funcionalidade ou correção
- Mantenha a branch `main` estável
- Rode `git pull` antes de começar a trabalhar
- Revise com `git status` antes de cada commit

---

## Comandos de emergência

| Comando | Função |
|---------|--------|
| `git restore arquivo.py` | Descarta alterações não commitadas no arquivo |
| `git reset --soft HEAD~1` | Desfaz o último commit, mantendo alterações no stage |
| `git reset --hard HEAD~1` | Desfaz o último commit e apaga alterações (**perigoso**) |

**Atenção:** `git reset --hard` apaga alterações de forma permanente. Use apenas se tiver certeza.

---

## Como Criar e Publicar um Repositório no GitHub pelo Terminal

### Git e GitHub na Prática: Criação de Repositório e Primeiro Push

Até aqui você viu comandos do **Git** (controle de versão na sua máquina). Agora vamos publicar o projeto no **GitHub** (site que hospeda repositórios na nuvem) usando o **terminal**, sem abrir o navegador para criar o repositório.

Para isso usamos o **GitHub CLI** — programa chamado **`gh`** que conversa com o GitHub por comandos. **CLI** significa *Command Line Interface*: interface de linha de comando, ou seja, digitar comandos em vez de clicar em botões.

### 1. Verificar a instalação do GitHub CLI

O **`gh`** é um programa separado do Git. Instale em [cli.github.com](https://cli.github.com) e confira:

```bash
gh --version
```

Se aparecer a versão, está instalado. Se der `command not found`, instale antes de continuar.

### 2. Verificar a autenticação no GitHub

Autenticação é provar ao GitHub quem você é (login). Sem isso, o `gh` não cria repositórios em seu nome.

```bash
gh auth status
```

Se não estiver logado:

```bash
gh auth login
```

Siga as perguntas (GitHub.com, HTTPS, login pelo navegador). Depois repita `gh auth status`.

### 3. Inicializar o repositório Git local

**Repositório local** = pasta do projeto com histórico Git só no computador.

```bash
cd caminho/do/meu-projeto
git init
```

Configure nome e e-mail (uma vez por máquina):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### 4. Criar o repositório remoto pelo terminal

**Repositório remoto** = cópia do projeto na nuvem (GitHub).

```bash
gh repo create meu-projeto --public --source=. --remote=origin
```

- **meu-projeto** — nome no GitHub (pode ser outro)
- **--public** — visível para todos (use `--private` se quiser fechado)
- **--source=.** — usa a pasta atual
- **--remote=origin** — cadastra o GitHub com o apelido **origin**

**O que é origin?** Nome padrão da conexão com o remoto. Em vez de digitar a URL completa, você usa `git push origin ...`.

### 5. Verificar a conexão com o repositório remoto

```bash
git remote -v
git status    # On branch main (ou master)
git branch    # * marca a branch atual
```

### 6. Adicionar arquivos ao stage

O **stage** é a área de preparação — o que entrará no commit.

```bash
git status
git add .
git status    # arquivos em verde = prontos
```

Crie um `.gitignore` para não enviar `.venv`, senhas etc.

### 7. Criar o primeiro commit

```bash
git commit -m "primeiro commit: estrutura inicial do projeto"
```

### 8. Realizar o primeiro push

**Push** envia commits locais para o GitHub. No primeiro envio, `-u` vincula a branch local à remota. O nome depois de `origin` deve ser o da branch atual — confira com `git status`. Em repos novos, quase sempre é **`main`**:

```bash
git status
git push -u origin main
```

Se estiver em outra branch (ex.: `feature-login`):

```bash
git push -u origin feature-login
```

### 9. Erros comuns e como corrigir

| Erro / situação | Causa provável | Como corrigir |
|-----------------|----------------|---------------|
| `gh: command not found` | GitHub CLI não instalado | Instale em cli.github.com |
| `not logged in` | Conta não autenticada | `gh auth login` |
| `fatal: not a git repository` | Pasta sem `git init` | `cd` na pasta certa e `git init` |
| `Please tell me who you are` | Nome/e-mail não configurados | `git config --global user.name` e `user.email` |
| `src refspec main does not match` | Branch `main` não existe | `git branch` — use o nome real |
| `failed to push some refs` | Remoto mais atualizado | `git pull --rebase origin main`, depois `git push` |
| `repository already exists` | Nome já usado no GitHub | Outro nome ou `gh repo create ... --push` |
| `nothing to commit` | Nada no stage | `git add .` antes do commit |

**Resumo do zero ao GitHub:**

```bash
cd meu-projeto
git init
gh auth login          # se necessário
gh repo create meu-projeto --public --source=. --remote=origin
git add .
git commit -m "primeiro commit"
git status             # confira a branch (geralmente main)
git push -u origin main
```

---

## Erros comuns

| Erro | Causa provável | O que fazer |
|------|----------------|-------------|
| `fatal: not a git repository` | Você não está dentro de uma pasta Git | Use `cd` até a pasta do projeto |
| `Please tell me who you are` | Git sem nome e e-mail configurados | Configure `user.name` e `user.email` |
| `rejected (fetch first)` | O remoto tem commits que você ainda não tem | Rode `git pull` antes do `git push` |
| `merge conflict` | Mesmo arquivo editado em lugares diferentes | Resolva manualmente, depois `git add` e `git commit` |
| `error: failed to push some refs` | Branch remota mais atualizada | `git pull --rebase` ou `git pull`, resolva conflitos, tente de novo |

### Exemplo de conflito de merge

```
<<<<<<< HEAD
seu código
=======
código do remoto
>>>>>>> branch-remota
```

Escolha o que manter (ou combine), remova os marcadores (`<<<<`, `====`, `>>>>`), depois:

```bash
git add arquivo.py
git commit -m "resolve conflito de merge"
```

---

## Exercício prático

Pratique o fluxo Git usando este repositório:

1. Clone o repositório (se ainda não tiver):

```bash
git clone https://github.com/GustaFranz/python_exercises.git
cd python_exercises
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

## Resumo rápido

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
