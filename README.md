# waiwai

## 環境構築

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
``````

## backend規約

- 1ブランチ_1API_1PRとする
- PRコメントは下記のフォーマットに沿って記載
1. 実装内容
2. 検証に必要な手順と情報
3. 設計書URL
4. 備考

- 相互レビューを通過したもののみをdevelopにマージ
