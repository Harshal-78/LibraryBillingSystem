print(" Welcome ")
print("--------------------------------")

Books={
    "Math":120,
    "Science":310,
    "Physics":160,
    "English":90,
    
}
cart={}
for book,price in Books.items():
 print(f"{book.capitalize():9}: {price}")
print("Exit(0)")
while True:
    item=input("Enter your book name: ").capitalize()
    if item == "0":
        break
    if item in Books:
        qt = int(input("Enter quantity of book: "))
        if item in cart:
            cart[item]["qty"]+=qt
        else:
            cart[item]={
                "price":Books[item],
                "qty":qt
            }
    else:
        print("Book not available")
total=0
print("------Bill-----")
file=open("bill.data","w")
file.write("----BILL----\n")
for book , data in cart.items():
    total_item = data["price"] * data["qty"]
    total+=total_item
    line = f"{book} X {data['qty']} : {total_item}\n"
    print(line.strip())
    file.write(line)

file.write("------------------\n")
file.write(f"Total bill is : {total}\n")

file.close()
print("-----------------")
print(f"Total bill is : {total}")

 
    
        