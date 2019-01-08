class Item():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def getName(self):
        return self.name
    def getSellIn(self):
        return self.sell_in
    def getQuality(self):
        return self.quality

    def __repr__(self):
        return "%s, %s, %s" % (self.getName(), self.getSellIn(), self.getQuality)

if __name__ == "__main__":
    

    # TEST CASES #

    new_item = Item("Edu", 10, 100)
    assert new_item.getName() == "Edu"
    assert new_item.getSellIn() == 10
    assert new_item.getQuality() == 100