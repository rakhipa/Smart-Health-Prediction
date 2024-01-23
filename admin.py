#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int processID;
    int timeLeft;
    struct Node *next;
} Node;

Node *createNode(int processID, int timeLeft) {
    Node newNode = (Node) malloc(sizeof(Node));
    newNode->processID = processID;
    newNode->timeLeft = timeLeft;
    newNode->next = NULL;
    return newNode;
}

Node *addToEnd(Node *head, Node *newNode) {
    if (head == NULL) {
        head = newNode;
        head->next = head;
    } else {
        Node *current = head;
        while (current->next != head) {
            current = current->next;
        }
        current->next = newNode;
        newNode->next = head;
    }
    return head;
}

Node *deleteNode(Node *head, int processID) {
    Node *current = head;
    Node *prev = NULL;

    if (head == NULL) {
        printf("Process with ID %d not found.\n", processID);
        return NULL;
    }

    do {
        if (current->processID == processID) {
            if (prev == NULL) {
                if (current->next == head) {
                    head = NULL;
                } else {
                    head = current->next;
                    Node *last = head;
                    while (last->next != current) {
                        last = last->next;
                    }
                    last->next = head;
                }
            } else {
                prev->next = current->next;
            }
            printf("Process with ID %d completed.\n", processID);
            free(current);
            break;
        }
        prev = current;
        current = current->next;
    } while (current != head);

    if (current == head && current->processID != processID) {
        printf("Process with ID %d not found.\n", processID);
    }

    return head;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    Node *head = NULL;

    // Adding processes to circular linked list
    for (int i = 1; i <= n; i++) {
        int timeLeft;
        printf("Enter the time left for process %d: ", i);
        scanf("%d", &timeLeft);
        head = addToEnd(head, createNode(i, timeLeft));
    }

    // Running processes in a circular queue
    Node *current = head;
    while (current != NULL) {
        printf("Running process %d...\n", current->processID);
        current->timeLeft--;
        if (current->timeLeft == 0) {
            head = deleteNode(head, current->processID);
            current = head;
        } else {
            current = current->next;
        }
    }

    printf("All processes completed.\n");

    return 0;
}
