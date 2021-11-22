from skimage.metrics import structural_similarity as compare_ssim
import cv2

if __name__ == "__main__":
    imageA = cv2.imread("путь к оригинальному изображению")
    imageB = cv2.imread("путь к изображению из отклика")

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    score = compare_ssim(grayA, grayB, full=True)[0] * 100
    if score > 95:
        print(True)
    else:
        print(False)

"""
где score - регулируемая обсуждаемая величина. 
Для следующего пака изображений проверка выше проходит только для файла 002.png, 
исходное изображение - 001.png, остальные два изображения проверку по схожести не проходят. 
При величине score > 94 проверку проходят все 3 изображения.

"""
