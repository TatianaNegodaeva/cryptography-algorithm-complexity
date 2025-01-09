#include <iostream>
#include <string>
#include "karatsuba.cpp"
using namespace std;

int main() {
    int x, y;

    cout << "Введите первое число: ";
    cin >> x;
    cout << "Введите второе число: ";
    cin >> y;

    int result = karatsuba(x, y);
    cout << "Результат: " << result << endl;

    return 0;
}