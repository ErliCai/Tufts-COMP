//
//  setbits.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>


int setbits(int x, int p, int n, int y){
    int z;
    printf("%d\n", z);
    z = (x >> p);
    printf("%d\n", z);
    z <<= n;
    printf("%d\n", z);
    z |= (y & ~(~0 << n));
    printf("%d\n", z);
    z <<= p-n;
    printf("%d\n", z);
    z |= (x & ~(~0 << (p-n)));
    printf("%d\n", z);
    
    return z;
}

int main(){
//    int x = 7;
//    printf("%d\n", x>>1);
//    printf("%d\n", x);
    
    int a = setbits(7,1,1,7);
}
