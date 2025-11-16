import pytest
import os
import sys
from PIL import Image
import numpy as np

# Добавляем корневую папку в путь для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, process_image


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Изменение контраста изображения' in response.data


def test_upload_page_not_found(client):
    """Тест GET запроса к /upload (должен вернуть 405)"""
    response = client.get('/upload')
    assert response.status_code == 405


def test_process_image_function():
    """Тест функции обработки изображения"""
    # Создаем тестовое изображение
    test_image = Image.new('RGB', (100, 100), color='red')

    # Обрабатываем изображение
    enhanced_img, hist_orig, hist_enh = process_image(test_image, 2.0)

    # Проверяем результаты
    assert enhanced_img is not None
    assert enhanced_img.size == test_image.size
    assert hist_orig is not None
    assert hist_enh is not None


def test_image_contrast_effect():
    """Тест изменения контраста"""
    # Создаем серое изображение
    test_image = Image.new('RGB', (10, 10), color=(128, 128, 128))

    # Увеличиваем контраст
    enhanced_img, _, _ = process_image(test_image, 2.0)
    enhanced_array = np.array(enhanced_img)

    # Проверяем, что контраст изменился (значения пикселей должны отличаться от исходных)
    assert not np.array_equal(enhanced_array, np.array(test_image))


if __name__ == '__main__':
    pytest.main()