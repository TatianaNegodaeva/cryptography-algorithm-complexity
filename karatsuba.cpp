#include <iostream>
#include <cmath>
#include <string>

using namespace std;

// Функция для нахождения максимальной длины числа
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Функция для разбиения числа на две части
void split(int num, int& high, int& low, int m) {
    high = num / pow(10, m);
    low = num % (int)pow(10, m);
}

// Реализация метода Карацубы
int karatsuba(int x, int y) {
    // Базовый случай
    if (x < 10 || y < 10) {
        return x * y;
    }

    int n = max((int)log10(x) + 1, (int)log10(y) + 1);
    int m = n / 2; // Деление на 2

    int highX, lowX, highY, lowY;

    // Разбиваем x на две половины
    split(x, highX, lowX, m);
    // Разбиваем y на две половины
    split(y, highY, lowY, m);

    // 3 рекурсивных умножения
    int z0 = karatsuba(lowX, lowY); // x1 * y1
    int z1 = karatsuba((lowX + highX), (lowY + highY)); // (x0 + x1)(y0 + y1)
    int z2 = karatsuba(highX, highY); // x0 * y0

    return (z2 * pow(10, 2 * m)) + ((z1 - z2 - z0) * pow(10, m)) + z0;
}


