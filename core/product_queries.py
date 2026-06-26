from core.models import Product, Category, Tag

def tag_seed():
    tags = ['Новинка', 'Распродажа', 'Эко', 'Премиум']
    for tag_name in tags:
        Tag.objects.get_or_create(name=tag_name)

def category_seed():
    categories = ['Электроника', 'Одежда', 'Книги', 'Дом и сад']
    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name)

def product_seed():
    # Получаем категории и теги для связи с продуктами
    electronics, _ = Category.objects.get_or_create(name='Электроника')
    clothing, _ = Category.objects.get_or_create(name='Одежда')
    
    tag_new, _ = Tag.objects.get_or_create(name='Новинка')
    tag_eco, _ = Tag.objects.get_or_create(name='Эко')

    # Создаем тестовые продукты
    p1, _ = Product.objects.get_or_create(name='Смартфон', category=electronics)
    p1.tags.add(tag_new)

    p2, _ = Product.objects.get_or_create(name='Футболка хлопковая', category=clothing)
    p2.tags.add(tag_eco, tag_new)

    p3, _ = Product.objects.get_or_create(name='Ноутбук', category=electronics)
    p3.tags.add(tag_new)