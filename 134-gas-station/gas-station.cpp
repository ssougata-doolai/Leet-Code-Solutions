class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        /* Brute force */
        // int i, j, n = gas.size(), k, total_gas, idx;
        // bool flag;
        // for(i = 0; i < n; i++) {
        //     flag = true;
        //     total_gas = 0;
        //     for(j = 0; j < n; j++) {
        //         idx = (i + j) % n;
        //         total_gas += gas[idx] - cost[idx];
        //         if(total_gas < 0) {
        //             flag = false;
        //             break;
        //         }
        //     }
        //     if(flag) return i;
        // }

        // return -1;

        int start = gas.size()-1, end = 0;

        int total_gas = gas[start] - cost[start];
        while(start > end) {
            if(total_gas < 0) {
                start--;
                total_gas += gas[start] - cost[start];
            }
            else {
                total_gas += gas[end] - cost[end];
                end++;
            }
        }

        if(total_gas < 0) return -1;
        else return start;

    }
};