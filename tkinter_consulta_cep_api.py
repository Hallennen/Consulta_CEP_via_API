from tkinter import * 
from tkinter import ttk as tk
import requests
from tkinter import messagebox





class my_app:


    def app_run(self):
        info_pais = '-'

        #Config da tela 
        my_app = Tk()
        my_app.geometry('450x450+450+150')
        my_app.title('Consumo CEP via API')
        cor='#FFFFFF'
        my_app.configure(background=cor)


        #parte titulo
        titulo_tela = Label(my_app, text='Informe o CEP: ', font=('Georgia', 14),background=cor)
        titulo_tela.place(anchor=CENTER, relx=0.5, rely=0.05 )

        #campo input CEP
        self.input_CEP = Entry(my_app, borderwidth=1, highlightcolor= 'blue', highlightthickness= 2, font=('Arial', 12), justify='center' )
        self.input_CEP.place( relx=0.25, rely=0.12, relwidth=0.5)
        self.input_CEP.focus()
        buton_busca_cep = tk.Button(my_app, text='Buscar CEP',command= my_app_func.buscar_cep, cursor="hand2")
        buton_busca_cep.place(relx= 0.78, rely= 0.12)
        self.input_CEP.bind('<Return>', my_app_func.buscar_cep )



        #Retorno Estado
        label_estado = Label(my_app, text="Estado: ", font=('Arial', 12),background=cor)
        label_estado.place(rely=0.3, relx= 0.06)
        self.label_estado_entry = Label(my_app,  text= info_pais, relief='groove', background = 'lightgrey')
        self.label_estado_entry.place(rely=0.305, relx= 0.30, relwidth= 0.60, relheight=0.06)


        #Retorno Cidade 
        label_city = Label(my_app, text="Cidade: ", font=('Arial', 12),background=cor)
        label_city.place(rely=0.45, relx= 0.06)
        self.label_city_entry = Label(my_app, text=info_pais, relief='groove', background = 'lightgrey')
        self.label_city_entry.place(rely=0.455, relx= 0.30, relwidth= 0.60, relheight=0.06)


        #Retorno Bairro
        label_bairro = Label(my_app, text="Bairro: ", font=('Arial', 12),background=cor)
        label_bairro.place(rely=0.6, relx= 0.06)
        self.label_bairro_entry = Label(my_app,  text= info_pais, relief='groove', background = 'lightgrey')
        self.label_bairro_entry.place(rely=0.605, relx= 0.30, relwidth= 0.60, relheight=0.06)



        #Retorno tipo de endereço
        label_tipo = Label(my_app, text="Tipo: ", font=('Arial', 12),background=cor)
        label_tipo.place(rely=0.75, relx= 0.06)
        self.label_tipo_entry = Label(my_app,  text= info_pais, relief='groove', background = 'lightgrey')
        self.label_tipo_entry.place(rely=0.755, relx= 0.30, relwidth= 0.60, relheight=0.06)



        #Retorno Rua
        label_rua = Label(my_app, text="Logradouro: ", font=('Arial', 12),background=cor)
        label_rua.place(rely=0.9, relx= 0.06)
        self.label_rua_entry = Label(my_app,  text= info_pais, relief='groove', background = 'lightgrey')
        self.label_rua_entry.place(rely=0.905, relx= 0.30, relwidth= 0.60, relheight=0.06)




        return my_app.mainloop()
    
    

class my_app_func():
    def buscar_cep(event=None):
        try:
            cep = my_app.input_CEP.get()
            base_url = 'https://cep.awesomeapi.com.br/json/'

            retorno_api = requests.get(base_url + cep)

            my_app.input_CEP.delete(0, END)
            return my_app_func.att_campos(consulta=retorno_api.json())
        
        
        except:

            my_app.input_CEP.delete(0, END)
            
            return messagebox.showerror(title='error',message='VERIFIQUE O CEP INFORMADO')
        


    def att_campos(consulta):
        print(consulta['cep'])
        my_app.label_city_entry.configure(text=consulta['city'])
        my_app.label_estado_entry.configure(text=consulta['state'])
        my_app.label_bairro_entry.configure(text=consulta['district'])
        my_app.label_tipo_entry.configure(text=consulta['address_type'])
        my_app.label_rua_entry.configure(text=consulta['address_name'])
    
    

my_app.app_run(my_app)