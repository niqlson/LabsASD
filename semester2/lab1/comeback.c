#include <stdio.h>
#include <stdlib.h>

struct previousRes {
  double Fi;
  double sum;
};

struct previousRes recursion(double x, unsigned int n) {
  double i = n - 1;
  struct previousRes currentRes;

  if (n > 1) {
    currentRes = recursion(x, n - 1);
    currentRes.Fi = currentRes.Fi * (2 * i - 1) * (2 * i - 1) * x * x / (4 * i * i + 2 * i);
  } else {
    currentRes.Fi = x;
    currentRes.sum = 0;
  }

  currentRes.sum += currentRes.Fi;
  return currentRes;
}

int main() {
  unsigned int n;
  double x;

  printf("Enter x: ");
  scanf("%lf", &x);
  printf("Enter n: ");
  scanf("%u", &n);

  if (x > -1 && x < 1) {
    struct previousRes finalRes = recursion(x, n);
    printf("Result: %.8lf\n", finalRes.sum);
  } else {
    printf("x must be in the range (-1; 1)\n");
  }

  return 0;
}
