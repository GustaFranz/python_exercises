# -*- coding: utf-8 -*-
"""Conteudo: Git - guia completo para iniciantes."""

from ..tema import TEMA_GIT

SPEC = {
    "tema": TEMA_GIT,
    "topico": "GIT",
    "destaque": "GUIA PARA INICIANTES",
    "subtitulo": "Commits, branches e fluxo de trabalho — passo a passo, com exemplos",
    "simbolo": ">_",
    "blocos": [
        {"tipo": "secao", "titulo": "O que e Git?"},
        {"tipo": "paragrafo",
         "texto": "Git e um <b>sistema de controle de versao</b>. Ele registra o "
                  "historico do seu projeto, permite trabalhar em equipe, "
                  "experimentar sem medo e voltar atras quando necessario."},
        {"tipo": "checks", "itens": [
            "Salva o historico do projeto (commits).",
            "Permite trabalhar em varias linhas (branches).",
            "Facilita colaboracao e revisao de codigo.",
            "Protege contra perda de codigo.",
            "Da liberdade para testar sem medo de errar.",
        ]},

        {"tipo": "secao", "titulo": "O fluxo basico do Git"},
        {"tipo": "paragrafo",
         "texto": "<b>Arquivo alterado</b>  ->  (git add)  ->  <b>Stage</b>  ->  "
                  "(git commit)  ->  <b>Repositorio local</b>  ->  (git push)  ->  "
                  "<b>GitHub (remoto)</b>."},
        {"tipo": "checks", "itens": [
            "Voce altera arquivos no projeto.",
            "<b>git add</b> coloca no stage (voce escolhe o que sera salvo).",
            "<b>git commit</b> salva no historico.",
            "<b>git push</b> envia para o GitHub.",
        ]},

        {"tipo": "secao", "titulo": "1. Stage (area de preparacao)"},
        {"tipo": "paragrafo",
         "texto": "O stage e uma area intermediaria entre suas alteracoes e o "
                  "commit. Voce escolhe exatamente o que entra no proximo commit."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.30, 0.42, 0.28], "mono": [0, 2],
         "linhas": [
            ["git add arquivo.py", "Coloca um arquivo especifico no stage.", "git add app.py"],
            ["git add .", "Coloca todos os arquivos no stage.", "git add ."],
            ["git status", "Mostra o que mudou e o que esta no stage.", "git status"],
            ["git restore --staged x", "Tira do stage sem apagar as alteracoes.", "git restore --staged app.py"],
         ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Sempre use git status antes de commitar. Ele mostra exatamente "
                  "o que esta pronto para ser salvo."},

        {"tipo": "secao", "titulo": "2. Commits (salvando alteracoes)"},
        {"tipo": "paragrafo",
         "texto": "O commit e um 'ponto de salvamento' no historico. Cada commit "
                  "deve ter uma mensagem clara sobre o que foi feito."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.26, 0.40, 0.34], "mono": [0, 2],
         "linhas": [
            ["git commit -m \"msg\"", "Salva as mudancas do stage no historico.", "git commit -m \"cria login\""],
            ["git log", "Mostra o historico de commits.", "git log"],
            ["git log --oneline", "Mostra o historico resumido (1 linha).", "git log --oneline"],
            ["git diff", "Mostra o que foi alterado e ainda nao adicionado.", "git diff"],
         ]},
        {"tipo": "codigo", "titulo": "Exemplo de historico (git log --oneline)", "linhas": [
            ("1ab32cd  cria sistema de login", None),
            ("f4d9ab6  corrige botao de acesso", None),
            ("98f736e  ajusta layout da tela inicial", None),
        ]},

        {"tipo": "secao", "titulo": "3. Branches (linhas de trabalho)"},
        {"tipo": "paragrafo",
         "texto": "Branch e uma linha paralela de desenvolvimento. Permite criar "
                  "funcionalidades sem mexer na branch principal (geralmente main)."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.28, 0.40, 0.32], "mono": [0, 2],
         "linhas": [
            ["git branch", "Lista todas as branches.", "git branch"],
            ["git branch nome", "Cria uma nova branch.", "git branch tela-login"],
            ["git checkout nome", "Muda para outra branch.", "git checkout tela-login"],
            ["git checkout -b nome", "Cria e ja muda para a nova branch.", "git checkout -b pagamento"],
            ["git switch nome", "Muda de branch (alternativa ao checkout).", "git switch main"],
            ["git switch -c nome", "Cria e ja muda (alternativa).", "git switch -c nova-feature"],
         ]},

        {"tipo": "secao", "titulo": "4. Mesclando (merge)"},
        {"tipo": "paragrafo",
         "texto": "Quando a funcionalidade da branch estiver pronta, juntamos "
                  "(merge) na branch principal."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.28, 0.40, 0.32], "mono": [0, 2],
         "linhas": [
            ["git checkout main", "Vai para a branch principal.", "git checkout main"],
            ["git merge nome", "Mescla a branch informada na atual.", "git merge tela-login"],
            ["git push", "Envia as mudancas para o GitHub.", "git push"],
         ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Sempre teste a branch antes do merge. Depois, voce pode excluir "
                  "a branch que nao precisa mais."},

        {"tipo": "secao", "titulo": "5. Envio e atualizacao (GitHub)"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.30, 0.40, 0.30], "mono": [0, 2],
         "linhas": [
            ["git push -u origin nome", "Envia a branch pela primeira vez.", "git push -u origin feature"],
            ["git push", "Envia as mudancas da branch atual.", "git push"],
            ["git pull", "Baixa e aplica as alteracoes do GitHub.", "git pull"],
            ["git fetch", "Baixa as alteracoes sem aplicar (so informa).", "git fetch"],
         ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Sempre de git pull antes de comecar a trabalhar, para evitar conflitos."},

        {"tipo": "secao", "titulo": "6. Fluxo de trabalho recomendado"},
        {"tipo": "paragrafo",
         "texto": "Siga esta ordem sempre que for criar uma nova funcionalidade:"},
        {"tipo": "codigo", "titulo": "Ordem dos comandos", "linhas": [
            ("git pull", "# atualiza a branch principal"),
            ("git checkout -b nova-funcionalidade", "# cria e entra na branch"),
            ("# ... faca suas alteracoes no codigo ...", None),
            ("git add .", "# coloca tudo no stage"),
            ("git commit -m \"mensagem clara\"", "# salva no historico"),
            ("git push -u origin nova-funcionalidade", "# envia para o GitHub"),
            ("# abra um Pull Request, faca o merge na main e exclua a branch", None),
        ]},

        {"tipo": "secao", "titulo": "Conceitos importantes"},
        {"tipo": "tabela",
         "cabecalho": ["Termo", "Significado"],
         "larguras": [0.22, 0.78], "mono": [0],
         "linhas": [
            ["Repositorio", "Projeto onde o codigo e gerenciado."],
            ["Commit", "Salvamento de um ponto da alteracao."],
            ["Branch", "Linha paralela de desenvolvimento."],
            ["Merge", "Juncao de uma branch em outra."],
            ["Stage", "Area de preparacao do commit."],
            ["Push", "Enviar alteracoes para o GitHub."],
            ["Pull", "Baixar alteracoes do GitHub."],
            ["Remote", "Repositorio na nuvem (ex.: GitHub)."],
         ]},

        {"tipo": "secao", "titulo": "Comandos de emergencia (use com cuidado)"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.30, 0.44, 0.26], "mono": [0, 2],
         "linhas": [
            ["git restore arquivo", "Descarta alteracoes (volta ao ultimo commit).", "git restore app.py"],
            ["git reset --soft HEAD~1", "Desfaz o ultimo commit, mantendo as alteracoes.", "git reset --soft HEAD~1"],
            ["git reset --hard HEAD~1", "Desfaz o commit e APAGA as alteracoes (perigoso).", "git reset --hard HEAD~1"],
         ]},

        {"tipo": "callout", "titulo": "Resumo rapido + boas praticas",
         "cor": "#F05133",
         "texto": [
            "Comandos do dia a dia: status, add ., commit -m, push, pull.",
            "Faca commits pequenos e com mensagens claras e objetivas.",
            "Use uma branch para cada funcionalidade ou correcao.",
            "Sempre teste antes do merge e mantenha a main estavel.",
            "Pratique e erre sem medo: com o tempo, vira natural.",
         ]},
    ],
}
