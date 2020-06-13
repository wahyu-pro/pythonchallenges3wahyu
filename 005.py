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
                # idItem = item['item_id']
                del x['item_id']
                return self
    def showAll(self):
        print(self.items)



cart = Cart()
cart.addItem('{ "item_id": 1, "price": 30000, "quantity": 3 }').addItem('{ "item_id": 2, "price": 30000, "quantity": 3 }').removeItems('{ "item_id": 1, "price": 30000, "quantity": 3 }').showAll()
