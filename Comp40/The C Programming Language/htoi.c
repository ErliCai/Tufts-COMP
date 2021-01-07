//
//  htoi.c
//  
//
//  Created by Erli Cai on 28/12/2020.
//

#include <stdio.h>

int htoi(char c[]){
    int answer = 0;
    
    char allowable[] = "aAbBcCdDeEfF";
    for(int i=0; c[i]!='\0'; i++){
        answer *= 16;
        for(int j=0; j<12; j++){
            if (c[i] == allowable[j]){
                answer += (10 + j/2);
            }
        }
        if (c[i] >'0' && c[i]<'9'){
            answer += c[i] - '0';
        }
    }
    return answer;
}

int main(){
    int a = htoi("0xaA");
    printf("%d\n", a);
    
    return 0;
}
