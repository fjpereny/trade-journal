class Stock(object):
    """
    docstring
    """
    
    def __init__(self):
        self.symbol = ''
        self.market_type = ''
        self.long_position = None
        self.open_price = 0
        self.shares = 0
        self.open_date = 0


    def __str__(self):
        text = str(self.symbol) + '\n'
        if self.long_position:
            text += 'Position Type: Long\n'
        elif self.long_position == False:
            text += 'Position Type: Short\n'
        else: 
            text += 'Position Type: None\n'  
        text += 'Open Price: ' + str(self.open_price) + '\n'
        text += 'Shares: ' + str(self.shares) + '\n'
        return text


    def open_value(self):
        return self.open_price * self.shares


    def market_value(self, market_price):
        return market_price * self.shares


    def gain_loss(self, market_price):
        if self.long_position == True:
            return (market_price - self.open_price) * self.shares  
        elif self.long_position == False:
            return (self.open_price - market_price) * self.shares
        else:
            return None

t = Stock()
t.symbol = "TSLA"
