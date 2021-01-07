//
//  switchtest.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>


int main(){
    int c = 1;
    
    switch (c) {
        case 1:
            printf("1");
        case 2:
            printf("2");
            break;
        default:
            printf("3");
            break;
    }
    return 0;
}
