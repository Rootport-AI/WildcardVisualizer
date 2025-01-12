
# WildcardVisualizer

WildcardVisualizer は、Flask ベースのツールで、ワイルドカードファイル間の参照関係を視覚的に表現するアプリケーションです。ダブルクリックで簡単に起動でき、ブラウザで直感的に操作可能です。

## 特徴

- **参照関係の視覚化**:
  - ワイルドカード (`.txt` ファイル) の参照関係をインタラクティブなグラフとして描画します。
- **簡単な操作**:
  - ファイルを指定して、すぐに関係性を確認。
- **軽量な実装**:
  - Python Flask を使用し、簡単な構成で動作。

---

## 推奨環境

- **Python バージョン**: Python 3.10
  - 他のバージョンでの動作は確認していません。

---

## インストール

1. このリポジトリをクローンまたはダウンロードします。
   ```bash
   git clone https://github.com/Rootport-AI/WildcardVisualizer.git
   ```
   または [Download ZIP](https://github.com/Rootport-AI/WildcardVisualizer/archive/refs/heads/main.zip) をクリックしてZIPファイルをダウンロードし、展開します。

2. 必要なPythonライブラリをインストールします。
   ```bash
   pip install flask
   ```

---

## 使用方法

1. **起動**:
   - フォルダ内の `run_app.bat` をダブルクリックしてください。
   - これによりアプリケーションが起動します。

2. **アクセス**:
   - 起動後、ブラウザソフトで以下のURLにアクセスしてください。
     ```
     http://127.0.0.1:5000
     ```

3. **操作**:
   - 指定したフォルダ内のワイルドカードファイルを解析し、参照関係をグラフとして表示します。

---

## ファイル構成

```
WildcardVisualizer/
├── app.py                # Flaskアプリケーションのメインスクリプト
├── run_app.bat           # アプリケーション起動用バッチファイル
├── templates/
│   └── index.html        # フロントエンドのHTMLテンプレート
├── README.md             # このREADMEファイル
```

---

## 注意点

- **動作確認環境**:
  - 推奨環境は **Python 3.10** です。他のバージョンでは予期せぬ動作が起こる可能性があります。
- **セキュリティ**:
  - 開発用サーバーは本番環境には適していません。デプロイ時は適切なWSGIサーバー（例: Gunicorn、uWSGI）を使用してください。

---

## ライセンス

このプロジェクトは [MIT License](https://opensource.org/licenses/MIT) のもとで公開されています。詳細は `LICENSE` ファイルをご確認ください。

---

## 貢献

不具合の報告や改善提案は、このリポジトリの [Issues](https://github.com/username/WildcardVisualizer/issues) セクションで受け付けています。
