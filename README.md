# image_clasification_anotation_gui

## 概要
Pythonのtkinterで開発したクラス分類器用のGUIアノテーションツール

## 環境
* python 3.6.5

## ショートカットキー
* 「→」：次の画像へ
* 「←」：前の画像へ
* 「数字キー」：指定したクラスを選択（9クラス目まで)
* 「アルファベットキー」：指定したクラスを選択（10クラス目から)

## 使い方
```
git clone https://github.com/Kentea-Watanabe/image_clasification_anotation_gui.git
```

```
python -m venv .venv
```

```
pip install -r requirements.txt
```

##  to do 
* python anotation_tool.pyの中身のinput画像のパスを変更

```
python anotation_tool.py
```

* ラベルの数だけ、json_csv.pyの中身のdf.dolumnsの値を指定する<br>
* json_csv.pyを実行し、jsonファイルをcsvファイルに出力する<br>
```
python json_csv.py
```

## Label形式
* label.csv

|    |  img_path  |  label  |
| ---- | ---- | ---- |
|  0  |  test1.jpg  | 0 |
|  0  |  test2.jpg  | 1 |

<br>

##  Sample image
![image](https://user-images.githubusercontent.com/87839643/184858357-3339a9a0-9343-4965-ad82-5b493bf0d390.png)
