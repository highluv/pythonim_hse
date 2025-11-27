import csv
import json

purchases = {}
# Читаем purchase_log.txt (каждая строка — JSON)
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        record = json.loads(line)     # превращаем JSON-строку в dict
        user_id = record.get('user_id')
        category = record.get('category')

        if user_id:
            purchases[user_id] = category

# Открываем funnel.csv для записи
with open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:
    writer = csv.writer(funnel_file)
    writer.writerow(['user_id', 'source', 'category'])  # header

    # 3. Читаем visit_log.csv построчно
    with open('visit_log__1_.csv', 'r', encoding='utf-8') as visit_file:
        reader = csv.DictReader(visit_file)
        for row in reader:
            user_id = row['user_id']

            # если есть покупка — записываем
            if user_id in purchases:
                writer.writerow([
                    user_id,
                    row['source'],
                    purchases[user_id]
                ])
