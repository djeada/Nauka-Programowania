#include <iostream>

void pascal(int n)
{

    for (int i = 1; i <= n; ++i) {
        int k = 1;
        for (int j = 1; j <= n - i; ++j)
            std::cout << " ";

        for (int j = 1; j <= i; j++) {
            std::cout << k << " ";
            k *= (i - j) / j;
        }

        std::cout << std::endl;
    }
}

int main()
{

    int a = 5;
    pascal(a);

    return 0;
}
