//
//  squeeze.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>


void squeeze(char c1[], char c2[]){
    int same,i,k;
    
    for(i=k=0; c1[i]!='\0'; i++){
        same = 0;
        for(int j=0; c2[j]!='\0'; j++){
            if (c1[i] == c2[j]){
                same = 1;
            }
        }
        if (!same) {
            c1[k++] = c1[i];
        }
    }
    c1[k] = '\0';
}

int main(){
    
    char s1[] = "abcdefghijkmn";
    char s2[] = "fuck";
    
    squeeze(s1, s2);
    
    printf("%s\n", s1);
    
    return 0;
}
