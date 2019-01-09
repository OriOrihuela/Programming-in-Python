from normal_Item import NormalItem

class AgedBrie(NormalItem):

    def update_quality(self):

        if self.getSellIn() >= 0:
            self.quality += 1
        
        else:
            self.quality += 2

if __name__ == '__main__':

    # TEST CASES #

    Edu = AgedBrie("Edu", 5, 20)
    Edu.update_quality()

    assert Edu.getQuality() == 21
    assert Edu.getSellIn() == 5

    