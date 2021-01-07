//
//  entab.c
//  
//
//  Created by Erli Cai on 26/12/2020.
//

#include <stdio.h>

int main(){
    int c, ntab;
    int nspace = 0;
    
    while ((c = getchar()) != EOF){
        if (c == ' ')
            nspace++;
        else{
            ntab = nspace/4
            for (int i=0; i<ntab; i++)
                putchar('\t');
            for (int i=0; i<nspace-4*ntab; i++)
                ptuchar(' ');
            nspace = 0;
        }
    }
}
