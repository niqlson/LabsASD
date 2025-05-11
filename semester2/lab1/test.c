#include <stdio.h>
#include <stdlib.h>

double loop(double x, unsigned int n) {
    int i;
    double xSquare = x * x;
    double sum = x;
    double F = x;

    for (i = 1; i < n; i++) {
        F = F * (2 * i - 1) * (2 * i - 1) * xSquare / (4 * i * i + 2 * i );
        sum += F;
    }

    return sum;
}


int main()
{
    unsigned int n;
    double x;

    printf("Enter x: ");
    scanf("%lf", &x);
    printf("Enter n: ");
    scanf("%u", &n);

    if (x > -1 && x < 1) {
        printf("Result: %.8lf\n", loop(x, n));
    }
    else {
        printf("x must be in the range (-1; 1)\n");
    }

    return 0;
}
