class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        Showing type of property and what it has
        :param square_feet:
        :param beds:
        :param baths:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

        def display(self):
            """
            Shows on screen Property details
            """
            print("PROPERTY DETAILS")
            print("================")
            print("square footage: {}".format(self.square_feet))
            print("bedrooms: {}".format(self.num_bedrooms))
            print("bathrooms:  {}".format(self.num_baths))
            print()

        def prompt_init():
            return dict(square_feet = input("Enter the square feet:  "),
                    beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: "))
        prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony = '', laundry = '', **kwargs):
        """
        Saving all parameters in apartment
        :param balcony:
        :param laundry:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Shows all params on screen
        :return:
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def get_valid_input(input_string, valid_options):
        """
        checking if input is valid
        :param valid_options:
        :return:
        """
        input_string += " ({}) ".format(", ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response

    def prompt_init():
        """
        function that make all work together
        :return:
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does"
            "the property have? ",
            Apartment.valid_laundries)
        '''while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does"
                    "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))'''
        balcony = get_valid_input(
            "Does the property have a balcony?",
            Apartment.valid_balconies)
        '''while balcony.lower() not in \
                Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony?"
                "({})".format(
                ", ".join(Apartment.valid_balconies)))'''
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init() = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("arrached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',garage='',fenced='',**kwargs):
        """
        Saving all parameters in house
        :param num_stories:
        :param garage:
        :param fenced:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Shows all params on screen
        :return:
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        function that make all work together
        :return:
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                    House.valid_fenced)
        garage = get_valid_input("Is there a garage?",
                    House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase(self, price ='', taxes = '', **kwargs ):
    super().__init__(**kwargs)
    self.price = price
    self.taxes = taxes

    def display(self):
        """
        showing all params of property what is choosen for purchase
        :return:
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        makes all work together
        :return:
        """
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self, furnished = '', utilities = '', rent = '', **kwargs):
        """
        saving all params of property what is choosen for rent
        :param furnished:
        :param utilities:
        :param rent:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        showing all params of property what is choosen for rent
        :return:
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        makes all class functions work together
        :return:
        """
        return  dict(
            rent = input("What is the monthly rent? "),
            utilities = input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished ",
                    ("yes", "no")))
    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
    """
    updates when smb choose a house to rent
    """
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):
    """
    updates when smb choose an apartment to rent
    """
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    """
    updates when smb choose an apartment to purchase
    """
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, Apartment):
    """
    updates when smb choose a house to purchase
    """
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    """
    Has list of properties that some agent sells
    """
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()
