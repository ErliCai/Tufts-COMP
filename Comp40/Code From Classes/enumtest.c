//
//  enumtest.c
//  
//
//  Created by Erli Cai on 08/01/2021.
//

#include <stdio.h>

int main(){
    
    enum code_quality {good=2, medicore=1, ugly} my_program;
    
    my_program = ugly;
    
    printf("%d\n", my_program);
}
