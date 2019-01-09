from normal_Item import NormalItem

class Sulfuras(NormalItem):


    def update_quality(self):
        assert self.quality == 80
        self.quality = 80


if __name__ == '__main__':

    item = Sulfuras("Sulfuras, mano de Ragnaros", 3, 80)
    item.update_quality()
    assert item.getQuality() == 80
    