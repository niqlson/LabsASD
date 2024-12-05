#include <stdio.h>

#define ROWS 7
#define COLS 10

// Bubble Sort with Flag to sort an array in non-decreasing order
void bubbleSortAscendingWithFlag(int arr[], int n) {
  int temp;
  int swapped;

  for (int i = 0; i < n - 1; i++) {
    swapped = 0; // Reset the flag
    for (int j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) { // Non-decreasing order
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = 1; // Flag to indicate a swap occurred
      }
    }
    if (!swapped) {
      break; // Exit early if no swaps were made
    }
  }
}

int main() {
  int matrix[ROWS][COLS] = {
    {10, 20, 30, 40, 50, 60, 70, 80, 90, 100},
    {110, 120, 130, 140, 150, 160, 170, 180, 190, 200},
    {210, 220, 230, 240, 250, 260, 270, 280, 290, 300},
    {310, 320, 330, 340, 350, 360, 370, 380, 390, 400},
    {410, 420, 430, 440, 450, 460, 470, 480, 490, 500},
    {510, 520, 530, 540, 550, 560, 570, 580, 590, 600},
    {610, 620, 630, 640, 650, 660, 670, 680, 690, 700},
  };

  printf("Original Matrix:\n");
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      printf("%3d ", matrix[i][j]);
    }
    printf("\n");
  }

  // Extract odd-indexed elements (rows 1, 3, 5) from the last column
  int oddElements[(ROWS + 1) / 2]; // Array for odd-indexed elements
  int k = 0;

  for (int i = 1; i < ROWS; i += 2) { // Rows: 1, 3, 5
    oddElements[k++] = matrix[i][COLS - 1];
  }

  // Sort the odd elements in non-decreasing order using Bubble Sort with Flag
  bubbleSortAscendingWithFlag(oddElements, k);

  // Place sorted odd elements back into their original positions
  k = 0;
  for (int i = 1; i < ROWS; i += 2) {
    matrix[i][COLS - 1] = oddElements[k++];
  }

  printf("\nModified Matrix:\n");
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      printf("%3d ", matrix[i][j]);
    }
    printf("\n");
  }

  return 0;
}
