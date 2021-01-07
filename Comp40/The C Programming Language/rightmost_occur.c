//
//  rightmost_occur.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>

#define Max_length 1000

int getlines(char s[], int limit);
int strindex(char s[], char t[]);

char line[Max_length];
char pattern[] = "ould";

int main(){
    while (getlines(line,Max_length)){
        if (strindex(line, pattern) != -1){
            printf("%s",line);
        }
    }
}

//int strindex(char s[], char t[]){
//    int i,j,k;
//    for (i=0; s[i]!='\0' ;i++){
//        for (j=0,k=i; t[j]!='\0'; j++){
//            if (t[j] != s[k++]){
//                break;}
//        }
//        if (t[j] == '\0')
//            return i;
//    }
//    return -1;
//}
//
//int getlines(char s[], int limit){
//    int c,i=0;
//    while ((c = getchar()) != '\n' && c != EOF && i<limit){
//        s[i++] = c;
//    }
//    if (c=='\n'){
//        s[i++] = c;
//    }
//    s[i] = '\0';
//
//    return i;
//}
