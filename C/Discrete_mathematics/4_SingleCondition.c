#include "stdio.h"
int main(int argc, char const *argv[])
{
    int z, p, q;
    p = 2;
    q = 2;
    printf("验证逻辑联结词‘单条件 ");
    printf("\n");
    printf("z = p --> q");  /*单条件*/
    printf("\n");

    while((p!=0 && p!=1) || (q!=0 && q!=1)){
        printf("please input p(0 or 1):p= ");
        scanf("%d", &p);
        printf("please input q(0 or 1):q= ");
        scanf("%d", &q);
    }
    
    if (p == 0 || q == 1) {
        z = 1;
    }
    else
    {
        z = 0;
    }
    printf("z = %d\n",z);
    
    return 0;
}
