class Calculator:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def calculate(self):
        if self.op == "add":
            return self.a + self.b
        elif self.op == "sub":
            return self.a - self.b
        elif self.op == "mul":
            return self.a * self.b
        elif self.op == "div":
            return self.a / self.b
        else:
            return "Invalid operation"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add/sub/mul/div): ")

c = Calculator(a, b, op)
print("Result:", c.calculate())
