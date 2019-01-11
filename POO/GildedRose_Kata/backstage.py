from normal_Item import NormalItem

class Backstage(NormalItem):

    def update_quality(self):
        if self.getSellIn() > 10:
            self.quality += 1
        
        elif self.getSellIn() <= 5:
            self.quality += 3

        elif 5 <= self.getSellIn() <= 10:
            self.quality += 2

        else:
            self.quality = 0


if __name__ == "__main__":
    

    # TEST CASES #

    Edu = Backstage("Edu", 5, 20)
    Edu.update_quality()

    assert Edu.getQuality() == 23
    assert Edu.getSellIn() == 5