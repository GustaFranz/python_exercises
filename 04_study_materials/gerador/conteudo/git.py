# -*- coding: utf-8 -*-
"""Conteúdo: Git - guia completo para iniciantes."""

from ..tema import TEMA_GIT

SPEC = {
    "tema": TEMA_GIT,
    "topico": "GIT",
    "destaque": "GUIA PARA INICIANTES",
    "subtitulo": "Commits, branches e fluxo de trabalho — passo a passo, com exemplos",
    "simbolo": ">_",
    "blocos": [
        {"tipo": "secao", "titulo": "O que é Git?"},
        {"tipo": "paragrafo",
         "texto": "Git é um <b>sistema de controle de versão</b>. Ele registra o "
                  "histórico do seu projeto, permite trabalhar em equipe, "
                  "experimentar sem medo e voltar atrás quando necessário."},
        {"tipo": "checks", "itens": [
            "Salva o histórico do projeto (commits).",
            "Permite trabalhar em várias linhas (branches).",
            "Facilita colaboração e revisão de código.",
            "Protege contra perda de código.",
            "Dá liberdade para testar sem medo de errar.",
        ]},

        {"tipo": "secao", "titulo": "O fluxo básico do Git"},
        {"tipo": "paragrafo",
         "texto": "<b>Arquivo alterado</b>  ->  (git add)  ->  <b>Stage</b>  ->  "
                  "(git commit)  ->  <b>Repositório local</b>  ->  (git push)  ->  "
                  "<b>GitHub (remoto)</b>."},
        {"tipo": "checks", "itens": [
            "Você altera arquivos no projeto.",
            "<b>git add</b> coloca no stage (você escolhe o que será salvo).",
            "<b>git commit</b> salva no histórico.",
            "<b>git push</b> envia para o GitHub.",
        ]},

        {"tipo": "secao", "titulo": "1. Stage (área de preparação)"},
        {"tipo": "paragrafo",
         "texto": "O stage é uma área intermediária entre suas alterações e o "
                  "commit. Você escolhe exatamente o que entra no próximo commit."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.30, 0.42, 0.28], "mono": [0, 2],
         "linhas": [
            ["git add arquivo.py", "Coloca um arquivo específico no stage.", "git add app.py"],
            ["git add .", "Coloca todos os arquivos no stage.", "git add ."],
            ["git status", "Mostra o que mudou e o que está no stage.", "git status"],
            ["git restore --staged x", "Tira do stage sem apagar as alterações.", "git restore --staged app.py"],
         ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Sempre use git status antes de commitar. Ele mostra exatamente "
                  "o que está pronto para ser salvo."},

        {"tipo": "secao", "titulo": "2. Commits (salvando alterações)"},
        {"tipo": "paragrafo",
         "texto": "O commit é um 'ponto de salvamento' no histórico. Cada commit "
                  "deve ter uma mensagem clara sobre o que foi feito."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.26, 0.40, 0.34], "mono": [0, 2],
         "linhas": [
            ["git commit -m \"msg\"", "Salva as mudanças do stage no histórico.", "git commit -m \"cria login\""],
            ["git log", "Mostra o histórico de commits.", "git log"],
            ["git log --oneline", "Mostra o histórico resumido (1 linha).", "git log --oneline"],
            ["git diff", "Mostra o que foi alterado e ainda não adicionado.", "git diff"],
         ]},
        {"tipo": "codigo", "titulo": "Exemplo de histórico (git log --oneline)", "linhas": [
            ("1ab32cd  cria sistema de login", None),
            ("f4d9ab6  corrige botão de acesso", None),
            ("98f736e  ajusta layout da tela inicial", None),
        ]},

        {"tipo": "secao", "titulo": "3. Branches (linhas de trabalho)"},
        {"tipo": "paragrafo",
         "texto": "Branch é uma linha paralela de desenvolvimento. Permite criar "
                  "funcionalidades sem mexer na branch principal (geralmente main)."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.28, 0.40, 0.32], "mono": [0, 2],
         "linhas": [
            ["git branch", "Lista todas as branches.", "git branch"],
            ["git branch nome", "Cria uma nova branch.", "git branch tela-login"],
            ["git checkout nome", "Muda para outra branch.", "git checkout tela-login"],
            ["git checkout -b nome", "Cria e já muda para a nova branch.", "git checkout -b pagamento"],
            ["git switch nome", "Muda de branch (alternativa ao checkout).", "git switch main"],
            ["git switch -c nome", "Cria e já muda (alternativa).", "git switch -c nova-feature"],
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
            ["git push", "Envia as mudanças para o GitHub.", "git push"],
         ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Sempre teste a branch antes do merge. Depois, você pode excluir "
                  "a branch que não precisa mais."},

        {"tipo": "secao", "titulo": "5. Envio e atualização (GitHub)"},
        {"tipo": "paragrafo",
         "texto": "No comando <b>git push -u origin NOME_DA_BRANCH</b>, o último termo "
                  "(<i>feature</i>, <i>main</i>, etc.) é o <b>nome da branch</b> que "
                  "vai receber o push — não é um comando fixo. Antes de enviar, rode "
                  "<b>git status</b>: a linha <i>On branch ...</i> mostra em qual branch "
                  "você está. No <b>primeiro push</b> de um repo novo, essa branch "
                  "costuma ser <b>main</b> (não feature)."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.30, 0.40, 0.30], "mono": [0, 2],
         "linhas": [
            ["git push -u origin NOME", "Envia a branch pela 1ª vez e vincula ao remoto.", "git push -u origin main"],
            ["git push -u origin NOME", "Mesmo comando em branch de funcionalidade.", "git push -u origin feature-login"],
            ["git push", "Envia as mudanças da branch atual (já vinculada).", "git push"],
            ["git pull", "Baixa e aplica as alterações do GitHub.", "git pull"],
            ["git fetch", "Baixa as alterações sem aplicar (só informa).", "git fetch"],
         ]},
        {"tipo": "codigo", "titulo": "Conferir a branch antes do primeiro push", "linhas": [
            ("git status", "# On branch main  <- use este nome no push"),
            ("git push -u origin main", "# primeiro push (repo novo)"),
            ("# git push -u origin feature-login  # só se você ESTIVER nessa branch", None),
        ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Sempre dê git pull antes de começar a trabalhar, para evitar conflitos. "
                  "E use git status antes do push para não enviar para a branch errada."},

        {"tipo": "secao", "titulo": "6. Fluxo de trabalho recomendado"},
        {"tipo": "paragrafo",
         "texto": "Siga esta ordem sempre que for criar uma nova funcionalidade:"},
        {"tipo": "codigo", "titulo": "Ordem dos comandos", "linhas": [
            ("git pull", "# atualiza a branch principal"),
            ("git checkout -b nova-funcionalidade", "# cria e entra na branch"),
            ("# ... faça suas alterações no código ...", None),
            ("git add .", "# coloca tudo no stage"),
            ("git commit -m \"mensagem clara\"", "# salva no histórico"),
            ("git push -u origin nova-funcionalidade", "# envia para o GitHub"),
            ("# abra um Pull Request, faça o merge na main e exclua a branch", None),
        ]},

        {"tipo": "secao", "titulo": "Conceitos importantes"},
        {"tipo": "tabela",
         "cabecalho": ["Termo", "Significado"],
         "larguras": [0.22, 0.78], "mono": [0],
         "linhas": [
            ["Repositório", "Projeto onde o código é gerenciado."],
            ["Commit", "Salvamento de um ponto da alteração."],
            ["Branch", "Linha paralela de desenvolvimento."],
            ["Merge", "Junção de uma branch em outra."],
            ["Stage", "Área de preparação do commit (git add)."],
            ["Push", "Enviar alterações para o GitHub."],
            ["Pull", "Baixar alterações do GitHub."],
            ["Remote / Remoto", "Repositório na nuvem (ex.: GitHub)."],
            ["Origin", "Apelido padrão da conexão com o remoto."],
            ["CLI", "Interface de linha de comando (digitar no terminal)."],
            ["gh (GitHub CLI)", "Programa para usar o GitHub pelo terminal."],
         ]},

        {"tipo": "secao", "titulo": "Comandos de emergência (use com cuidado)"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "O que faz", "Exemplo"],
         "larguras": [0.30, 0.44, 0.26], "mono": [0, 2],
         "linhas": [
            ["git restore arquivo", "Descarta alterações (volta ao último commit).", "git restore app.py"],
            ["git reset --soft HEAD~1", "Desfaz o último commit, mantendo as alterações.", "git reset --soft HEAD~1"],
            ["git reset --hard HEAD~1", "Desfaz o commit e APAGA as alterações (perigoso).", "git reset --hard HEAD~1"],
         ]},

        {"tipo": "secao", "titulo": "Como Criar e Publicar um Repositório no GitHub pelo Terminal"},
        {"tipo": "paragrafo",
         "texto": "<b>Git e GitHub na Prática: Criação de Repositório e Primeiro Push</b><br/><br/>"
                  "Até aqui você viu comandos do <b>Git</b> (controle de versão na sua máquina). "
                  "Agora vamos publicar o projeto no <b>GitHub</b> (site que hospeda repositórios "
                  "na nuvem) usando o <b>terminal</b>, sem abrir o navegador para criar o repo.<br/><br/>"
                  "Para isso usamos o <b>GitHub CLI</b> — programa chamado <b>gh</b> que conversa "
                  "com o GitHub por comandos. <b>CLI</b> significa <i>Command Line Interface</i>: "
                  "interface de linha de comando, ou seja, digitar comandos em vez de clicar em botões."},

        {"tipo": "secao", "titulo": "1. Verificar a instalação do GitHub CLI"},
        {"tipo": "paragrafo",
         "texto": "O <b>gh</b> é um programa separado do Git. Você precisa instalá-lo uma vez "
                  "(site: cli.github.com). Depois, confira se está disponível:"},
        {"tipo": "codigo", "linhas": [
            ("gh --version", None),
        ]},
        {"tipo": "paragrafo",
         "texto": "Se aparecer a versão (ex.: <i>gh version 2.x</i>), está instalado. "
                  "Se der erro <i>command not found</i>, instale o GitHub CLI antes de continuar."},

        {"tipo": "secao", "titulo": "2. Verificar a autenticação no GitHub"},
        {"tipo": "paragrafo",
         "texto": "Autenticação é o processo de provar ao GitHub quem você é (login). "
                  "Sem isso, o <b>gh</b> não consegue criar repositórios em seu nome."},
        {"tipo": "codigo", "linhas": [
            ("gh auth status", None),
        ]},
        {"tipo": "paragrafo",
         "texto": "Se não estiver logado, rode <b>gh auth login</b> e siga as perguntas "
                  "(GitHub.com, HTTPS, login pelo navegador). Ao final, repita "
                  "<b>gh auth status</b> — deve mostrar sua conta conectada."},

        {"tipo": "secao", "titulo": "3. Inicializar o repositório Git local"},
        {"tipo": "paragrafo",
         "texto": "<b>Repositório local</b> é a pasta do seu projeto com histórico Git "
                  "apenas no computador. Entre na pasta do projeto e inicie o Git:"},
        {"tipo": "codigo", "linhas": [
            ("cd caminho/do/meu-projeto", None),
            ("git init", "# cria a pasta oculta .git (histórico local)"),
        ]},
        {"tipo": "paragrafo",
         "texto": "Na primeira vez na máquina, configure nome e e-mail (Git usa isso nos commits):"},
        {"tipo": "codigo", "linhas": [
            ('git config --global user.name "Seu Nome"', None),
            ('git config --global user.email "seu@email.com"', None),
        ]},

        {"tipo": "secao", "titulo": "4. Criar o repositório remoto pelo terminal"},
        {"tipo": "paragrafo",
         "texto": "<b>Repositório remoto</b> é a cópia do projeto na nuvem (GitHub). "
                  "Com o <b>gh</b>, você cria o repo no site sem sair do terminal:"},
        {"tipo": "codigo", "linhas": [
            ("gh repo create meu-projeto --public --source=. --remote=origin", None),
        ]},
        {"tipo": "checks", "itens": [
            "<b>meu-projeto</b> — nome do repositório no GitHub (pode ser outro).",
            "<b>--public</b> — repo visível para todos (use --private se quiser fechado).",
            "<b>--source=.</b> — usa a pasta atual como origem.",
            "<b>--remote=origin</b> — cadastra o GitHub com o apelido <b>origin</b>.",
        ]},
        {"tipo": "callout", "titulo": "O que é origin?",
         "texto": "<b>origin</b> é o nome padrão da conexão com o repositório remoto. "
                  "Pense nele como um 'apelido' para a URL do GitHub. Depois você usa "
                  "<i>git push origin ...</i> em vez de digitar a URL completa toda vez."},

        {"tipo": "secao", "titulo": "5. Verificar a conexão com o repositório remoto"},
        {"tipo": "paragrafo",
         "texto": "Confirme se o Git 'enxerga' o GitHub corretamente:"},
        {"tipo": "codigo", "linhas": [
            ("git remote -v", None),
        ]},
        {"tipo": "paragrafo",
         "texto": "A saída deve listar <b>origin</b> com URL do tipo "
                  "<i>https://github.com/seu-usuario/meu-projeto.git</i> (fetch e push). "
                  "Também confira a branch atual:"},
        {"tipo": "codigo", "linhas": [
            ("git status", "# On branch main  (ou master em repos antigos)"),
            ("git branch", "# lista branches locais; * marca a atual"),
        ]},

        {"tipo": "secao", "titulo": "6. Adicionar arquivos ao stage"},
        {"tipo": "paragrafo",
         "texto": "Lembre: o <b>stage</b> é a área de preparação — você escolhe o que "
                  "entrará no próximo commit. Para o primeiro envio, costuma-se adicionar tudo:"},
        {"tipo": "codigo", "linhas": [
            ("git status", "# vê arquivos novos ou alterados (vermelho = fora do stage)"),
            ("git add .", "# coloca todos os arquivos da pasta no stage"),
            ("git status", "# verde = prontos para commit"),
        ]},
        {"tipo": "callout", "titulo": "Dica",
         "texto": "Crie um arquivo .gitignore para não enviar pastas como .venv ou "
                  "senhas acidentalmente. O Git só commita o que você adicionou com git add."},

        {"tipo": "secao", "titulo": "7. Criar o primeiro commit"},
        {"tipo": "paragrafo",
         "texto": "O <b>commit</b> grava um 'checkpoint' no histórico local. "
                  "Use uma mensagem curta e clara sobre o que este primeiro salvamento representa:"},
        {"tipo": "codigo", "linhas": [
            ('git commit -m "primeiro commit: estrutura inicial do projeto"', None),
        ]},
        {"tipo": "paragrafo",
         "texto": "Se aparecer erro pedindo identidade, volte ao passo 3 e configure "
                  "user.name e user.email."},

        {"tipo": "secao", "titulo": "8. Realizar o primeiro push"},
        {"tipo": "paragrafo",
         "texto": "<b>Push</b> envia seus commits locais para o repositório remoto (GitHub). "
                  "No primeiro envio, use <b>-u</b> (upstream) para vincular sua branch local "
                  "à branch remota. O nome depois de <b>origin</b> deve ser o da sua branch atual — "
                  "confira com <b>git status</b>. Em repos novos, quase sempre é <b>main</b>:"},
        {"tipo": "codigo", "titulo": "Sequência completa (repo novo, branch main)", "linhas": [
            ("git status", "# confirme: On branch main"),
            ("git push -u origin main", None),
        ]},
        {"tipo": "paragrafo",
         "texto": "Depois do primeiro push com <b>-u</b>, basta <b>git push</b> na mesma branch. "
                  "Se você estiver em outra branch (ex.: <i>feature-login</i>), o comando seria "
                  "<b>git push -u origin feature-login</b> — sempre o nome que aparece no git status."},

        {"tipo": "secao", "titulo": "9. Erros comuns e como corrigir"},
        {"tipo": "tabela",
         "cabecalho": ["Erro / situação", "Causa provável", "Como corrigir"],
         "larguras": [0.28, 0.34, 0.38], "mono": [],
         "linhas": [
            ["gh: command not found", "GitHub CLI não instalado.", "Instale em cli.github.com e teste gh --version."],
            ["not logged in", "Conta GitHub não autenticada.", "Rode gh auth login e depois gh auth status."],
            ["fatal: not a git repository", "Pasta sem git init.", "Entre na pasta certa e rode git init."],
            ["Please tell me who you are", "Nome/e-mail não configurados.", "git config --global user.name e user.email."],
            ["src refspec main does not match", "Branch main não existe localmente.", "git branch — use o nome real (main ou master)."],
            ["failed to push some refs", "Remoto tem commits que você não tem.", "git pull --rebase origin main, depois git push."],
            ["repository already exists", "Repo com mesmo nome no GitHub.", "Escolha outro nome ou use gh repo create ... --push."],
            ["nothing to commit", "Nenhum arquivo no stage.", "git add . e git status antes do commit."],
         ]},

        {"tipo": "codigo", "titulo": "Resumo: do zero ao GitHub (copie e adapte)", "linhas": [
            ("cd meu-projeto", None),
            ("git init", None),
            ("gh auth login", "# se ainda não estiver logado"),
            ("gh repo create meu-projeto --public --source=. --remote=origin", None),
            ("git add .", None),
            ('git commit -m "primeiro commit"', None),
            ("git status", "# veja o nome da branch (geralmente main)"),
            ("git push -u origin main", None),
        ]},

        {"tipo": "callout", "titulo": "Resumo rápido + boas práticas",
         "cor": "#F05133",
         "texto": [
            "Comandos do dia a dia: status, add ., commit -m, push, pull.",
            "Faça commits pequenos e com mensagens claras e objetivas.",
            "Use uma branch para cada funcionalidade ou correção.",
            "Sempre teste antes do merge e mantenha a main estável.",
            "Pratique e erre sem medo: com o tempo, vira natural.",
         ]},
    ],
}
