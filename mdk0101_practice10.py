# Пример реализации паттерна Фабрика
class Product:
    def __init__(self, name):
        self.name = name

    def operate(self):
        pass


class ConcreteProductA(Product):
    def operate(self):
        print(f"Operating {self.name} of type A")


class ConcreteProductB(Product):
    def operate(self):
        print(f"Operating {self.name} of type B")


class Factory:
    def create_product(self, product_type, name):
        if product_type == "A":
            return ConcreteProductA(name)
        elif product_type == "B":
            return ConcreteProductB(name)
        else:
            raise ValueError("Invalid product type")


# Пример реализации паттерна Абстрактная фабрика
class AbstractProductA:
    def operate(self):
        pass


class AbstractProductB:
    def operate(self):
        pass


class ConcreteProductAX(AbstractProductA):
    def operate(self):
        print("Operating ProductAX")


class ConcreteProductAY(AbstractProductA):
    def operate(self):
        print("Operating ProductAY")


class ConcreteProductBX(AbstractProductB):
    def operate(self):
        print("Operating ProductBX")


class ConcreteProductBY(AbstractProductB):
    def operate(self):
        print("Operating ProductBY")


class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactoryX(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductAX()

    def create_product_b(self):
        return ConcreteProductBX()


class ConcreteFactoryY(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductAY()

    def create_product_b(self):
        return ConcreteProductBY()


# Пример реализации паттерна Строитель
class ProductBuilder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass


class ConcreteProductBuilder(ProductBuilder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA")

    def build_part_b(self):
        self.product.add_part("PartB")

    def build_part_c(self):
        self.product.add_part("PartC")

    def get_product(self):
        return self.product


# Клиентский код, использующий все три паттерна
def main():
    # Использование паттерна Фабрика
    factory = Factory()
    product_a = factory.create_product("A", "ProductA")
    product_a.operate()

    # Использование паттерна Абстрактная фабрика
    factory_x = ConcreteFactoryX()
    product_ax = factory_x.create_product_a()
    product_ax.operate()

    # Использование паттерна Строитель
    builder = ConcreteProductBuilder()
    builder.build_part_a()
    builder.build_part_b()
    builder.build_part_c()
    product = builder.get_product()
    product.list_parts()


if __name__ == "__main__":
    main()
