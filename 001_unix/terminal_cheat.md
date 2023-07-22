# Lista de comandos importantes para uso no terminal Ubuntu :scroll:

O sistema operacional Ubuntu conta com uma série de funcionalidades embutidas. Abaixo estão alguns comandos úteis para o terminal Ubuntu em ordem alfabética:

## A

[apt-get](https://manpages.ubuntu.com/manpages/xenial/man8/apt-get.8.html)
: Controle de pacotes do sistema

    apt-get install [pacote]; [update]; [upgrade]

## B

## C

[cat](https://manpages.ubuntu.com/manpages/jammy/en/man1/cat.1.html)
: Imprime o conteúdo de um arquivo de texto

    cat [arquivo]

[cd](https://manpages.ubuntu.com/manpages/jammy/en/man1/cd.1posix.html)
: _change directory_ muda de diretório

    cd [caminho_novo_diretório]

[chmod](https://manpages.ubuntu.com/manpages/jammy/en/man1/chmod.1posix.html)
: _CHange MODe_ Altera as permissões de um arquivo ou diretório

    chmod [RWX] [arquivo]

[cp](https://manpages.ubuntu.com/manpages/jammy/en/man1/cp.1.html)
: _copy_ Copia o arquivo

    cp [arquivo] [destino]

## D

## E

## F

[find](https://manpages.ubuntu.com/manpages/jammy/en/man1/find.1.html)
:Localizar arquivo

    find [diretório] -name [arquivo]

## G

[grep](https://manpages.ubuntu.com/manpages/jammy/en/man1/grep.1plan9.html)
:_Globaly search for Regular Expression and Print out_ Procura por um padrão em um arquivo.

    grep -i [case insensitive] -r [recursivo]

[gunzip](https://manpages.ubuntu.com/manpages/jammy/en/man1/gunzip.1.html)
: Descompacta arquivo de formato .gz

    gunzip [arquivo.gz]

[gzip](https://manpages.ubuntu.com/manpages/jammy/en/man1/gzip.1.html)| Compacta arquivo no formato .gz

    gzip [arquivo.gz] [pasta/arquivo]

## H

[head](https://manpages.ubuntu.com/manpages/jammy/en/man1/head.1posix.html)
: Imprime as 10 primeiras linhas de um arquivo.

    head -[numero de linhas] [arquivo]

[history](https://manpages.ubuntu.com/manpages/jammy/en/man3/history.3readline.html)
: Imprime o histórico de comandos executados no terminal

    history

## I

## J

## K

## L

[ls](https://manpages.ubuntu.com/manpages/jammy/en/man1/ls.1plan9.html)
: _list_ Lista todos os itens do diretório atual.

    ls -d [lista diretórios]

## M

[man](https://manpages.ubuntu.com/manpages/jammy/en/man1/man.1posix.html)
: _MANual_ Imprime o manual da ferramenta

    man [ferramenta]

[mkdir](https://manpages.ubuntu.com/manpages/jammy/en/man1/mkdir.1.html)
: _make directory_

    mkdir [nome_do_diretório]

[mv](https://manpages.ubuntu.com/manpages/jammy/en/man1/mv.1posix.html)
: _move_ Move arquivos.

    mv [caminho_do_arquivo] [destino_do_arquivo]

## N

## O

## P

[pwd](https://manpages.ubuntu.com/manpages/jammy/en/man1/pwd.1posix.html)
: _pathway directory_ Imprime o caminho do diretório

    pwd [diretório/arquivo]

## Q

## R

[rm](https://manpages.ubuntu.com/manpages/jammy/en/man1/rm.1posix.html)
: _remove_ Remove arquivos.

    rm -r [recursivo] -f [force] [arquivo]

## S

[sort](https://manpages.ubuntu.com/manpages/jammy/en/man1/sort.1posix.html)
: Organiza em ordem alfabética

    cat arquivo | sort

[ssh](https://manpages.ubuntu.com/manpages/jammy/en/man1/ssh.1.html)
: _Secure SHell_ Conectar computadores de forma remota

    ssh -p [porta] [usuário]@[IP ADDRESS]

[sudo](https://manpages.ubuntu.com/manpages/jammy/en/man8/sudo.8.html)
: _superuser do_ Ativa funções de superusuário _adm do windows_.

    sudo [command]

## T

[tail](https://manpages.ubuntu.com/manpages/jammy/en/man1/tail.1.html)
: Imprime as 10 últimas linhas de um arquivo.

    tail -[numero de linhas] [arquivo]**

[tar](https://manpages.ubuntu.com/manpages/jammy/en/man1/tar.1.html)
: _Tape ARchiver_ Compacta -czvf [**C**reate g**Z V**erbose **F**ile] ou descompacta -xzvf [e**X**tract g**Z V**erbose **F**ile] os arquivos no formato .tar.gz

    tar -czvf [arquivo.tar.gz] [diretório/arquivo]
    tar -xzvf [aquivo.tar.gz]

[top](https://manpages.ubuntu.com/manpages/jammy/en/man1/top.1.html)
: Imprime a lista de processos em execução

    top

[touch](https://manpages.ubuntu.com/manpages/jammy/en/man1/touch.1posix.html)
: Cria um arquivo.

    touch [nome_do_arquivo]

## U

[unzip](https://manpages.ubuntu.com/manpages/jammy/en/man1/unzip.1.html)
: Descompacta arquivo de formato .zip.

    unzip [file]

## V

## W

[wget](https://manpages.ubuntu.com/manpages/jammy/en/man1/wget.1.html)
: Baixar um arquivo da web.

    wget [URL]

## X

## Y

## Z

[zip](https://manpages.ubuntu.com/manpages/jammy/en/man1/zip.1.html)
: Compacta arquivo no formato .zip

<justify> Para checar mais manuais de ferramentas do Ubuntu pode-se checar a [página de manuais oficial do Ubuntu](https://manpages.ubuntu.com/)</justify>
[EOF]