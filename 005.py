import json
class Cart:
    items = []
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

    def totalPrice(self):
        total = 0
        items = self.items
        for item in items:
            qty = item['quantity']
            price = item['price']
            totalprice = price * qty / 2
            total += totalprice
        print("Total price ",total)

    def checkout(self):
        myObj = self.items
        toJson = json.dumps(myObj, indent=4)
        fwrite = open("cart.json", 'w')
        fwrite.write(toJson)
    



cart = Cart()
cart.addItem('{ "item_id": 1, "price": 30000, "quantity": 3 }').addItem('{ "item_id": 2, "price": 30000, "quantity": 3 }').removeItems('{ "item_id": 1, "price": 30000, "quantity": 3 }').addItem('{ "item_id": 3, "price": 30000, "quantity": 3 }')
cart.showAll()
cart.totalItems()
cart.totalQuantity()
cart.totalPrice()
cart.checkout()