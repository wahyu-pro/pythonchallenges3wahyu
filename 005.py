import json
class Cart:
    items = []
    diskon = 0
    def addItem(self, arg):
        string = str(arg)
        item = json.loads(string)
        self.items.append(item)
        return  self

    def removeItems(self, arg):
        string = str(arg)
        item = json.loads(string)
        for x in self.items:
            if (item['item_id'] == x['item_id']):
                idItem = item['item_id'] - 1
                del self.items[idItem]
                return self
    def showAll(self):
        print(self.items)

    def totalItems(self):
        myList = self.items
        print("Total Items ",len(myList))

    def totalQuantity(self):
        total = 0
        items = self.items
        for item in items:
            qty = item['quantity']
            total += qty
        print("Total quantity ",total)

    def addDiskon(self, arg):
        disk = arg
        if disk == "50%":
            self.diskon += 2
        return self

    def totalPrice(self):
        total = 0
        items = self.items
        for item in items:
            qty = item['quantity']
            price = item['price']
            totalprice = price * qty / self.diskon
            total += totalprice
        print("Total price ",int(total))

    def checkout(self):
        myObj = self.items
        toJson = json.dumps(myObj, indent=4)
        fwrite = open("cart.json", 'w')
        fwrite.write(toJson)
        self.items.clear() # hapus semua data ketika semua sudah di checkout
    



cart = Cart()
cart.addItem('{"item_id": 1, "price": 30000, "quantity": 3 }').addItem('{"item_id": 2, "price": 10000, "quantity": 1 }').addItem('{"item_id": 3, "price": 5000, "quantity": 2 }').removeItems('{"item_id": 2}').addItem('{"item_id": 4, "price": 400, "quantity": 6 }').addDiskon("50%")
cart.showAll()
cart.totalItems()
cart.totalQuantity()
cart.totalPrice()
cart.checkout()
