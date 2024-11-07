#include <stdio.h>
#include <windows.h>

const char CHR = '$'; 

void putChar(const int x, const int y, const char symbol) {
  printf("\033[%d;%dH%c", y, x, symbol);
  Sleep(10);
}

void spiral(int columns, int rows, int step, char chr){
  const int height = rows - 2 * step;
  const int width = columns - 2 * step - 1;
  if (height <= 0 || width <= 0) return;
  for (int i = 0; i < height; i++){
    putChar(columns - step, rows - i - step, chr);
  }
  for (int i = 0; i < width; i++){
    putChar(columns - i - step - 1, step + 1, chr);
  }
  if (width > 1) {
    for (int i = 0; i < height - 1; i++) {
      putChar(step + 1, step + 2 + i, chr);
    }
  }
  if (height > 1) {
    for (int i = 0; i < width - 1; i++) {
      putChar(step + 2 + i, rows - step, chr);
    }
  }
  spiral(columns, rows, step + 1, chr);
}

void main(int argc, char *argv[]){
  system("clear");
  CONSOLE_SCREEN_BUFFER_INFO csbi;
  int columns, rows;
  GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
  columns = csbi.dwSize.X;
  rows = csbi.dwSize.Y;
  spiral(columns, rows, 0, CHR);
  getchar();
  system("clear");
}
