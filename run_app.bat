@echo off
chcp 65001 >nul

:: Pythonのインストール確認
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pythonがインストールされていないか、環境変数が設定されていません。
    echo Pythonをインストールして、環境変数PATHに追加してください。
    pause
    exit /b
)

:: 必要なライブラリをインストール
echo 必要なPythonライブラリをインストール中...
pip install flask >nul 2>&1
if %errorlevel% neq 0 (
    echo Flaskライブラリのインストールに失敗しました。
    pause
    exit /b
)

:: app.pyを実行
echo Pythonスクリプトを実行します...
python app.py

:: 実行終了メッセージ
echo アプリケーションを終了しました。
pause
exit
