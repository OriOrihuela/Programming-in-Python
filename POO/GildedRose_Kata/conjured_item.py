from normal_Item import NormalItem

class ConjuredItem(NormalItem):

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_In()


if __name__ == "__main__":
    

    # TEST CASES #

    new_item = ConjuredItem("Edu", 5, 25)
    new_item.update_quality()

    assert new_item.getQuality() == 23
    assert new_item.getSellIn() == 4
    assert new_item.getName() == "Edu"