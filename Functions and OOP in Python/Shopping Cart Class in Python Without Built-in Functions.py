class ShoppingCart:
    def __init__(self, item_value):
        self.item_list=[item_value]
    def add_item(self,item_value):
        self.item_list.insert(len(self.item_list),item_value)
    def remove_item(self,item_value):
        i=0
        for item in self.item_list:
            if (item==item_value):
                self.item_list.pop(i)
            i=i+1
    def check_out(self):
        for item in self.item_list:
            print(item)
            
x=ShoppingCart('kurta')
x.add_item('shirt')
x.add_item('tie')
x.remove_item('shirt')
x.add_item('belt')
x.check_out()