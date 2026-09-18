class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="[" or i=="(" or i=="{":
                st.append(i)
            else:
                if not st:
                    return False
                else:
                    if i==")" and st[-1]=="(":
                        st.pop()
                    elif i=="]" and st[-1]=="[":
                        st.pop() 
                    elif i=="}" and st[-1]=="{":
                        st.pop()
                    else:
                        return False    
        if not st:
            return True
        else:
            return False                                  
        