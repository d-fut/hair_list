# 髪型見本カタログ / Hairstyle Reference

アニメ調の髪型・髪色見本を一覧できるカタログです。ComfyUI で生成した画像を、日本語名・英語名つきのギャラリーで閲覧できます。

**▶ 公開ページ:** `https://<ユーザー名>.github.io/<リポジトリ名>/index.html`
（GitHub Pages 有効化後に表示されます。下記「公開手順」参照）

## 収録数

全 234 種

| カテゴリ | 件数 |
|---|---|
| 髪質 | 15 |
| 長さ | 17 |
| カット | 19 |
| セット | 18 |
| 結い方 | 39 |
| 前髪 | 16 |
| パーツ | 16 |
| 髪色 | 34 |
| サロン(トレンド) | 12 |
| サロン(メンズ) | 12 |
| 職業・転身 | 10 |
| 時代物(和) | 8 |
| 時代物(洋) | 8 |
| 創作・ファンタジー | 10 |

## ファイル構成

| ファイル | 内容 |
|---|---|
| `index.html` | 見本ギャラリー（単体で開けます。検索・絞り込み・クリック拡大対応） |
| `hair_list.csv` | マスターリスト（日本語名/英語名/性別/角度/生成タグ/Danbooruランク等） |
| `prompt.txt` | ComfyUI 用 生成プロンプト（1行=1スタイル） |
| `filename.txt` | 出力ファイル名リスト |
| `label_en.txt` | 画像に焼き込む英語ラベル |
| `hairstyle_csv.json` | ComfyUI ワークフロー |
| `danbooru_top_review.csv` | Danbooru 人気タグ抽出（和訳付き） |
| `compress_to_512jpg.py` | 画像を 512x512 JPEG に一括変換する補助スクリプト |
| `images/` | 生成画像（`<filename>_00001_.jpg` 形式） |

## 生成について

- モデル: アニメ調（animayume 系）/ 512x512 / JPEG
- 生成タグは Danbooru の人気タグに準拠
- 髪色・ファンタジー・西洋系は人種指定なし、それ以外は日本人指定

## 公開手順（GitHub Pages）

1. このリポジトリを GitHub に push
2. リポジトリの **Settings → Pages** を開く
3. **Source** で `Deploy from a branch` を選択
4. **Branch** を `main` / フォルダ `/ (root)` に設定して Save
5. 数分後、`https://<ユーザー名>.github.io/<リポジトリ名>/index.html` で公開

## ローカルでの閲覧

`index.html` をブラウザで開くだけ（サーバー不要）。画像は同階層の `images/` を参照します。

## ライセンス / 注意

生成画像・リストの利用範囲は作成者の方針に従ってください。Danbooru タグは参照情報です。
