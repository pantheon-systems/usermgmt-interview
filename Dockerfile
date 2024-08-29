FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  git \
  vim \
  curl \
  wget

COPY . /app

WORKDIR /app

RUN pip3 install poetry --break-system-packages
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8080

ENV DEBUG=True
ENV SECRET_KEY=8f3a12b9e7c54d6a9f0d2e1c8b7a3f6e
ENV DATABASE_URL=sqlite:////app/prod_database.db

RUN python3 setup_db.py

RUN useradd -m authservice && echo "authservice ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER authservice

CMD ["poetry", "run", "quart", "--app", "auth.main:app", "--debug", "run", "--host", "0.0.0.0", "--port", "8080"]
