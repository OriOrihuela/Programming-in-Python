from item import Item
from interface import Interface

class NormalItem(Item, Interface):

    '''def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)'''
    
    def setSell_In(self):
        self.sell_in -=  1


    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality = self.quality + value
        else:
            self.quality = 0
        

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_In()


if __name__ == "__main__":
    
    # TEST CASES # 

    new_item = NormalItem("Edu", 5, 50)
    assert new_item.setSell_In() == 4
    assert new_item.setQuality(0) == ("Edu", 4, 49)