from CuentaBancaria import CuentaBancaria

class CuentaJoven(CuentaBancaria):

    #Constructor
    def __init__(self, numeroCuenta, nombreTitular):
        super().__init__(numeroCuenta, nombreTitular)

    #Metodos
    def ingresarCantidad(self, cantidad):
        return super().ingresarCantidad(cantidad)

    def retirarCantidad(self, cantidad):
        return super().retirarCantidad(cantidad)