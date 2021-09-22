import glob
import zipfile

arsivlenecekDosyalar=[]

for belge in glob.iglob("**/*", recursive=True):
  arsivlenecekDosyalar.append(belge)

with zipfile.ZipFile("arsiv.zip", "w") as arsiv:
  for dosya in arsivlenecekDosyalar:
    arsiv.write(dosya)