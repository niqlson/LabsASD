#include <stdio.h>

int main(int argc, char const *argv[]) {
  float x, y = 0;
  printf("Enter x: ");
  scanf("%f", &x);
  if (x >= 2 && x <= 7) {
    y = x * x * x + 14;
    printf("f(%.2f) = %.2f\n", x, y);
  }
  else if (x > -13 && x < -3 || x >= 14) {
    y = -4 * x * x * x + 3 * x - 7;
    printf("f(%.2f) = %.2f\n", x, y);
  }
  else printf("no value\n");
  return 0;
}
