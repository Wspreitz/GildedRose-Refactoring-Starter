# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros" and item.name != "Conjured Mana Cake":
                if item.quality > 0:
                    item.quality = item.quality - 1
            if item.name == "Conjured Mana Cake":
                item.quality = item.quality - 2
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11 and item.sell_in > 5:
                        item.quality += 1
                    if item.sell_in < 6 and item.sell_in > 0:
                        item.quality += 2
                    if item.sell_in < 1:
                            item.quality = 0
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.sell_in = item.sell_in - 1
 


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)