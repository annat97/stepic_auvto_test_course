import xml.etree.ElementTree as ET
import csv
import os
import sys

# Настройки фильтра
NEW_LIMIT = 3000
OLD_LIMIT = 5000

def parse_xml(filepath):
    if not os.path.exists(filepath):
        print(f"❌ Файл {filepath} не найден. Убедитесь, что он лежит в папке 'Загрузки'.")
        return None
        
    print(f"⏳ Читаем {filepath} (может занять пару секунд, файл большой)...")
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"❌ Ошибка в XML файле {filepath}: {e}")
        return None

    offers = []
    # Ищем все теги <offer>
    for offer in root.iter('offer'):
        oid = offer.get('id', 'unknown')
        available = offer.get('available', 'unknown')
        price_text = offer.findtext('price')
        cat_text = offer.findtext('categoryId', 'unknown')
        name = offer.findtext('name', 'Без названия')
        
        # Если цены нет (например, в product.xml), пропускаем
        if not price_text:
            continue
            
        try:
            price = float(price_text.replace(',', '.').strip())
        except ValueError:
            continue

        offers.append({
            'id': oid,
            'price': price,
            'available': available,
            'categoryId': cat_text,
            'name': name
        })
    return offers

def analyze_and_save(filepath, offers):
    if not offers:
        print(f"⚠️ В файле {filepath} не найдено тегов <price>. Возможно, это фид без цен (только каталог). Пропускаем.")
        return

    buckets = {
        'below_3000': [],
        'exactly_3000': [],
        'between_3000_5000': [],
        'above_5000': []
    }

    for o in offers:
        p = o['price']
        if p < NEW_LIMIT:
            buckets['below_3000'].append(o)
        elif p == NEW_LIMIT:
            buckets['exactly_3000'].append(o)
        elif p < OLD_LIMIT:
            buckets['between_3000_5000'].append(o)
        else:
            buckets['above_5000'].append(o)

    # Вывод в консоль
    print(f"\n==================================================")
    print(f"📊 ОТЧЕТ ПО ФАЙЛУ: {filepath}")
    print(f"Всего товаров с ценами: {len(offers)}")
    print(f"==================================================")
    
    print(f"🔴 Цена < {NEW_LIMIT} руб. (НЕ должны передаваться): {len(buckets['below_3000'])}")
    if buckets['below_3000']:
        print("   ⚠️ ВНИМАНИЕ: Найдены товары ниже нового порога! Это баг (см. CSV).")
    
    print(f"🟢 Цена ровно {NEW_LIMIT} руб. (Граница, должны быть): {len(buckets['exactly_3000'])}")
    if not buckets['exactly_3000']:
        print(f"   ℹ️ Товаров с ценой ровно {NEW_LIMIT} нет.")
    
    print(f"🟡 Цена от {NEW_LIMIT} до {OLD_LIMIT} руб. (Доказывает, что порог сдвинут): {len(buckets['between_3000_5000'])}")
    if not buckets['between_3000_5000']:
        print("   ⚠️ ПОДОЗРИТЕЛЬНО: Нет товаров в этом диапазоне. Возможно, порог всё ещё 5000.")

    print(f"🔵 Цена >= {OLD_LIMIT} руб. (Всё как раньше): {len(buckets['above_5000'])}")

    # Сохранение в CSV
    report_name = f"report_{os.path.basename(filepath).replace('.xml', '')}.csv"
    with open(report_name, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Группа', 'ID товара', 'Цена', 'В наличии', 'Категория', 'Название'])
        
        for bucket_name, items in buckets.items():
            for item in items:
                writer.writerow([
                    bucket_name, item['id'], item['price'], 
                    item['available'], item['categoryId'], item['name']
                ])
    print(f"\n✅ Файл с результатами сохранен: {report_name} (откройте его в Excel)")

if __name__ == '__main__':
    # Ищем файлы в текущей папке
    files_to_check = ['product.xml', 'price.xml']
    found_any = False
    
    for file in files_to_check:
        offers_data = parse_xml(file)
        if offers_data:
            found_any = True
            analyze_and_save(file, offers_data)
            
    if not found_any:
        print("\n❌ Не удалось найти данные для анализа.")
        print("Убедитесь, что файлы product.xml и price.xml лежат в той же папке, откуда вы запускаете скрипт.")
    