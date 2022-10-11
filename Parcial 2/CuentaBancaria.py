class CuentaBancaria:

    #Constructor
    def __init__(self, numeroCuenta, nombreTitular):
        self._numeroCuenta = numeroCuenta
        self._nombreTitular = nombreTitular
        self._saldo
        self._numeroOperaciones = 0
        self._MAXIMOREINTEGRO = 5000
        self._cuentasCreadas = 0
    
    #Metodos
    def getNumeroCuenta(self):
        return self._numeroCuenta
    
    def getNombre(self):
        return self._nombreTitular

    def getSaldo(self):
        return self._saldo

    def setSaldo(self, saldo):
        self._saldo = saldo
    
    def getNumeroOperaciones(self):
        return self._numeroOperaciones

    def ingresarCantidad(self, cantidad):
        if(cantidad>0):
            self._saldo += cantidad
            self._numeroOperaciones+=1
            return True
        else:
            return False
        
    def retirarCantidad(self, cantidad):
        if(cantidad<=self._saldo):
            self._saldo -= cantidad
            self._numeroOperaciones+=1
            return True
        else:
            return False

    def getCuentasCreadas(self):
        return self._cuentasCreadas

    def setCuentasCreadasNull(self):
        pass