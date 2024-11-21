#include <stdio.h>

#define ROWS 7
#define COLS 10

int binarySearch(double row[], int cols, double min, double max, double* value) {
  int left = 0, right = cols - 1;
  int index = -1;

  while (left <= right) {
    int mid = left + (right - left) / 2;

    if (row[mid] >= min && row[mid] <= max) {
      index = mid;  
      *value = row[mid];  
      right = mid - 1;     
    }
    else if (row[mid] < min) {
      right = mid - 1;     
    } 
    else {
      left = mid + 1;      
    }
  }

  return index;  
}

int main() {
  double matrix[ROWS][COLS] = {
      {10.0, 8.5, 5.0, 5.0, 4.0, 3.5, 3.1, 2.2, 1.5, 0.9},
      {15.0, 14.0, 12.0, 10.0, 5.0, 4.9, 4.5, 3.0, 2.0, 0.1},
      {50.0, 40.0, 30.0, 20.0, 20.0, 15.0, 13.3, 8.2, 8.1, 7.5},
      {4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0},
      {8.5, 8.4, 7.5, 7.0, 6.5, 6.0, 5.9, 5.8, 5.6, 0.0},
      {6.0, 5.0, 4.8, 4.6, 4.4, 3.9, 3.5, 3.2, 2.8, 2.5},
      {9.9, 9.5, 8.5, 6.5, 5.6, 5.5, 3.5, 2.5, 1.5, 0.5},
    };
  double min = 0.0, max = 5.0;  

  printf("Matrix:\n");
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      printf("%6.1f ", matrix[i][j]);
    }
    printf("\n");
  }
  printf("\n");

  printf("Search results:\n");
  for (int i = 0; i < ROWS; i++) {
    double value = 0.0;  
    int col = binarySearch(matrix[i], COLS, min, max, &value);
    if (col != -1) {
      printf("Row %d, Column %d, Value: %.1f\n", i, col, value);
    } else {
      printf("No element in range [%.1f, %.1f] found in row %d\n", min, max, i);
    }
  }

  return 0;
}
