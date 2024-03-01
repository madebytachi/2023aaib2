//今天的LeetCode挑戰題,二進位的數字的字串,裡面有一堆0和1
//享用這些0和1湊出最大的基數(最右邊有1個1)
//解法: 先數有幾個1,把1個放右邊,其他都放左邊,中間塞一堆0
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int N = s.length(); //C++的字串的長度
        int one = 0; //s裡面,有幾個1呢?等一下會慢慢變數出來
        for(int i=0; i<N; i++){ // C/C++迴圈(有圓括號)
            if(s[i]=='1') one += 1; // if(判斷) 也有圓括號
        }
        //printf("N:%d one:%d ", N, one);//先印出來,有幾個1
        string ans; //用來放答案
        for(int i=0; i<one-1; i++) ans += '1'; //有幾個1要放前面?
        for(int i=0; i<N-one; i++) ans += '0'; //有幾個1要放前面?
        ans += '1'; //最後塞個1
        return ans;
    }
};