//
//  getop.c
//  
//
//  Created by Erli Cai on 29/12/2020.
//
#include <stdio.h>
#include <ctype.h>

#define NUMBER  '0'
#define SIN  '1'
#define EXP  '2'
#define POW  '3'
#define SWAP  '4'
#define PRINT  '5'
#define DUPLICATE  '6'

int getch(void);
void ungetch(int);

int getop(char s[]){
    
    
    int i,c,c1,c2;
    
    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    
    if (c  == 's'){
        //c1 = getch();
        if ((c1 = getch()) == 'i'){
            if ((c2 = getch()) == 'n')
                return SIN;
        ungetch(c1);
        ungetch(c2);
        }
    }
    if (c  == 'p'){
        //c1 = getch();
        if ((c1 = getch()) == 'o'){
            if ((c2 = getch()) == 'w')
                return POW;
            ungetch(c1);
            ungetch(c2);
        }
    }
    if (c  == 'p'){
        //c1 = getch();
        if ((c1 = getch()) == 'o'){
            if ((c2 = getch()) == 'w')
                return POW;
            ungetch(c1);
            ungetch(c2);
        }
    }
    if (c  == 'e'){
        //c1 = getch();
        if ((c1 = getch()) == 'x'){
            if ((c2 = getch()) == 'p')
                return EXP;
            ungetch(c1);
            ungetch(c2);
        }
    }
    if (!isdigit(c) && c != '.' && c != '-' ){
        return c;
    }
    if (c == '-'){
        if ((c = getch()) == ' ')
            return c;
        ungetch(c);
    }
//    if (c  == 's' || c == 'e' || c == 'p'){
//        c1 = getch();
//        if ((c1 = getch()) == 'i'){
//            if ((c2 = getch()) == 'n')
//                return SIN;
//            ungetch(c1);
//            ungetch(c2);
//        }
//        if ((c = getch()) == ' ')
//            return 's';
//    }
    i = 0;
    if (isdigit(c))
        while (isdigit(s[++i] = c = getch()))
            ;
    if (c == '.')
        while (isdigit(s[++i] = c = getch()))
            ;
    
    s[i] = '\0';
    if (c != EOF)
        ungetch(c);
    return NUMBER;
}
