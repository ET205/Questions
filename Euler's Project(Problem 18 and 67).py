class Tree:
    def __init__(self):
            self.left=None
            self.right=None
            self.data=None

f = open('1.txt', 'r')
line=[]
no_of_lists=0
while True:
    line.append(f.readline().replace("\n",""))
    if line[no_of_lists]=="":
        f.closed
        line.pop()
        break
    no_of_lists+=1

no_of_lists-=1
elements=[]
parent=0
child=0
no_of_elements=0
while no_of_lists>0:
    elements=line[no_of_lists-1].split(" ")
    no_of_elements=len(elements)
    while no_of_elements>0:
        root=Tree
        root.data=elements[parent]
        root.left=line[no_of_lists].split(" ")[child]
        root.right=line[no_of_lists].split(" ")[child+1]
        elements[parent]=str(int(elements[parent])+max(int(root.left),int(root.right)))
        child+=1
        parent+=1
        no_of_elements-=1
    line[no_of_lists-1]=' '.join(elements)
    parent=0
    child=0
    no_of_lists-=1
    
print(elements[parent])
