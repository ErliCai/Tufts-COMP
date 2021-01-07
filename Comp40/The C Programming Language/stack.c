//
//  stack.c
//  
//
//  Created by Erli Cai on 29/12/2020.
//

#include <stdio.h>
#define MAXVAL 100

int sp = 0;
double val[MAXVAL];

void push(double f){
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf("error: stack is full\n");
}

double pop(void){
    if (sp>0){
        return val[--sp];
    }
    else{
        printf("error: stack is empty\n");
        return 0.0;
    }
}
