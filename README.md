# dynamodb-practice

よくわかってない（＾～＾）　練習（＾～＾）

📖　[AWSにデータベースサーバーってどうやって置くの（＾～＾）？](https://crieit.net/drafts/61890804402ea)  

## Set up

```shell
pip install pprintpp
pip install boto3
```

## AWS CLI テスト

```shell
aws ec2 describe-instances
```

## テスト

Music テーブルからアイテム取得。条件はJSONファイルに記載

```shell
aws dynamodb query --table-name Music --key-conditions file://key-conditions.json
```

📖 [ステップ 1: Python を使用してテーブルを作成する](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html)  
📖 [【Windows】Pythonをアップデートする](https://www.suzu6.net/posts/224-python-windows-update/)  

📖 [Step 5: (Optional) Delete the Table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.05.html)  
