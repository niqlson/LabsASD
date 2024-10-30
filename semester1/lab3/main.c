#include <stdio.h>
#include <stdbool.h>

#define M 10
#define N 8

void printMatrix(const double matrix[][N], int rows, int cols) {
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      printf("%.2lf\t", matrix[i][j]);
    }
    printf("\n");
  }
}

int main(const int argc, const char* argv[]) {
  const double matrix[M][N] = {
    { -8.37,  3.79,  4.93,  3.31,  0.04, -8.31,  5.83,  1.01  },
    {  7.33,  5.35, -6.19,  0.54,  2.31, -4.05,  2.64,  2.54  },
    { -7.47, -1.39, -2.57,  2.88,  8.03,  6.88,  0.61,  3.02  },
    { -8.85, -9.88,  7.63, -1.50,  2.70,  2.80, -9.33,  5.97  },
    {  2.09, -4.18,  4.82, -5.82,  2.57, -6.83,  5.09,  0.21  },
    {  6.14,  9.96,  7.74,  1.23, -7.13,  5.35, -1.25,  7.62  },
    { -7.53,  7.17, -1.72,  2.13, -1.62,  4.55, -2.47,  0.99  },
    { -4.55,  6.89, -3.56,  2.56,  7.62,  5.56,  0.19,  1.01  },
    {  7.33,  5.35, -6.19,  0.54,  2.31, -4.05,  2.64,  2.59  }, 
    {  2.09, -4.18,  4.82, -5.82,  2.57, -6.83,  5.09, -0.21  },
  };

  printMatrix(matrix, M, N);

  for (int i = 0; i < N; i++) {
  bool finded = false;
    for (int j = 0; j < M; j++) {
      const double item = matrix[j][i];
      if (item >= 0) continue;
      finded = true;
      printf("Item: %.2lf, position = (%d, %d)\n", item, j, i);
      break;
    }
    if (!finded) printf("There is not negative values in row\n");
  }

  return 0;
}
