"""
Brian Horner
CS 521 - Summer 1
Date: 6/22/2021
Homework Problem: 6_12_2
This program defines an Organ super class and Heart and Brain
subclasses. Each class has individual methods.
"""


class Organ:
    """Organ class that has the following attributes: organ_name,
    organ_weight_grams, is_vital_organ, organ_system, is_transpantable,
    and organ_gender. It comes with a repr method for printing."""
    def __init__(self, organ_name="", organ_weight_grams=0.0,
                 is_vital_organ='No', organ_system='',
                 is_transplantable='No', organ_gender=''):
        # Associating inputs with attributes
        self.__organ_name = organ_name
        self.organ_weight_grams = organ_weight_grams
        self.is_vital_organ = is_vital_organ
        self.organ_system = organ_system
        self.is_transplantable = is_transplantable
        self.organ_gender = organ_gender

    def __repr__(self):
        """Returns organ attributes in a printable manner."""
        return f"-{self.__organ_name}- \n" \
               f"Weight in grams: {self.organ_weight_grams}\n" \
               f"Vital Organ: {self.is_vital_organ}\n" \
               f"Organ System: {self.organ_system}\n" \
               f"Transplantable: {self.is_transplantable}\n" \
               f"Organ Gender: {self.organ_gender}\n"


class Heart(Organ):
    """Heart class that is a child-class of the Organ class. It has the
    following attributes: heart_length_cm, heart_weight_grams,
    heart_thickness_cm, heart_breath_cm. It uses the parent class to
    process the heart_weight_grams."""
    def __init__(self, heart_length_cm=0.0, heart_weight_grams=0.0,
                 heart_thickness_cm=0.0, heart_breadth_cm=0.0):
        # Using parent class to process the heart_weight_grams input.
        super().__init__(organ_weight_grams=heart_weight_grams)
        self.heart_length_cm = heart_length_cm
        self.heart_thickness_cm = heart_thickness_cm
        self.heart_breadth_cm = heart_breadth_cm

    def __repr__(self):
        """Returns heart attributes in a printable manner."""
        return f" -Heart- \n" \
               f"Length in centimeters: {self.heart_length_cm}\n" \
               f"Weight in grams: {self.organ_weight_grams}\n" \
               f"Thickness in centimeters: {self.heart_thickness_cm}\n" \
               f"Breadth in centimeters: {self.heart_breadth_cm}\n"

    @staticmethod
    def heart_status():
        """Returns the current status of the heart which is currently
        pumping blood."""
        return 'Pumping blood...\n'

    def heart_weight(self):
        """Converts heart weight from grams to ounces using
        organ_weight_grams."""
        return f"The heart's weight in ounces is" \
               f" {(float(self.organ_weight_grams) / 0.035):,.2f}\n"


class Brain(Organ):
    """Brain class that is a child-class of the Organ class. It has the
    following attributes: brain_volume and brain_weight_grams.
    It uses the parent class to process the brain_weight_grams."""

    def __init__(self, brain_volume=0.0, brain_weight_grams=0.0):
        # Using parent class to process brain_weight_grams input
        super().__init__(organ_weight_grams=brain_weight_grams)
        self.brain_volume = brain_volume

    def __repr__(self):
        """Returns Brain class in a printable manner."""
        return f"-Brain- \n" \
               f"Volume in centimeters: {self.brain_volume}\n" \
               f"Weight in grams: {self.organ_weight_grams}\n"

    @staticmethod
    def brain_status():
        """Returns brain status of thinking."""
        return "Thinking...\n"

    def brain_weight_oz(self):
        """Converts brain weight from grams to ounces
        using organ_weight_grams."""
        return f"The brain's weight in ounces is:" \
               f" {(float(self.organ_weight_grams) / 0.035):,.2f}\n"


if __name__ == "__main__":

    """Unit tests"""
# Testing general Organ class
lungs = Organ('Lungs', 3.5, 'Yes', 'Respitory', 'Yes', 'Male')
print(lungs)

# Testing Heart subclass and methods
heart_test = Heart(12, 280, 6.0, 9.0)
print(heart_test)
print(heart_test.heart_weight())
print(heart_test.heart_status())

# Testing Brain subclass and methods
brain_test = Brain(1260, 1370.0)
print(brain_test)
print(brain_test.brain_status())
print(brain_test.brain_weight_oz())
