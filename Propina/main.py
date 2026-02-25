import flet as ft

def main(page: ft.page):
    page.title ="Propinas"
    page.vertical_alignment = ft.MainAxisAligmnement.CENTER
    
    monto = ft.TextField(label = "Escribe el monto a pagar", width = 200)
    txt_valor = ft.Text(value = "5%", size = 25)
    
    def calcular(e):
        txt_valor.value =str(int(slider.value)) + '%'
        if monto.value != "":
            propina = int(monto.value) * slider.value / 100
            total = int(monto.value) + propina
            txt_propina.value = "La propona e: " + str(round(propina,2))
            txt_total.value = "El total a pagar es: " + str(round(total, 2))
            page.update()
            
    txt_propina = ft.Text("La propina es: ", size = 25)
    txt_total = ft.Text("El total a pagar es: ", size = 25)
        
    slider = ft.Sñider(min =5, max = 25, value = 5, on_change = clacular)
    page.add(txt_valor, monto, slider, txt_propina, txt_total)
    
    
            
ft.app(target = main)