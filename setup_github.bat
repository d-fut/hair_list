@echo off
REM 使い方: setup_github.bat <github-username> <repo-name>
if "%~2"=="" (
  echo Usage: setup_github.bat ^<github-username^> ^<repo-name^>
  exit /b 1
)
git init
git add .
git commit -m "髪型見本カタログ 初版"
git branch -M main
git remote add origin https://github.com/%1/%2.git
git push -u origin main
echo 完了。GitHub の Settings -^> Pages で main / root を有効化してください。
echo 公開URL: https://%1.github.io/%2/
