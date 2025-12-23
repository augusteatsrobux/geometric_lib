# Документация geometric_lib

## Общее описание

Библиотека geometric_lib содержит функции для вычисления площади и периметра геометрических фигур - круга и квадрата. Библиотека написана на Python.

## Описание функций

### Модуль circle.py

#### Функция area(r)
Вычисляет площадь круга.

Формула: S = πR²

Пример:
```python
import circle

r = 2
s = circle.area(r)
print(s)  # out: 12.56637061
```

#### Функция perimeter(r)
Вычисляет периметр круга.

Формула: P = 2πR

Пример:
```python
import circle

r = 2
p = circle.perimeter(r)
print(p)  # out: 12.56637061
```

### Модуль square.py

#### Функция area(a)
Вычисляет площадь квадрата.

Формула: S = a²

Пример:
```python
import square

a = 2
s = square.area(a)
print(s)  # out: 4
```

#### Функция perimeter(a)
Вычисляет периметр квадрата.

Формула: P = 4a

Пример:
```python
import square

a = 2
p = square.perimeter(a)
print(p)  # out: 8
```

## История изменений

- d078c8d - L-03: Docs added
- 8ba9aeb - L-03: Circle and square added

