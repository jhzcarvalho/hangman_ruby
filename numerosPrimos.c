#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct node
{
    int valor;
    struct node *link;
};

int raizInteira(int n)
{
    if (n == 0 || n == 1)
        return n;

    int i = 1, result = 1;
    while (result <= n)
    {
        i++;
        result = i * i;
    }
    return (i - 1);
}

void addPrimo(struct node *head, int n)
{
    struct node *pointer, *temp;
    pointer = head;
    temp = (struct node *)malloc(sizeof(struct node));

    temp->valor = n;
    temp->link = NULL;

    while (pointer->link != NULL)
    {
        pointer = pointer->link;
    }

    pointer->link = temp;
};

int ehPrimo(struct node *head, int n)
{
    // Verifica se o inteiro n é ou não primo
    int flag = 0;

    int raiz = raizInteira(n);

    struct node *temp;
    temp = head->link;

    while (temp->link == NULL)
    {
        int resto = n % temp->valor;

        if (resto == 0)
        {
            return 1;
        }
        temp = temp->link;
    }
};

void imprimeLista(struct node *head)
{
    if (head == NULL)
    {
        print("Lista Vazia");
    }
}

int main()
{
    int limite;
    printf("Até qual numero deseja calcular:\n");
    scanf("%d", &limite);

    struct node *listaPrimos = malloc(sizeof(struct node));
    listaPrimos->valor = 2;
    listaPrimos->link = NULL;

    for (int i = 3; i < limite; i += 2)
    {
        printf("Testando o numero %d\n", i);
    };

    // printf("%d\n", raizInteira(4));
    // printf("%d\n", raizInteira(11));

    printf("Lista final de Primos\n");
    while (listaPrimos->link = NULL)
    {
        printf("%d", listaPrimos->valor);

        listaPrimos = listaPrimos->link;
    };

    return 0;
}