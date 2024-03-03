FROM python:3.12.2-alpine3.19
LABEL maintainer='vnicidigital@gmail.com'

# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Cria uma pasta onde ficara os arquivos do projeto
WORKDIR /app

COPY requirements.txt /app/
COPY commands.sh /app/


RUN pip install -r requirements.txt && \
    chmod -R +x /app/commands.sh


COPY . .

EXPOSE 8000

CMD [ "/app/commands.sh" ]