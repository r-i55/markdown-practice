## 使用技術一覧
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2.  [開発背景](#開発背景)
3. [環境](#環境)
4. [ディレクトリ構成](#ディレクトリ構成)
5. [開発環境構築](#開発環境構築)

## プロジェクト名

Markdown to HTML Converter


## プロジェクトについて

- MarkdownファイルをHTMLファイルに変換するPythonスクリプトです。
- コマンドラインから入力・出力ファイルを指定可能です。


## 開発背景

Python の基礎学習の一環として、標準出力やファイル操作の理解を深めるために本プロジェクトを作成しました。  
コマンドライン引数を受け取って処理を実行する仕組みを実装し、Markdown の内容を HTML ファイルとして標準出力ではなくファイルに書き込む流れを体験することを目的としています。


## 環境

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.12.3     |
| OS                | Ubuntu 24.04.2 LTS     |


## ディレクトリ構成
```
.
├── file-converter.py
├── input_text.md
└── output_text.html
```

## 開発環境構築

### 1.リポジトリのクローン
```
git clone https://github.com/r-i55/markdown-practice.git
```

### 2.Pythonのバージョン確認
本プロジェクトはPython3系を前提としています。
```
python3 --version  # 例:Python 3.12.3
```

### 3.依存パッケージのインストール
```
sudo apt update
sudo apt install -y python3 python3-pip python3-markdown
```

### 4.動作確認
サンプルのMarkdownをHTMLに変換する場合
```
python3 file-converter.py input_text.md output_text.html
```



