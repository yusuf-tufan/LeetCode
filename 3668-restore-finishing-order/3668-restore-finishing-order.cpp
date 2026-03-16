class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        vector<int>resultList;

        for (int i = 0;i<order.size();i++) {

            if (find(friends.begin(), friends.end(), order[i]) != friends.end()) {
                resultList.push_back(order[i]);
            }
        }
        return resultList;
    }
};