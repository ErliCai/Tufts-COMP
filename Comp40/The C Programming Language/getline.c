//
//  getline.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>

int getlines(char s[], int limit){
    int c,i=0;
    while ((c = getchar()) != '\n' && c != EOF && i<limit){
        s[i++] = c;
    }
    if (c=='\n'){
        s[i++] = c;
    }
    s[i] = '\0';
    
    return i;
}
