import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gdk, Gtk
from os.path import abspath, dirname, join

WHERE_AM_I = abspath(dirname(__file__))

class pantallaInicio:

    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('pantallas.glade')

        # Cargar el aspecto de la  app
        self.set_style()

        # Inicializar variables
        self.stringN = []
        self.stringP = []

        self.numMon2 = 0
        self.numMon1 = 0
        self.numMon050 = 0
        self.numMon020 = 0
        self.numMon010 = 0
        self.numMon005 = 0

        # Objetos
        self.venprincipal = b.get_object('win_pricipal')
        self.venCompra = b.get_object('win_compra')
        self.venDialog = b.get_object('winDialogo')
        self.pricePro = b.get_object('lblPrecioProdu')
        self.namePro = b.get_object('lblProducto')
        self.monedero = b.get_object('lblpricemonedero')
        self.resultado = b.get_object('lblResultad')
        self.monedas = b.get_object('lblMonedas')


        # Diccionario
        # Eventos
        dic = {'on_win_pricipal_destroy': self.salir,
               'on_win_compra_destroy' :self.closeCompra,
               'on_btnExit_clicked': self.salir,
               'on_btnPizza_clicked': self.openCompraPizza,
               'on_btnSpace_clicked' : self.openCompraSpace,
               'on_btnItalia_clicked': self.openCompraItalia,
               'on_btnCheese_clicked' : self.openCompraCheese,
               'on_btnProteins_clicked':self.openCompraProteins,
               'on_btnChicken_clicked':self.openCompraChicken,
               'on_btnSugar_clicked':self.openCompraSugar,
               'on_btnBattery_clicked':self.openCompraBattery,
               'on_btnNails_clicked':self.openCompraNails,
               'on_btnSalirwinCom_clicked':self.closeCompra,
               'on_btnCompra_clicked': self.comprobarPrice,
               'on_btn2_clicked' : self.sum2,
               'on_btn1_clicked' : self.sum1,
               'on_btn50_clicked': self.sum50,
               'on_btn20_clicked': self.sum20,
               'on_btn10_clicked': self.sum10,
               'on_btn5_clicked' : self.sum5,
               'on_btnVerDialog_activate' : self.verDialog,
               'on_btnsalirmenu_activate' : self.salir,
               'on_btnSalirDia_clicked' : self.exitDiaglog,
               'on_winDialogo_destroy' : self.exitDiaglog,}

        b.connect_signals(dic)

        #cerrar ventana de evento
        self.venCompra.connect('delete-event', lambda w,e:w.hide() or True)
        self.venprincipal.show()

    # Cargamos el tema oscuro para nuestra app
    def set_style(self):
        provider = Gtk.CssProvider()
        provider.load_from_path(join(WHERE_AM_I, 'gtk-dark.css'))
        screen = Gdk.Display.get_default_screen(Gdk.Display.get_default())
        GTK_STYLE_PROVIDER_PRIORITY_APPLICATION = 600
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider,
          GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
        )


    # Cerrar ventana principal
    def salir(self, widget, data=None):
        Gtk.main_quit()

    # Abrir de la ventana de dialog
    def verDialog(self,widget,data=None):
        self.venDialog.show()

    # Salir de la ventana de dialog
    def exitDiaglog(self,widget,data=None):
        self.venDialog.hide()

    # Abrir ventana para pagar una Pizza
    def openCompraPizza(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "pizza"
        self.stringP = "20"
        self.pricePro.set_text("Precio del producto: 20€")
        self.namePro.set_text(" Producto: Pizza")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar una Nave Espacial
    def openCompraSpace(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "space"
        self.stringP = "100"
        self.pricePro.set_text("Precio del producto: 100€")
        self.namePro.set_text(" Producto: SpaceShip")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar Spagettis
    def openCompraItalia(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "italia"
        self.stringP = "19"
        self.pricePro.set_text("Precio del producto: 19€")
        self.namePro.set_text(" Producto: Spagettis")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar Queso
    def openCompraCheese(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "queso"
        self.stringP = "5.90"
        self.pricePro.set_text("Precio del producto: 5,90€")
        self.namePro.set_text(" Producto: Queso")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar Proteinas
    def openCompraProteins(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "proteinas"
        self.stringP = "1"
        self.pricePro.set_text("Precio del producto: 1€")
        self.namePro.set_text(" Producto: Proteinas")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar un Pollo
    def openCompraChicken(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "pollo"
        self.stringP = "8.65"
        self.pricePro.set_text("Precio del producto: 8,65€")
        self.namePro.set_text(" Producto: Pollo")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar Edulcorante
    def openCompraSugar(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "azucar"
        self.stringP = "2"
        self.pricePro.set_text("Precio del producto: 2€")
        self.namePro.set_text(" Producto: Edulcorante")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar Pilas
    def openCompraBattery(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "pilas"
        self.stringP = "2.65"
        self.pricePro.set_text("Precio del producto: 2,65€")
        self.namePro.set_text(" Producto: Pilas")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Abrir ventana para pagar Clavos
    def openCompraNails(self, widget, data=None):
        self.resultado.set_text(str(""))
        self.monedas.set_text(str(""))
        self.stringN = "nails"
        self.stringP = "0.95"
        self.pricePro.set_text("Precio del producto: 0,95€")
        self.namePro.set_text(" Producto: Clavos")
        self.monedero.set_text("0")
        self.venCompra.show()

    # Cerrar ventana para pagar
    def closeCompra(self, widget, data=None):
        self.venCompra.hide()

    # Sumar 2€ al monedero
    def sum2(self, widget, data=None):
        self.monedero.set_text(str(float(self.monedero.get_text()) + 2))

    # Sumar 1€ al monedero
    def sum1(self, widget, data=None):
        self.monedero.set_text(str(float(self.monedero.get_text()) + 1))

    # Sumar 0.5€ al monedero
    def sum50(self, widget, data=None):
        self.monedero.set_text(str(round(float(self.monedero.get_text()) + 0.50,3)))

    # Sumar 0.2€ al monedero
    def sum20(self, widget, data=None):
        self.monedero.set_text(str(round(float(self.monedero.get_text()) + 0.20,3)))

    # Sumar 0.1€ al monedero
    def sum10(self, widget, data=None):
        self.monedero.set_text(str(round(float(self.monedero.get_text()) + 0.10,3)))

    # Sumar 0.05€ al monedero
    def sum5(self, widget, data=None):
        self.monedero.set_text(str(round(float(self.monedero.get_text()) + 0.05,3)))

    # Comprobar que el valor del monedero es superior al del producto
    # Si lo es, vemos si es divisible entre cada moneda para saber cuantas monedas devolver
    # Si no, sacamos mensaje de dinero insuficiente.
    def comprobarPrice(self, widget, data=None):

        if self.stringN == "pizza":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Pizza comprada -- Cambio a dar: " + str(resu)+"€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "space":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Space Ship comprada -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "italia":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Spagettis comprados -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "queso":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Queso comprado -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "proteinas":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Proteinas compradas -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "pollo":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Pollo comprado -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "azucar":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Edulcorante comprado -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "pilas":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP), 3))
                self.resultado.set_text(str("Pilas compradas -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        elif self.stringN == "nails":
            if float(self.stringP) <= float(self.monedero.get_text()):
                resu = str(round(float(self.monedero.get_text()) - float(self.stringP),3))
                self.resultado.set_text(str("Clavos comprados -- Cambio a dar: " + resu + "€"))
                self.devolverMonedas()

            else:
                self.resultado.set_text(str("No tienes suficiente dinero en el monedero."))

        else:
            self.resultado.set_text(str("No tienes suficiente dinero en el monedero"))


    # Metodo para saber cuantas monedas de cambio dar
    def devolverMonedas(self):

        self.numMon2 = 0
        self.numMon1 = 0
        self.numMon050 = 0
        self.numMon020 = 0
        self.numMon010 = 0
        self.numMon005 = 0

        resu = round(float(self.monedero.get_text()) - float(self.stringP),2)

        while True:
            if (resu - 2) < 0:
                break
            else:
                self.numMon2 = self.numMon2 + 1
                resu = resu - 2

        while True:
            if (resu - 1) < 0:
                break
            else:
                self.numMon1 = self.numMon1 + 1
                resu = resu - 1

        while True:
            if (resu - 0.5) < 0:
                break
            else:
                self.numMon050 = self.numMon050 + 1
                resu = resu - 0.5

        while True:
            if (resu - 0.20) < 0:
                break
            else:
                self.numMon020 = self.numMon020 + 1
                resu = resu - 0.2

        while True:
            if (resu - 0.10) < 0:
                break
            else:
                self.numMon010 = self.numMon010 + 1
                resu = resu - 0.1

        if resu > float(0):
            self.numMon005 = self.numMon005 + 1
            resu = resu - 0.05
               

        # Mostramos en la lbl el resultado
        self.monedas.set_text(str(
            "Monedas de 2€: " + str(self.numMon2) + "   - 1€:" + str(self.numMon1) + "   - 0.50€:" + str(
                self.numMon050) + "   - 0.20€:" + str(self.numMon020) + "   - 0.10€:" + str(
                self.numMon010) + "   - 0.05€:" + str(self.numMon005)))


if __name__ == '__main__':
    main = pantallaInicio()
    Gtk.main()