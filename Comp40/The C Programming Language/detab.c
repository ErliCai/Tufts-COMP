//
//  detab.c
//  
//
//  Created by Erli Cai on 26/12/2020.
//

#include <stdio.h>

#define F  0;
#define T  1;

int main(){
    int c;
    int i = F;
    
    while ((c = getchar()) != EOF){
        if (c == '\t'){
            i = T;
        }
        else{
            if (i){
                i = F;
                putchar(' ');
            }
            putchar(c);
        }
    }
    
    return 0;
}
