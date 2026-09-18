class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st=[]
        for i in operations:
            if i!="D" and i!="C" and i!="+":
                st.append(int(i))
            elif i=="D":
                element=st[-1]*2
                st.append(element)
            elif i=="C":
                st.pop()
            elif i=="+":
                e1=st[-1]
                e2=st[-2]
                sm=e1+e2
                st.append(sm)
        return sum(st)                        

        