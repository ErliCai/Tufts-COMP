//
//  pointertest.c
//  
//
//  Created by Erli Cai on 03/01/2021.
//

#include <stdio.h>

int main(){
    int x,y,z;
    int *ip;
    
    x = 2;
    y = 3;
    ip = &z;
    
    *ip = x + y;
    printf("%d\n",z);
    
    *ip = *ip + z;
    printf("%d\n",z);
    
    return 0;
}
