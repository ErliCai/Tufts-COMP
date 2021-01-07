//
//  arraytest.c
//  
//
//  Created by Erli Cai on 25/12/2020.
//

#include <stdio.h>

int main(){
    
    int digits[10];
    
    for (int i=0; i<10; i++){
        digits[i] = i;
    }
    
    for (int i=0; i<10; i++){
        printf("%d", digits[i]);
    }
}
