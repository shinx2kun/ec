## 開発環境構築

DB起動

```
docker-compose up -d
# mysqlにログインできることを確認 起動まで30秒-1分程度かかる
./manage.py dbshell
$ ./manage.py dbshell
mysql: [Warning] Using a password on the command line interface can be insecure.
...中略
mysql> exit
Bye
```

DBマイグレーション
```
./manage.py migrate
```

テストデータimport
```
./manage.py loaddata fixtures/users.json
```

## Django Tips

テストデータexport
```
./manage.py dumpdata users > fixtures/users.json
# is_staff, is_superuserはnullだとインポートに失敗するため手動で修正する必要あり
```
