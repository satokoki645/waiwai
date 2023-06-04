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

npm install

npm dev
```

storybook
```
cd waiwai

docker compose up -d --build

docker compose exec storybook sh

npm install

npm run build-storybook
```