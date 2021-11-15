# dynamodb-practice

よくわかってない（＾～＾）　練習（＾～＾）

📖　[AWSにデータベースサーバーってどうやって置くの（＾～＾）？](https://crieit.net/drafts/61890804402ea)  

## AWS CLI テスト

```shell
aws ec2 describe-instances
```

## テスト

Music テーブルからアイテム取得。条件はJSONファイルに記載

```shell
aws dynamodb query --table-name Music --key-conditions file://key-conditions.json
```
