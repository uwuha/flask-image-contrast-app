import os
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageEnhance
import matplotlib
# Используем "Агрегатный" бэкенд, чтобы matplotlib не пытался открывать окно
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import numpy as np

app = Flask(__name__)

# Создаем папки, если они не существуют
os.makedirs('static/uploads', exist_ok=True)
os.makedirs('static/results', exist_ok=True)

@app.route('/')
def index():
    """Главная страница с формой загрузки."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Обработка загруженного файла и данных формы."""
    # 1. Получаем файл и значение контраста из формы
    file = request.files['file']
    contrast_level = float(request.form['contrast'])

    # 2. Сохраняем загруженное изображение
    upload_path = os.path.join('static', 'uploads', file.filename)
    file.save(upload_path)

    # 3. Обрабатываем изображение
    original_img = Image.open(upload_path)
    enhanced_img, hist_original, hist_enhanced = process_image(original_img, contrast_level)

    # 4. Сохраняем результаты (изображение и графики)
    # Уникальные имена файлов, чтобы избежать конфликтов
    base_name = os.path.splitext(file.filename)[0]
    result_img_path = os.path.join('static', 'results', f"{base_name}_enhanced.png")
    hist_original_path = os.path.join('static', 'results', f"{base_name}_hist_original.png")
    hist_enhanced_path = os.path.join('static', 'results', f"{base_name}_hist_enhanced.png")

    enhanced_img.save(result_img_path)
    hist_original.savefig(hist_original_path)
    hist_enhanced.savefig(hist_enhanced_path)

    # Закрываем графики, чтобы освободить память
    plt.close(hist_original)
    plt.close(hist_enhanced)

    # 5. Передаем пути к файлам в шаблон для отображения
    return render_template('result.html',
                           original_image=upload_path,
                           enhanced_image=result_img_path,
                           hist_original=hist_original_path,
                           hist_enhanced=hist_enhanced_path)

def process_image(image, contrast_factor):
    """
    Изменяет контраст изображения и строит гистограммы.

    Args:
        image (PIL.Image): Исходное изображение.
        contrast_factor (float): Уровень контраста (1.0 - оригинал, >1 - увеличить, <1 - уменьшить).

    Returns:
        tuple: (Улучшенное изображение, Объект графика исходной гистограммы, Объект графика новой гистограммы)
    """
    # Конвертируем в RGB, если изображение в другом режиме (например, PNG с прозрачностью)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Увеличиваем контраст
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(contrast_factor)

    # Строим гистограммы
    # Конвертируем изображения в numpy массивы
    original_array = np.array(image)
    enhanced_array = np.array(enhanced_image)

    # Создаем графики
    fig_orig, ax_orig = plt.subplots(figsize=(8, 4))
    fig_enh, ax_enh = plt.subplots(figsize=(8, 4))

    # Гистограмма для исходного изображения
    for i, color in enumerate(['red', 'green', 'blue']):
        ax_orig.hist(original_array[..., i].ravel(), bins=256, range=(0, 256),
                     color=color, alpha=0.5, label=color)
    ax_orig.set_title('Гистограмма исходного изображения')
    ax_orig.set_xlabel('Значение пикселя')
    ax_orig.set_ylabel('Частота')
    ax_orig.legend()

    # Гистограмма для измененного изображения
    for i, color in enumerate(['red', 'green', 'blue']):
        ax_enh.hist(enhanced_array[..., i].ravel(), bins=256, range=(0, 256),
                    color=color, alpha=0.5, label=color)
    ax_enh.set_title('Гистограмма изображения после контраста')
    ax_enh.set_xlabel('Значение пикселя')
    ax_enh.set_ylabel('Частота')
    ax_enh.legend()

    # Убираем лишние пробелы вокруг графиков
    fig_orig.tight_layout()
    fig_enh.tight_layout()

    return enhanced_image, fig_orig, fig_enh

if __name__ == '__main__':
    # Запускаем приложение в режиме отладки (debug=True)
    # Для продакшена debug должен быть False!
    app.run(debug=True)