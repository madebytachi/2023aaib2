#include <string.h>
#include <stdio.h>
int main()
{
    char line[20];
    scanf("%s", line);
    int N = strlen(line);
    int bad = 0;
    for(int i=0; i<N/2; i++){
        if( line[i] != line[N-1-i] ) bad = 1;
    }///�Y�e��������r�����P,�N����
    ///0123456789 �@10�ӼƦr
    ///^        ^ �ۥ[�O9
    /// 1      8 �ۥ[�O9
    ///  2    7 �ۥ[�O9
    ///   3  6 �ۥ[�O9
    ///    45 �ۥ[�O9
    ///    45 �ۥ[�O9
    ///   3  6 �ۥ[�O9
    ///  2    7 �ۥ[�O9
    /// 1      8 �ۥ[�O9
    ///0        9 �ۥ[�O9
    if(bad==1) printf("NO\n");
    else printf("YES\n");
}
