#include<stdio.h>
#include<math.h>

double f(unsigned n, unsigned* cntOperations) {
  double result = 1;
  unsigned cnt = 5;     
  double lnsSum = 0.0;
  for (int i = 1; i <= n; i++) {
    lnsSum = lnsSum + log(i + 2);
    const double cosinuse = cos(i);
    result = result * ((3 - cosinuse*cosinuse) / lnsSum);
    cnt += 13;      
  }
  *cntOperations = cnt;
  return result;
}

int main(int argc, char*argv[]) {
  unsigned n, cntOperations;
  printf("Enter natural number: ");
  scanf("%u", &n);
  double res = f(n, &cntOperations);
  printf("f(%d) = %.7lf\n Count of operations = %u\n", n, res, cntOperations);
  return 0;
}
