print("""
      Contoh Kalimat yang harus digunakan saat Interview Kerja
      Dengan contoh data diri yang kalian punya
      """)
client_name = str(input("nama Kamu : "))
client_graduate = str(input("Lulisan Sekolah/Universitas : "))
client_city = str(input(" : "))
client_age = int(input("Umur kamu (Masukkan angka saja) : "))
client_skill = str(input("Keahlian dalam bidang apa yang kamu miliki: "))

print(client_name)
print(client_city)
print(client_age)
print(client_skill)

skill_interview = {
    "Nama        :" : client_name,
    "Asal Negara :" : client_city,
    "Umur        :" : client_age,
    "Skill       :" : client_skill,
    "Lulusan Dari:" : client_graduate
}

print("Baik pak, perkenalkan nama saya " + skill_interview["Nama        :"])
print("Saya merupakan lulusan dari SMK " + skill_interview["Lulusan Dari:"])
print("keahlian saya dalam bidang " + skill_interview["Skill       :"] + "Membuat salah satu alasan saya melamar di perusahaan ini.")
