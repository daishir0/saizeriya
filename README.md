#### Overview
`saizeriya.py` is a Python script for aligning two images and detecting differences. It is useful for applications like image comparison, change detection, and quality control.

#### Installation
1. Clone the repository: `git clone https://github.com/daishir0/saizeriya`
2. Navigate to the project directory: `cd saizeriya`
3. Install dependencies: `pip install -r requirements.txt`

#### Usage
Run the script with two images as arguments:
```
python saizeriya.py <path_to_image1> <path_to_image2>
```

#### Example
Command:
```
python saizeriya.py sai1.png sai2.png
```
Output Images:
- Aligned and difference-marked image: ![yyyymmdd-hhmmss.png](yyyymmdd-hhmmss.png)
- Difference-only image: ![yyyymmdd-hhmmss-diff.png](yyyymmdd-hhmmss-diff.png)

#### Notes
- Ensure that the input images are of similar size and orientation.
- The script may not perform well with images having very few feature points.

#### License
This project is licensed under the MIT License.

---


#### 概要
`saizeriya.py`は、二つの画像を整列させて差異を検出するためのPythonスクリプトです。画像比較、変更検出、品質管理などに役立ちます。

#### インストール方法
1. リポジトリをクローンする: `git clone https://github.com/daishir0/saizeriya`
2. プロジェクトディレクトリに移動する: `cd saizeriya`
3. 依存関係をインストールする: `pip install -r requirements.txt`

#### 使い方
スクリプトを二つの画像を引数にして実行します：
```
python saizeriya.py <path_to_image1> <path_to_image2>
```

#### 実行例
コマンド:
```
python saizeriya.py sai1.png sai2.png
```
出力画像:
- 整列され、差分がマークされた画像: ![yyyymmdd-hhmmss.png](yyyymmdd-hhmmss.png)
- 差分のみの画像: ![yyyymmdd-hhmmss-diff.png](yyyymmdd-hhmmss-diff.png)

#### 注意点
- 入力される画像は、似たサイズと向きであることを確認してください。
- 特徴点が非常に少ない画像では、スクリプトの性能が落ちる可能性があります。

#### ライセンス
このプロジェクトはMITライセンスの下にあります。
