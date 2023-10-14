lass Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        int sizeA = getSize(headA); 
        int sizeB = getSize(headB);

        if(sizeA > sizeB){
            while(sizeA > sizeB){
                headA = headA->next;
                sizeA--;
            }
        }else{
             while(sizeB > sizeA){
                headB = headB->next;
                sizeB--;
            }
        }
        
        while(headA != headB){
            headA = headA->next;
            headB = headB->next;
        }

        return headA;
    }

    int getSize( ListNode *head){

        int size = 1; 

        while( head != nullptr ){
            head = head->next;
            size++;
        }
            
            return size;
    }
};
