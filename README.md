# Capify Api

## Run

```bash
docker compose up -d
```

Go to on [http://localhost:8000/](http://localhost:8000)

## Dev

Install dependencies

```bash
poetry install
```

Activate env

```bash
poetry shell
```

Install git hooks

```bash
pre-commit install
```

Configure secrets

```bash
cp example.settings.yaml settings.yaml
cp example.env .env
```

Set up MongoDB and mongo-exporess instances

```bash
docker compose up -d mongodb mongo-express
```

Run ASGI server

```bash
python -m src
```

Go to [http://localhost:8000/](http://localhost:8000)
