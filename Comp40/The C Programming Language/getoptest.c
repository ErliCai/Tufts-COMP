//
//  getoptest.c
//  
//
//  Created by Erli Cai on 29/12/2020.
//

#include <stdio.h>

int getop(char[]);

int main(){
    int type;
    char s[100];

    while ((type = getop(s)) != EOF){
        printf("%s\n",s);
    }
    
//    char c;
//    while ((c=getchar())!=EOF){
//        putchar(c);
//    }
//
//    return 0;
}
