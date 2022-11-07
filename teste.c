#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    printf("Até qual numero deseja calcular:\n");
    scanf("%d", &n);

    double raiz = sqrt(n);

    printf("%f", raiz);
    return 0;
}