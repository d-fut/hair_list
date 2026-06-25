#!/usr/bin/env bash
# 使い方: bash setup_github.sh <github-username> <repo-name>
# 事前にGitHubで空リポジトリを作成しておくこと。
set -e
USER="$1"; REPO="$2"
if [ -z "$USER" ] || [ -z "$REPO" ]; then
  echo "Usage: bash setup_github.sh <github-username> <repo-name>"; exit 1
fi
git init
git add .
git commit -m "髪型見本カタログ 初版"
git branch -M main
git remote add origin "https://github.com/$USER/$REPO.git"
git push -u origin main
echo "完了。GitHub の Settings → Pages で main / root を有効化してください。"
echo "公開URL: https://$USER.github.io/$REPO/"
