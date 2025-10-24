#git add . ; git commit -m "Graph" ; git push -u origin main


class Solution:
    def findCenter(self, edges):
        edge1 = edges[0]
        edge2 = edges[1]

        if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
            return edge1[0]
        else:
            return edge1[1]
    

if __name__ =="__main__":
    n=3
    edges=[[1,2],[2,3],[4,2]]
    sol=Solution()
    print(sol.findCenter(edges))
