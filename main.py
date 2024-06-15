import os
import qrcode
import webbrowser
import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image

ddds = {
    "Brasil (+55)": "+55",
    "Estados Unidos (+1)": "+1",
    "Argentina (+54)": "+54",
    "Portugal (+351)": "+351",
    "Reino Unido (+44)": "+44",
    "França (+33)": "+33",
    "Alemanha (+49)": "+49",
    "Itália (+39)": "+39",
    "Espanha (+34)": "+34",
    "Canadá (+1)": "+1",
    "Austrália (+61)": "+61",
    "Nova Zelândia (+64)": "+64",
    "México (+52)": "+52",
    "Chile (+56)": "+56",
    "Colômbia (+57)": "+57",
    "Peru (+51)": "+51",
    "Venezuela (+58)": "+58",
    "Uruguai (+598)": "+598",
    "Paraguai (+595)": "+595",
    "Bolívia (+591)": "+591",
    "Equador (+593)": "+593",
    "Costa Rica (+506)": "+506",
    "Panamá (+507)": "+507",
    "Japão (+81)": "+81",
    "Coreia do Sul (+82)": "+82",
    "China (+86)": "+86",
    "Índia (+91)": "+91",
    "Rússia (+7)": "+7",
    "África do Sul (+27)": "+27",
    "Nigéria (+234)": "+234",
    "Gana (+233)": "+233",
    "Quênia (+254)": "+254",
    "Egito (+20)": "+20",
    "Turquia (+90)": "+90",
    "Grécia (+30)": "+30",
    "Suíça (+41)": "+41",
    "Suécia (+46)": "+46",
    "Dinamarca (+45)": "+45",
    "Noruega (+47)": "+47",
    "Finlândia (+358)": "+358",
    "Polônia (+48)": "+48",
    "Hungria (+36)": "+36",
    "Áustria (+43)": "+43",
    "Irlanda (+353)": "+353",
    "Holanda (+31)": "+31",
    "Bélgica (+32)": "+32",
    "Luxemburgo (+352)": "+352",
    "República Tcheca (+420)": "+420",
    "Eslováquia (+421)": "+421",
    "Eslovênia (+386)": "+386",
    "Croácia (+385)": "+385",
    "Bulgária (+359)": "+359",
    "Romênia (+40)": "+40",
    "Ucrânia (+380)": "+380",
    "Estônia (+372)": "+372",
    "Letônia (+371)": "+371",
    "Lituânia (+370)": "+370",
    "Malásia (+60)": "+60",
    "Singapura (+65)": "+65",
    "Tailândia (+66)": "+66",
    "Indonésia (+62)": "+62",
    "Filipinas (+63)": "+63",
    "Vietnã (+84)": "+84",
    "Israel (+972)": "+972",
    "Arábia Saudita (+966)": "+966",
    "Emirados Árabes Unidos (+971)": "+971",
    "Kuwait (+965)": "+965",
    "Qatar (+974)": "+974",
    "Bahrein (+973)": "+973",
    "Omã (+968)": "+968",
    "Bahamas (+1)": "+1",
    "Trinidad e Tobago (+1)": "+1",
    "Jamaica (+1)": "+1",
    "Barbados (+1)": "+1",
    "Granada (+1)": "+1",
    "Santa Lúcia (+1)": "+1",
    "Dominica (+1)": "+1",
    "Haiti (+509)": "+509",
    "República Dominicana (+1)": "+1",
    "Cuba (+53)": "+53",
    "Guatemala (+502)": "+502",
    "Honduras (+504)": "+504",
    "El Salvador (+503)": "+503",
    "Nicarágua (+505)": "+505",
    "Cuba (+53)": "+53",
    "Guatemala (+502)": "+502",
    "Honduras (+504)": "+504",
    "El Salvador (+503)": "+503",
    "Nicarágua (+505)": "+505",
}

os.makedirs("Qr_code", exist_ok=True)

def gerar_qr_code():
    nome = entrada_nome.get().strip()
    ddd = combobox_ddd.get().split(" ")[-1]  
    numero = entrada_numero.get().strip()
    email = entrada_email.get().strip()
    rede_social = entrada_rede_social.get().strip()

    if not nome:
        print("Nome não fornecido.")
        return  

    def criar_qr(data, file_name):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        file_path = os.path.join("Qr_code", file_name)
        img.save(file_path)
        print(f"QR Code salvo em: {file_path}")

    
    if numero:
        telefone = f"{ddd} {numero}"
        criar_qr(telefone, f"{nome}_telefone_qrcode.png")

    
    if email:
        criar_qr(email, f"{nome}_email_qrcode.png")

    
    if rede_social:
        criar_qr(rede_social, f"{nome}_rede_social_qrcode.png")

    
    messagebox.showinfo("Sucesso", "QR Code gerado com sucesso!")


def abrir_linkedin():
    webbrowser.open("https://www.linkedin.com/in/isllantoso/")


app = ctk.CTk()
app.geometry("600x800")
app.title("Gerador de QR Code")


label_nome = ctk.CTkLabel(app, text="Digite seu nome:")
label_nome.pack(pady=10)

entrada_nome = ctk.CTkEntry(app, width=250)
entrada_nome.pack(pady=10)

label_ddd = ctk.CTkLabel(app, text="Selecione o DDD do país:")
label_ddd.pack(pady=10)

combobox_ddd = ttk.Combobox(app, values=list(ddds.keys()), state="readonly")
combobox_ddd.pack(pady=10)
combobox_ddd.current(0)

label_numero = ctk.CTkLabel(app, text="Digite o número de telefone:")
label_numero.pack(pady=10)

entrada_numero = ctk.CTkEntry(app, width=250)
entrada_numero.pack(pady=10)

label_email = ctk.CTkLabel(app, text="Digite o e-mail:")
label_email.pack(pady=10)

entrada_email = ctk.CTkEntry(app, width=250)
entrada_email.pack(pady=10)

label_rede_social = ctk.CTkLabel(app, text="Digite a rede social:")
label_rede_social.pack(pady=10)

entrada_rede_social = ctk.CTkEntry(app, width=250)
entrada_rede_social.pack(pady=10)

botao_gerar = ctk.CTkButton(app, text="Gerar QR Code", command=gerar_qr_code)
botao_gerar.pack(pady=10)


label_desenvolvido = ctk.CTkLabel(app, text="Desenvolvido pelo Isllan Toso")
label_desenvolvido.pack(side="bottom", pady=10)


botao_linkedin = ctk.CTkButton(app, text="LinkedIn", command=abrir_linkedin)
botao_linkedin.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)


app.mainloop()
