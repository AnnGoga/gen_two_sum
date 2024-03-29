# gen_two_sum  
Оригинальная программа получает сгенерированный массив целых чисел и сгенерированный таргет (int), а возвращает индексы двух чисел, сумма значений которых дает таргет. По условиям нельзя использовать один и тот же элемент дважды.    
После засекается среднее время работы программы по двум типам решений.    
Пример:   
Заданные числа = [2, 7, 11, 15], таргет = 9  
nums [ 0 ] + nums [ 1 ] = 2 + 7 = 9, возврат [ 0 , 1 ].  
***
Первое решение:  
Brute-подход. 
Цикл через каждый элемент Х и найти, есть ли другое значение равное target - X  
Анализ сложности  
Сложность времени: O(n^2)  
Пространственная сложность: O(1)  

Второе решение:  
Хэш-таблица
Чтобы улучшить  сложность во время выполнения, нам нужен более эффективный способ проверить, существует ли пара в массиве. Если пара существует, нам нужно посмотреть ее индекс.  Наилучший способ реализовать сопоставление каждого элемента в массиве с его индексом Хеш-таблица.  
Мы сокращаем время поиска от O(n) для O(1) путем обмена пространства на скорость. Хеш-таблица создана специально для этой цели, она поддерживает быстрый поиск в почти адекватное время.   
Простая реализация использует две итерации. На первой итерации мы добавляем значение каждого элемента и его индекс в таблицу. Затем во второй итерации мы проверяем (target - nums [i]) существует ли в таблице пара. Важно помнить, что нет пары для nums[i] самого.
***  
![1](https://github.com/AnnGoga/gen_two_sum/blob/master/replit.jpg)  
![2](https://github.com/AnnGoga/gen_two_sum/blob/master/rep2.jpg.png)  
