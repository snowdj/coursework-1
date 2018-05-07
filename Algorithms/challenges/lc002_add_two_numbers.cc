#include <stddef.h>

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      int carry = 0;
      ListNode head(0), *s = &head;
      while (l1||l2||carry) 
        {
          int t = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
          s->next = new ListNode(t % 10);
          carry = t / 10;
          s = s->next;
          l1 = l1 ? l1->next : l1;
          l2 = l2 ? l2->next : l2;
        }
      return head.next;
    }
};
