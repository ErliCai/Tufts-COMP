//
//  buffer.c
//  
//
//  Created by Erli Cai on 29/12/2020.
//

#include <stdio.h>

#define BUFSIZE 100

char buf[BUFSIZE];
int bufp = 0;

int getch(void){
    return (bufp>0) ? buf[--bufp] : getchar();
}

void ungetch(int c){
    if (bufp >= BUFSIZE)
        printf("Error: to many characters");
    else
        buf[bufp++] = c;
}
