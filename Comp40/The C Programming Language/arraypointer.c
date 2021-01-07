//
//  arraypointer.c
//  
//
//  Created by Erli Cai on 30/12/2020.
//

#include <stdio.h>

int main(){
    
    int array[] = {1,2,3,4,5,6,7,8};
    int *pa = &array;
    
    pa++;
    printf("%d\n", *pa);
    printf("%d\n", *(array + 2));
    printf("%d\n", pa[3]);
}
