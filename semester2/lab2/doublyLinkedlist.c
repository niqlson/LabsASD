#include <stdio.h>
#include <stdlib.h>

struct Node {
  double data;
  struct Node* prev;
  struct Node* next;
};

struct Node* createNode(double data) {
  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

  newNode->data = data;
  newNode->prev = NULL;
  newNode->next = NULL;

  return newNode;
}

void addElements(struct Node** headRef, double data) {
  struct Node* newNode = createNode(data);

  if (*headRef == NULL) {
    *headRef = newNode;
  } else {
    struct Node* current = *headRef;
    while (current->next != NULL) {
      current = current->next;
    }
    current->next = newNode;
    newNode->prev = current;
  }
}

void extendInReverse(struct Node** headRef) {
  struct Node* last = *headRef;

  while (last->next != NULL) {
    last = last->next;
  }

  struct Node* current = last;

  while (current != NULL) {
    addElements(headRef, current->data);
    current = current->prev;
  }
}

void printList(struct Node* head) {
  struct Node* current = head;

  while (current != NULL) {
    printf("%.2f ", current->data);
    current = current->next;
  }
  printf("\n");
}

void freeList(struct Node** headRef) {
  struct Node* current = *headRef;
  struct Node* next;

  while (current != NULL) {
    next = current->next;
    free(current);
    current = next;
  }
  *headRef = NULL;
}

int main() {
  int i, n;
  double data;
  printf("Enter the number of elements: ");
  scanf("%d", &n);

  struct Node* head = NULL;

  for (i = 0; i < n; ++i) {
    printf("Enter element %d: ", i + 1);
    scanf("%lf", &data);
    addElements(&head, data);
  }

  extendInReverse(&head);

  printf("Result: ");
  printList(head);

  freeList(&head);

  return 0;
}
