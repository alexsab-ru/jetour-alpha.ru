#!/usr/bin/env python
import json
import os

COLOROFF='\033[0m'
BGYELLOW='\033[30;43m'
BGGREEN='\033[30;42m'
BGRED='\033[30;41m'
TEXTRED='\033[30;31m'

def print_message(message, type='info'):
    if type == 'info':
        print(message)
    elif type == 'warning':
        print(f"{BGYELLOW}{message}{COLOROFF}")
    elif type == 'error':
        print(f"{BGRED}{message}{COLOROFF}")
    elif type == 'success':
        print(f"{BGGREEN}{message}{COLOROFF}")

    with open('output.txt', 'a') as file:
        file.write(f"{message}\n")

# Загружаем model_mapping из JSON файла
def load_model_mapping(json_path: str = "./src/data/model_mapping.json"):
    """Загрузка маппинга моделей из JSON файла.
    
    Args:
        json_path (str): Путь к JSON файлу

    Returns:
        dict: Словарь с маппингом моделей

    """
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при загрузке {json_path}: {e}")
        return {}

model_mapping = load_model_mapping()

def get_model_info(brand: str, model: str, property: str = None, color: str = None, vin: str = None) -> str | dict | None:
    """
    Получение информации о модели автомобиля.
    
    Args:
        brand: Название бренда
        model: Название модели
        property: Запрашиваемое свойство ('folder', 'cyrillic' или 'colors')
        color: Цвет автомобиля
        vin: VIN автомобиля
    Returns:
        Запрошенная информация о модели или None, если информация не найдена
    """
    if vin:
        vin = vin.upper()

    # Нормализуем входные данные
    normalized_brand = brand.lower()
    normalized_model = model.lower()
    
    # Найдем бренд независимо от регистра
    brand_key = next(
        (key for key in model_mapping if key.lower() == normalized_brand),
        None
    )
    
    if not brand_key:
        errorText = f"\nvin: <code>{vin}</code>\n<b>Не хватает бренда</b> <code>{brand}</code> в model_mapping.json"
        print_message(errorText, 'error')
        return None
    
    # Найдем модель независимо от регистра
    model_key = next(
        (key for key in model_mapping[brand_key] if key.lower() == normalized_model),
        None
    )
    
    if not model_key:
        errorText = f"\nvin: <code>{vin}</code>\n<b>Не хватает модели</b> <code>{model}</code> бренда <code>{brand}</code> в model_mapping.json"
        print_message(errorText, 'error')
        return None
    
    model_data = model_mapping[brand_key][model_key]
    
    # Если запрашивается конкретный цвет
    if color:
        normalized_color = color.lower()
        color_key = next(
            (key for key in model_data['color'] if key.lower() == normalized_color),
            None
        )
        
        if color_key:
            return model_data['color'][color_key]
        else:
            errorText = f"\nvin: <code>{vin}</code>\n<b>Не хватает цвета</b> <code>{color}</code> модели <code>{model}</code> бренда <code>{brand}</code> в model_mapping.json"
            print_message(errorText, 'error')
            return None
    
    # Если запрашивается конкретное свойство
    if property:
        normalized_property = property.lower()
        if normalized_property in ['folder', 'cyrillic', 'short']:
            return model_data[normalized_property]
        elif normalized_property == 'colors':
            return model_data['color']
        else:
            errorText = f"\nvin: <code>{vin}</code>\n<b>Не хватает свойства</b> <code>{property}</code> модели <code>{model}</code> бренда <code>{brand}</code> в model_mapping.json"
            print_message(errorText, 'error')
            return None
    
    # Возвращаем все данные модели, если не указаны property и color
    return model_data


def get_folder(brand: str, model: str, vin: str = None) -> str | None:
    """Получение названия папки для модели."""
    return get_model_info(brand, model, 'folder', vin=vin)


def get_cyrillic(brand: str, model: str, vin: str = None) -> str | None:
    """Получение кириллического названия модели."""
    return get_model_info(brand, model, 'cyrillic', vin=vin)


def get_color_filename(brand: str, model: str, color: str, vin: str = None) -> str | None:
    """Получение имени файла для указанного цвета модели."""
    return get_model_info(brand, model, color=color, vin=vin)


def get_available_colors(brand: str, model: str, vin: str = None) -> dict | None:
    """Получение словаря доступных цветов для модели."""
    return get_model_info(brand, model, 'colors', vin=vin)


# Примеры использования:
"""
get_folder('Geely', 'Atlas Pro')         # Вернет: "Atlas Pro"
get_cyrillic('Geely', 'Atlas Pro')       # Вернет: "Атлас Про"
get_color_filename('Geely', 'Atlas Pro', 'Черный')  # Вернет: "black-metallic.webp"
get_color_filename('Geely', 'Atlas Pro', 'BLACK')   # Вернет: "black-metallic.webp"
get_available_colors('Geely', 'Atlas Pro')  # Вернет словарь со всеми доступными цветами

# Работает независимо от регистра:
get_folder('GEELY', 'ATLAS PRO')         # Вернет: "Atlas Pro"
get_color_filename('geely', 'atlas pro', 'ЧЕРНЫЙ')  # Вернет: "black-metallic.webp"
"""
