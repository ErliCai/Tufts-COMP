//
//  Getchar.c
//  
//
//  Created by Erli Cai on 25/12/2020.
//

#include <stdio.h>

int main(){
    
    int c;
    
    c = getchar();
    while (c != EOF){
        putchar(c);
        c = getchar();
    }
}
