//
//  arraytest.c
//  
//
//  Created by Erli Cai on 08/01/2021.
//

#include <stdio.h>


int main(){
    
    int idx = 4;
    char *hello = "Hello World";
    
    printf("%c\n", hello[idx]);
    printf("%c\n", idx[hello]);
    printf("%c\n", *(hello + idx * sizeof(char)));
    printf("%c\n", 4[hello]);
}
