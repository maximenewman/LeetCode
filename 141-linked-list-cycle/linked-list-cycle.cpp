/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == nullptr || head->next == nullptr)
            return false;

        struct ListNode * current = head;
        struct ListNode * fast = head;
        while(fast != nullptr && fast->next != nullptr){
            current = current -> next;
            fast = fast ->next->next;
            if(current == fast)
                return true;
        }
        return false;
    }
};