
equal_parts=[]
def average(half):
    total = 0
    for value in half:
        total+=value
    return total/len(half)

X= [1,2,3,4,5,6,7,8]

list_1= [1,2,3,4]
list_2=[5,6,7,8]
v= [[1,2,3,4],[5,6,7,8]]
ok_list = []
print(len(X)/2)


is_Capaple = False
if len(X)%2==0:
    for i in range(0,int((len(X)/2))):
        for y in range(0,int((len(X)/2))):
            list_1 = [1,2,3,4]
            list_2=[5,6,7,8]
            middle_hv = list_1[i]
            list_1[i]=list_2[y]
            list_2[y]=middle_hv
            if average(list_1) == average(list_2):
                ok_list.append(list_1)
                ok_list.append(list_2)

            
print(list_1)
print("It is "+str(is_Capaple)+" that half sublists has equal average values. The lists are:"+str(ok_list))
