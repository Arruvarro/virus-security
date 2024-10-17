def custom_encrypt(plaintext):
    # Daftar huruf asli
    search = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # Daftar huruf pengganti
    replace = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

    # Gunakan placeholder sementara
    placeholder = [f"__{i}__" for i in range(len(search))]

    # Ganti huruf asli dengan placeholder sementara
    temp_text = plaintext
    for s, p in zip(search, placeholder):
        temp_text = temp_text.replace(s, p)

    # Ganti placeholder dengan huruf pengganti
    encrypted = temp_text
    for p, r in zip(placeholder, replace):
        encrypted = encrypted.replace(p, r)

    return encrypted

def custom_decrypt(ciphertext):
    # Daftar huruf asli
    search = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # Daftar huruf pengganti
    replace = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

    # Gunakan placeholder sementara
    placeholder = [f"__{i}__" for i in range(len(search))]

    # Ganti huruf pengganti dengan placeholder sementara
    temp_text = ciphertext
    for r, p in zip(replace, placeholder):
        temp_text = temp_text.replace(r, p)

    # Ganti placeholder dengan huruf asli
    decrypted = temp_text
    for p, s in zip(placeholder, search):
        decrypted = decrypted.replace(p, s)

    return decrypted

# Membaca input dari pengguna
original_text = input("Masukkan teks yang ingin dienkripsi: ")
print(f"Teks asli: {original_text}")

# Enkripsi teks
encrypted_text = custom_encrypt(original_text)
print(f"Teks terenkripsi: {encrypted_text}")

# Dekripsi teks
decrypted_text = custom_decrypt(encrypted_text)
print(f"Teks setelah dekripsi: {decrypted_text}")
