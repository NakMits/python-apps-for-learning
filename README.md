# python-apps-for-learning
python-apps-for-learning  

# 使い方
* pythonの3.Xをインストール  
* powershell起動 → pipenvをインストール（pip install pipenv）  
* python-apps-for-learning\\.env.sampleを同階層にコピー → リネーム（.env） → 各項目を編集  
* python-apps-for-learning\ で powershell起動（ctrl + shift + 右クリック → powershellウィンドウをここで開く）  
* 仮想環境構築（pipenv install）  
* DB構成ファイル作成（pipenv run python manage.py makemigrations）  
* DB反映（pipenv run python manage.py migrate）  
* 仮想環境起動、webサーバー起動（pipenv run python manage.py runserver）  
* ブラウザでアクセス（ http://127.0.0.1:8000/ ）  