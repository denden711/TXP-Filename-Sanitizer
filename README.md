# TXP Filename Sanitizer

## 概要
TXP Filename Sanitizerは、指定されたフォルダ内の.txpファイルから不要な文字's'を削除し、ファイル名を変更するためのGUIツールです。

## 特徴
- GUIを使用して簡単にフォルダを選択できます。
- .txpファイル名から's'を削除し、新しいファイル名で保存します。
- ファイル名が既に存在する場合は警告を表示します。

## 動作環境
- Python 3.x
- tkinterライブラリ

## インストール
このプログラムを実行するために、以下の手順に従ってください：

1. リポジトリをクローンします：
   ```sh
   git clone https://github.com/yourusername/txp-filename-sanitizer.git
   ```
2. 必要なPythonパッケージをインストールします：
   ```sh
   pip install tkinter
   ```

## 使用方法
1. プログラムを実行します：
   ```sh
   python txp_filename_sanitizer.py
   ```
2. 「参照」ボタンをクリックして、ファイル名を変更したいフォルダを選択します。
3. 「実行」ボタンをクリックして、フォルダ内の.txpファイル名から's'を削除します。

## ファイルの説明
- `txp_filename_sanitizer.py`: メインのGUIプログラムファイル。

## ライセンス
このプロジェクトは、個人利用のためフリーで提供されています。

## 貢献
バグ報告や機能提案は、GitHubのリポジトリのIssueセクションを通じて行ってください。
