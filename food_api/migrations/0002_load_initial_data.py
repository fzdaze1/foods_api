# 0002_load_initial_data.py

from django.db import migrations, models


def create_initial_data(apps, schema_editor):
    FoodCategory = apps.get_model('food_api', 'FoodCategory')
    Food = apps.get_model('food_api', 'Food')

    drinks = FoodCategory.objects.create(name_ru='Напитки', order_id=10)
    bakery = FoodCategory.objects.create(name_ru='Выпечка', order_id=20)
    meat = FoodCategory.objects.create(name_ru='Мясо', order_id=30)

    tea = Food.objects.create(category=drinks, internal_code=100, code=1,
                              name_ru='Чай', description_ru='Чай 100 гр', cost='123.00', is_publish=True)
    cola = Food.objects.create(category=drinks, internal_code=200, code=2,
                               name_ru='Кола', description_ru='Кола', cost='123.00', is_publish=True)
    sprite = Food.objects.create(category=drinks, internal_code=300, code=3,
                                 name_ru='Спрайт', description_ru='Спрайт', cost='123.00', is_publish=True)
    baikal = Food.objects.create(category=drinks, internal_code=400, code=4,
                                 name_ru='Байкал', description_ru='Байкал', cost='123.00', is_publish=True)
    burger = Food.objects.create(category=bakery, internal_code=500, code=5,
                                 name_ru='Бургер', description_ru='Бургер', cost='150.00', is_publish=False)
    cake = Food.objects.create(category=bakery, internal_code=600, code=6,
                               name_ru='Торт', description_ru='Торт', cost='200.00', is_publish=True)
    pork = Food.objects.create(category=meat, internal_code=700, code=7,
                               name_ru='Свинина', description_ru='Свинина', cost='300.00', is_publish=False)
    beef = Food.objects.create(category=meat, internal_code=800, code=8,
                               name_ru='Говядина', description_ru='Говядина', cost='400.00', is_publish=False)
    tea.additional.add(cola)


class Migration(migrations.Migration):

    dependencies = [
        ('food_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
