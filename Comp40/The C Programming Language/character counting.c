//
//  character counting.c
//  
//
//  Created by Erli Cai on 25/12/2020.
//

#include <stdio.h>

int main(){
    int cc, c;
    
    cc = 0;
    while ((c = getchar()) != EOF){
        ++cc;
    }
    
    printf("%d\n", cc);
    
}
