# Instruções para uso do miniconda com Docker

## Construindo a imagem do miniconda

- Baixe o Dockerfile
- Esteja no mesmo diretório do Dockerfile

```bash
docker build . -t miniconda3
```

## Rodando o miniconda dentro do container

```bash
docker run --rm miniconda3
```

## Apagando a imagem do miniconda

```bash
docker rmi miniconda3:latest
```
