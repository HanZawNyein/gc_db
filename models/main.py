import models


class A(models.Model):
    _name = 'ica.a'  # Define _inherit to specify the class to be inherited dynamically

    def abc_method(self):
        print("A Method in ABC")

    def origin_method(self):
        print("Origin Method in ABC")


class B(models.Model):
    _inherit = 'ica.a'  # Define _inherit to specify the class to be inherited dynamically

    def abc_method(self):
        super(B, self).abc_method()
        print("B Method in ABC")


class C(models.Model):
    _name = 'ica.c'
    _inherit = 'ica.a'  # Define _inherit to specify the class to be inherited dynamically

    def abc_method(self):
        super(C, self).abc_method()
        print("C Method in ABC")

    def c_class_only_method(self):
        print("c class only method")


if __name__ == '__main__':
    print(models.env)
    # {'ica.a': <class '__main__.B'>, 'ica.c': <class '__main__.C'>}

    icaC = models.env['ica.c']()
    # icaC.abc_method()
    # A Method in ABC
    # B Method in ABC
    # C Method in ABC

    icaA = models.env['ica.a']()
    icaA.abc_method()
    # A Method in ABC
    # B Method in ABC

    icaC.origin_method()
    icaC.c_class_only_method()
