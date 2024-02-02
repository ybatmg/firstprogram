from datetime import datetime

class MyCake():
    order_id:str
    cake_name:str
    cake_shape:str
    cake_size:int
    date=datetime.now()

    def toJson(cake):
        return {
            "order_id":cake.order_id,
            "cake_name":cake.cake_name,
            "cake_shape":cake.cake_shape,
            "cake_size":cake.cake_size,
            "date":str(cake.date)
        }
    
    def __init__(self,order_id,cake_name,cake_shape,cake_size=1):
        self.order_id=order_id
        self.cake_name=cake_name
        self.cake_shape=cake_shape
        self.cake_size=cake_size
