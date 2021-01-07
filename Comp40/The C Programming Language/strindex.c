//
//  strindex.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>

int strindex(char s[], char t[]){
    int i,j,k;
    for (i=0; s[i]!='\0' ;i++){
        for (j=0,k=i; t[j]!='\0'; j++){
            if (t[j] != s[k++]){
                break;}
        }
        if (t[j] == '\0')
            return i;
    }
    return -1;
}
