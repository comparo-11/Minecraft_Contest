#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include<time.h>
#include "control.h"

int main(int argc, char *argv){
    int ibuf;
    long cbuf, zbuf;
    /*
    int flag=0;
    init();
    setTime();
    exePython();
    setSurvival();*/
    init();
    exePython();

    while(rk){
        // detectMobsAbout(1, ibuf);
        cbuf = detectMobsSimple(1);
        zbuf = detectMobsSimple(2);

        // printf("完了\n");
        // printf("%d\n", strlen(han));
        // printf("%c\n\n", han[0]);
        
        // for(int i=0; i < strlen(han); i++) {
        //     printf("%c", han[i]);
        // }
        printf("\n");
        printf("\n");
        printf("%d\n", zbuf);
        printf("%d\n", cbuf);
        // for(int i=0; i < sizeof(ibuf)/4; i++) {
        //     printf("%d", ibuf[i] - '0');
        // }
        printf("\n");
        sleep(5);
    }
}
