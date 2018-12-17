#include "stdio.h"
int main(int argc, char const *argv[])
{
    int z, p, q;
    p = 2;
    q = 2;
    printf("验证逻辑联结词‘双条件’");
    printf("\t");
    printf("z = p < == > q");  /*双条件*/
    printf("\n");
    
    while((p!=1 && p!=0) || (q!=1 && q!=0)){
        printf("please input p(0 or 1):p= ");
        scanf("%d", &p);
        printf("please input q(0 or 1):q= ");
        scanf("%d", &q);
    }
    
    if (p==q) {
        z = 1;
    }
    else
    {
        z = 0;
    }
    printf("z = %d\n",z);
    
    return 0;
}
