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
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr || head->next == nullptr)
            return head;
        struct ListNode * current = head;
        struct ListNode * move = head->next;
        struct ListNode * temp;
        while(move->next != nullptr && current->next != nullptr){
            temp = current;
            current = move;
            move = move->next;
            current->next = temp;
        }
        move->next = current;
        head ->next = nullptr;
        head = move;
        return head;
    }
};