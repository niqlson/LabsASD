#include <stdio.h>
#include <stdlib.h>

double recursion(double x, unsigned int n, unsigned int i, double Fi, double sum) {
  if (i > 0) {
    Fi = Fi * (2 * i - 1) * (2 * i - 1) * x * x / (4 * i * i + 2 * i);
  } else {
    Fi = x;
  }

  double currentFi = Fi;
  i++;

  if (i < n) {
    sum = recursion(x, n, i, Fi, sum);
  }

  sum += currentFi;
  return sum;
}

int main() {
  unsigned int n;
  double x;

  printf("Enter x: ");
  scanf("%lf", &x);
  printf("Enter n: ");
  scanf("%u", &n);

  if (x > -1 && x < 1) {
    printf("Result: %.8lf\n", recursion(x, n, 0, 0, 0));
  } else {
    printf("x must be in the range (-1; 1)\n");
  }

  return 0;
}
