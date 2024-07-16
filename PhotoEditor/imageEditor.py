from PIL import  Image, ImageEnhance, ImageFilter
import os

path = "./images"
pathOut = "./imagesEdited"

if __name__ == "__main__":
    for filename in os.listdir(path):
        clean_name = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1].lower()

        if extension in [".jpg", ".jpeg", ".png"]:
            try:
                img = Image.open(f"{path}/{filename}")
                edit = img.filter(ImageFilter.SHARPEN).convert("L")

                factor = 1.5
                enhancer = ImageEnhance.Contrast(edit)
                edit = enhancer.enhance(factor)

                clean_name = os.path.splitext(filename)[0]
                edit.save(f"{pathOut}/{clean_name}_edited.png")
                print(f"{filename} editado y guardado como {clean_name}_edited{extension}")
                
            except (IOError, SyntaxError) as e:
                print(f"El archivo {filename} no es una imagen válida o no se puede procesar.")       
    

