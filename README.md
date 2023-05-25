# waiwai

waiwai develop
backend

```
cd waiwai

docker compose up -d --build

docker compose exec python sh

uvicorn main:app --host 0.0.0.0 --port 8080
```

frontend
```
cd waiwai

docker compose up -d --build

docker compose exec next sh

yarn install

yarn dev
```