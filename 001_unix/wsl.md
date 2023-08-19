# Instruções para a instalação do Ubuntu dentro do sistema Windows

Esse tutorial foi baseado nas instruções do [site](<https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview>) oficial do Ubuntu para instalação no Windows 10.

## Passo-a-passo

1. Vá ao menu iniciar e inicie o Powershell como administrador.

    DICA: Essa ação pode ser realizada clicando-se no ícone do windows e digirando powershell na barra de busca. Assim que selecionado o programa Windows Powershell pode-se selecionar a opção **Executar como administrador**.

2. Instale o wsl e o Ubuntu na tela de comando

    ```bash
    wsl --install -d ubuntu

    ```

3. Reinicie o computador.

4. Configure o Ubuntu com usuário e senha.

5. Atualize os pacotes do sistema.

    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    ```
