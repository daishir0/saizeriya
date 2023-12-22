import sys
import cv2
import numpy as np
from datetime import datetime
from skimage import io

def align_images(im1, im2):
    # 画像をグレースケールに変換
    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    
    # ORBディテクタを使用して特徴点を検出し、ディスクリプタを計算
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
    
    # 特徴点マッチングを行う
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)
    
    # 距離によってマッチをソート
    matches = sorted(matches, key=lambda x: x.distance)
    
    # 良いマッチの座標を抽出
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)
    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt
    
    # ホモグラフィーを計算
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
    
    # ホモグラフィーを使用して画像を変形し、画像を整列させる
    height, width = im2.shape[:2]
    im1_aligned = cv2.warpPerspective(im1, h, (width, height))
    
    return im1_aligned

def compute_difference(im1, im2):
    # 画像の差分を計算
    diff = cv2.absdiff(im1, im2)
    # 差分が閾値以上のものをマーク
    _, thresh = cv2.threshold(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY), 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 差分を赤色でマークするために画像に輪郭を描画
    im2_diff = im2.copy()
    cv2.drawContours(im2_diff, contours, -1, (0, 0, 255), 3)  # 赤色に変更
    return im2_diff

def main(imageA_path, imageB_path):
    # 画像を読み込む
    imageA = io.imread(imageA_path)
    imageB = io.imread(imageB_path)

    # 画像を整列させる
    imageA_aligned = align_images(imageA, imageB)

    # 差分を計算してマークする
    marked_diff_image = compute_difference(imageA_aligned, imageB)

    # 結果の画像をカレントディレクトリに保存
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = f"{current_time}.png"
    diff_filename = f"{current_time}-diff.png"

    # 差分がマークされた画像を保存
    io.imsave(output_filename, marked_diff_image)

    # 差分だけの画像を生成
    diff_only_image = cv2.absdiff(imageA_aligned, imageB)

    # 差分だけの画像を保存
    io.imsave(diff_filename, diff_only_image)
    
    print(f"Image processed. Marked output saved as {output_filename}")
    print(f"Diff only output saved as {diff_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <image1_path> <image2_path>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])
