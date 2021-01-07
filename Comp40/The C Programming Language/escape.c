//
//  escape.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>

void escape(char s[], char t[]){
    int i,j;
    for(i=j=0; t[i]!='\0'; i++){
        switch (t[i]) {
            case '\t':
                s[j++] = '\\';
                s[j++] = 't';
                break;
            case '\n':
                s[j++] = '\\';
                s[j++] = 'n';
                break;
            default:
                s[j++] = t[i];
                break;
        }
    }
    s[j] ='\0';
}

int main(){
    char c[] = "Woshi \t 123 \n";
    char d[100];
    escape(d,c);
    
    printf("%s\n%s\n", c,d);
}
