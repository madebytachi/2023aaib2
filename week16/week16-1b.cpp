///week16-1b.cpp
#include <stdio.h>
void myPrint(int a[10]){
    for(int i=0; i<10; i++) printf("%d ", a[i] );
    printf("\n");
}
int main()
{
    int a[10] = {9,8,7,6,5,4,3,2,1,0}; ///10计,9丁筳
    myPrint(a);

    for(int i=0; i<9; i++){ ///眖オǖ近,9丁筳
        if(a[i]>a[i+1]){ ///綟ゑ,ぃ癸
            int temp = a[i]; ///碞ユ传
            a[i] = a[i+1];
            a[i+1] = temp;
        }
    }
    myPrint(a);
for(int i=0; i<9; i++){ ///眖オǖ近,9丁筳
        if(a[i]>a[i+1]){ ///綟ゑ,ぃ癸
            int temp = a[i]; ///碞ユ传
            a[i] = a[i+1];
            a[i+1] = temp;
        }
    }
    myPrint(a);

    for(int i=0; i<9; i++){ ///眖オǖ近,9丁筳
        if(a[i]>a[i+1]){ ///綟ゑ,ぃ癸
            int temp = a[i]; ///碞ユ传
            a[i] = a[i+1];
            a[i+1] = temp;
        }
    }
    myPrint(a);
}
