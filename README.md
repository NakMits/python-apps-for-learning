# python-apps-for-learning
<p align="center">
<a href="https://line.me/ti/g2/_ajekaURvGQFDnCKQ_Jqcg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default" alt="development chat">
    <img src="https://img.shields.io/badge/openchat-python%E3%82%A2%E3%83%97%E3%83%AA%E9%96%8B%E7%99%BA%F0%9F%94%B0-green?style=flat&logo=line&color=00C300&logoColor=FFFFFF" /></a>
<a href="https://www.notion.so/python-0631edd40f22451f892d246c11a62617" alt="development note">
    <img src="https://img.shields.io/badge/notion-python%E3%82%A2%E3%83%97%E3%83%AA%E9%96%8B%E7%99%BA%F0%9F%94%B0-green?style=flat&logo=notion&color=00C300&logoColor=FFFFFF" /></a>
<a href="https://github.com/NakMits/python-apps-for-learning" alt="pipenv locked python version">
    <img src="https://img.shields.io/github/pipenv/locked/python-version/NakMits/python-apps-for-learning" />
</a>
<a href="https://github.com/NakMits/python-apps-for-learning" alt="django version">
    <img src="https://img.shields.io/badge/django-v3.2.4-blue?style=flat" />
</a>
<a href="https://github.com/NakMits/python-apps-for-learning/graphs/contributors" alt="repository contributors">
    <img src="https://img.shields.io/github/contributors/NakMits/python-apps-for-learning" />
</a>
</p>

## 前提
このリポジトリは勉強のために、Webアプリケーションを0からみんなで作ってみようというプロジェクトです
production-readyではないのでご注意ください。

## 内容
Googleマップに口コミ(ピン)を投稿しみんなで見れるWebアプリ 「レコマップ」

### できること
- Googleマップ上の任意の場所にコメントおよび画像を付けて口コミが投稿できる、また閲覧できる
- Googleアカウントでログインできる

### 利用ライブラリ
- [Django](https://docs.djangoproject.com/ja/3.2/intro/tutorial01/)
  - [social-auth-app-django](https://qiita.com/moi1990sk/items/a849fca7acb29db95508)
- [BootStrap5](https://getbootstrap.jp/docs/5.0/getting-started/introduction/)

### 利用API
- [Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript)
  - [Info window](https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple)

### ページ一覧
- トップページ
  - 内容未定
- マップページ
  - ユーザーが作成したマーカー群を見れる
    - ホットになっている場合マーカーが変わる
      - (コメント・いいねが付いたのが最近 AND/OR その数 でホットかどうかが決まる)
  - 各マーカーには いいねとコメントが追加できる
    - (マップページ内で完結させると技術的に複雑になるためマーカーページへ遷移)
- マーカーページ
  - ログイン中のユーザーが作成したマーカーを編集できる
    - 詳細ページ
      - 各マーカーの詳細が確認できる
        - 作成日時/付いたコメント/いいね数等
        - コメントを追加できる(要ログイン)
    - 一覧ページ(要ログイン)
      - 自分が投稿したマーカー一覧が確認できる
    - 追加ページ(要ログイン)
      - 任意の場所にマーカーを追加できる
    - 編集ページ(要ログイン)
      - 任意のマーカーを編集できる
    - 削除ページ(要ログイン)
      - 投稿したマーカーを削除できる
- アカウントページ
  - ログイン/サインアップページ
    - OAuth2で連携したアカウントでログインできる
  - ログアウトページ
    - 確認を挟んだ上でログアウトできる
- 管理者ページ
  - サイト管理者はユーザーの投稿したコンテンツを検閲できる
    - アカウント、マーカー、コメントを追加/編集/消去できる

## 環境構築
- pythonの3.Xをインストール
- powershell起動 → pipenvをインストール（pip install pipenv）
- python-apps-for-learning\\.env.sampleを同階層にコピー → リネーム（.env） → 各項目を編集
- python-apps-for-learning\ で powershell起動（ctrl + shift + 右クリック → powershellウィンドウをここで開く）
- 仮想環境構築（pipenv install）
- DB構成ファイル作成（pipenv run python manage.py makemigrations）
- DB反映（pipenv run python manage.py migrate）
- 仮想環境起動、webサーバー起動（pipenv run python manage.py runserver）
- ブラウザでアクセス（ http://127.0.0.1:8000/ ）