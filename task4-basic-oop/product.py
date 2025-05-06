"""
definition of the product class for managing inventory in invetory system

 """

class Product:
    """
    a class for representing aproduct in investory 
    Attributes:
    name : str
        the product name .
    price : float
       the price per unit product which must not  include a negative 
       the avalaible quantity in the stock  .
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product object with name, price, and quantity.

        Raises:
        ------
        ValueError:
            If price or quantity is negative.
        """
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self) -> str:
        """Returns the name of the product."""
        return self._name

    @property
    def price(self) -> float:
        """gets the price of the product."""
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price must not be negative.")
        self._price = value

    @property
    def quantity(self) -> int:
        """Gets the quantity in stock."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value

    def add_inventory(self, amount: int):
        """
        addition of the invetory quantity.

        Parameters:
        amount : int
         Amount to add (must be positive).

        Raises:
        ValueError:
            If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount to add must be positive.")
        self.quantity += amount

    def remove_inventory(self, amount: int):
        """
        Removes from the inventory quantity.

        Parameters:
        amount : int
            Amount to remove (must be positive and not exceed current quantity).

        Raises:
        ValueError:
            If amount is invalid or exceeds available quantity.
        """
        if amount <= 0:
            raise ValueError("Amount to remove must be positive.")
        if amount > self.quantity:
            raise ValueError("Not enough inventory to remove that amount.")
        self.quantity -= amount

    def total_value(self) -> float:
        """
        Calculates total value of product in stock.
        Returns:
        float
            Total value (price × quantity).
        """
        return self.price * self.quantity

    def display_info(self) -> str:
        """
        Returns a formatted string of product details.
        Returns:
    
        str
            Product summary.
        """
        return (
            f"Product: {self.name}, "
            f"Price: ${self.price:.2f}, "
            f"Quantity: {self.quantity}, "
            f"Total Value: ${self.total_value():.2f}"
        )
