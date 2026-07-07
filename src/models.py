
class Item:
    def __init__(self, item_id, name, high_price, low_price):
        self.item_id = item_id
        self.name = name
        self.high_price = high_price
        self.low_price = low_price
    
    @property
    def formatted_high(self):
        if self.high_price == 0:
            return "No recent trades"
        return f"{self.high_price:,} gp"
    @property
    def formatted_low(self):
        if self.low_price == 0:
            return "No recent trades"
        return f"{self.low_price:,} gp"
    
    def formatted_info(self):
        return f"Item: {self.name} (ID: {self.item_id})\nHigh Price: {self.formatted_high}\nLow Price: {self.formatted_low}"
    
    def __repr__(self):
        return f"Item({self.item_id}, {self.name}, {self.high_price}, {self.low_price})"