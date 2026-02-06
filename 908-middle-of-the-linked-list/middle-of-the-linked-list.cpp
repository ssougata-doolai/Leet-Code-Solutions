/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if(head == nullptr || head->next == nullptr) return head;

        ListNode *temp = new ListNode(0, head);
        ListNode *fast = temp, *slow = temp;
        while(fast != nullptr) {
            cout << slow->val << endl;
            if(fast->next == nullptr) return slow->next;
            slow = slow->next;
            fast = fast->next->next;
        } 

        return slow;
    }
};