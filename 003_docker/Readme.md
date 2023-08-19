# Instruções para uso do qiime2 com Docker

## Construindo a imagem do qiime2

- Baixe o Dockerfile
- Esteja no mesmo diretório do Dockerfile

```bash
docker build . -t qiime2-v8.22
```

## Rodando o qiime2 dentro do container

```bash
docker run --rm -it -v [PATH_TO_DATA_DIRECTORY]:/data qiime2-v8.22 qiime --help
```

## Apagando a imagem do qiime2

```bash
docker rmi qiime2-v8.22:latest
```
