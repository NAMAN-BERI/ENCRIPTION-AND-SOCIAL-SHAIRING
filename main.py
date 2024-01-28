import encription
import decription
import encripting_an_image
import decripting_an_image

# ENCRIPTING DATA
stego_key,auto_key = encription.encripting_data()
print("AUTO KEY : ", auto_key)
print("STEGO KEY : ", stego_key)

# ADDING DATA INTO IMAGE
encripting_an_image.encripting_image(stego_key,auto_key)
input("PRESS ENTER TO DECRIPT")

# TAKING DATA FROM IMAGE
decripted_autokey,decripted_stegokey = decripting_an_image.decription_image()
print("DECRIPTED AUTO KEY ", decripted_autokey)
print("DECRIPTED STEGO KEY ", decripted_stegokey)

# DECRIPTING DATA 
text = decription.decripting_data(decripted_stegokey,decripted_autokey)
print(text)