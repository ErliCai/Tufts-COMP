//
//  macrosubstitution.c
//  
//
//  Created by Erli Cai on 30/12/2020.
//

#include <stdio.h>

#define swap(t,a,b) {t c=a; a=b; b=c;}
#define printd(n) printf(#n " = %d \n", n)

int main(){
    int i, j;
    i = 1;
    j = 2;
    swap(int, i, j);
    
    printf("%d\n", i);
    printd(i);
}
