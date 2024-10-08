### Завдання 1 - оптимізація виробництва

#### Результати Розв'язання:

- Кількість лимонаду: 30.0 одиниць
- Кількість фруктового соку: 20.0 одиниць
- Загальна кількість продуктів: 50.0 одиниць

### Завдання 2 - обчислення визначеного інтеграла

#### Результати Розв'язання:

- Числовий інтеграл: 2.666666666666667 з помилкою 2.960594732333751e-14
- Monte Carlo інтеграл (100 точок): 2.48
- Monte Carlo інтеграл (1000 точок): 2.76
- Monte Carlo інтеграл (10000 точок): 2.672
- Monte Carlo інтеграл (100000 точок): 2.64912
- Monte Carlo інтеграл (1000000 точок): 2.667488

#### Висновки:

- Як видно з результатів, оцінка інтеграла методом Монте-Карло наближається до точного значення зі збільшенням кількості точок. Це очікуваний результат, оскільки точність методу Монте-Карло зростає при збільшенні числа випадкових точок.
- Для малого числа точок (100 та 1000) результати значно відрізняються від точного значення. Наприклад, для 100 точок оцінка складає 2.48, а для 1000 точок - 2.76. Це показує, що при невеликій кількості точок результат може бути досить приблизним.
- При збільшенні числа точок до 10000 і більше результати стають ближчими до точного значення. Наприклад, для 10000 точок оцінка інтеграла становить 2.672, а для 100000 точок - 2.64912. Це свідчить про покращення точності.
- Найбільш точні результати отримані для 1000000 точок, де оцінка інтеграла становить 2.667488, що дуже близьке до точного значення 2.666666666666667 з помилкою 2.960594732333751e-14.
- Таким чином, метод Монте-Карло є ефективним інструментом для наближеного обчислення інтегралів, особливо коли аналітичне обчислення є складним або неможливим. Однак, функція quad з бібліотеки SciPy забезпечує більш точний результат з оцінкою абсолютної помилки, що підтверджує її високу точність у порівнянні з методом Монте-Карло.
- Цей висновок відображає точність методу Монте-Карло в залежності від кількості точок і показує, як наближення результату до точного значення покращується з ростом числа випадкових точок.
