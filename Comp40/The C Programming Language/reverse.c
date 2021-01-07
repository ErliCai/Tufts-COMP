//
//  reverse.c
//  
//
//  Created by Erli Cai on 30/12/2020.
//

#include <stdio.h>

void recursive_reverse(char c[]);
void reverse(char c[], int i, int j);
int getlen(char c[]);
void swap(char c[], int i , int j);

int main(){
    char c[] = "1234567";
    recursive_reverse(c);
    printf("%s\n",c);
}

void recursive_reverse(char c[]){
    int left,right;
    left = 0;
    right = getlen(c);
    
    reverse(c,left,right);
}

void reverse(char c[], int i, int j){
    
    if (i<j-1){
        swap(c,i,j);
        reverse(c,i+1,j-1);
    }
}

int getlen(char c[]){
    int length = 0;
    for(;c[length]!='\0';length++)
        ;
    length --;
    return length;
}

void swap(char c[], int i , int j){
    int temp;
    temp = c[i];
    c[i] = c[j];
    c[j] = temp;
}
