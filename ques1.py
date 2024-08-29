def add_item(x):
    shop.append(x)

def remove_item(x) :
    newList = []
    for item in shop:
        if (item != x):
            newList.append(item)
    return newList

def search_item(x) :
    for item in newlist:
        if (item == x):
            return True
    return False
    
def display_list() :
    print(f"\nnew shopping list is :{newlist}")


def bin_search(x):
    l=0
    u=len(lst)
    mid = (u+l)/2

    for i in range(l,u,1):
        if (lst[mid] == x):
            print(f"{x} is found in the list")
        elif (lst[mid] > x):
            l=mid;
        else:
            u=mid
    print(f"{x} not found")
        

shop = ['biscuit' , 'soap', 'shampoo', 'fruits', 'shoes']
print("\ncurrent shopping list is: ")
print(shop)

ad = input("\nenter item to add to cart: ")
add_item(ad)
print(shop)

rem = input("\nenter an item to remove from list: ")
newlist = remove_item(rem)
print(newlist)

s = input("\nenter an item to search in the list: ")
res = search_item(s)
if (res) :
    print(f"{s} is in the list")
else :
    print(f"{s} is not in the list")

display_list()

find = input("enter the element to findy binary search: ")

lst = sorted(newlist)
print(find)
bin_search(find)

print("\n",lst)
