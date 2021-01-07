//
//  echo.c
//  
//
//  Created by Erli Cai on 31/12/2020.
//

#include <stdio.h>


int main(int argc, char *argv[]){
    int i;
    
    for (i=1;i<argc;i++)
        printf("%s%s", argv[i], (i<argc-1) ? " ": "");
    printf("\n");
    return 0;
}
