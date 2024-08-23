#LIFO(q)

# q=[]
# size=int(input("enter max size: "))
# front = 0 #out
# rear = 0 #insert
# def enqueve(): #insert_opration
#     global size,front,rear
#     if rear>=size: #if rare value is more than size
#         print("que is full insertion not possible")
#     else:
#         item=input("enter element: ")
#         rear+=1 #(rear=rear+1)
#         q.insert(rear,item)
#         print(q)
# def dequue(): #delete_opration
#     global size,front,rear
#     if front==rear==0:
#         print("que is empty deletion not possible")
#     else:
#         q.pop(front)
#         rear-=1#(rear=rear-1)
#         print(q)
# while True:
#     print("****options****")
#     op=int(input("1,ENQUERY \t \t 2.DEQUEUE \t \t 3.EXIT"))
#     if op==1:
#         enqueve()
#     elif op==2:
#         dequue()
#     elif op==3:
#         break
#     else:
#         print("INVALID OPTION")


#LIFO(stack)

q=[]
size=int(input("enetr a size: "))
top=-1

def enq():
    global size,top
    if top>=size:
        print("que is full,insert is not possible")
    else:
        item=input("enter your element:")
        top+=1
        q.insert(top,item)
        print(q)
        print(top)

def deq():
    global size,top
    if top==0:
        print("que is empty deletion is ist possible")
    else:
        q.pop(top)
        top-=1
        print(q)
while True:
    print("*****options****")
    op=int(input("enter a number: 1.ENQ \t \t 2.deq \t \t 3.break"))
    if op==1:
        enq()
    elif op==2:
        deq()
    elif op==3:
        break
    else:
        print("invalid option")


