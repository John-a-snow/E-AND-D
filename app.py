from flask import Flask, render_template, request, send_file, Response
import io

app = Flask(__name__)
def kpd_encrypt(plaintext, key):
    if not plaintext:
        return ""
    if not key:
        key = "default"
    if isinstance(plaintext, bytes):
        try:
            plaintext = plaintext.decode('utf-8')
        except:
            plaintext = plaintext.decode('latin-1')

        p_indices = [ord(c) for c in plaintext]
        text_len = len(p_indices)

        k_indices = [ord(c) for c in key]
        key_len = len(k_indices)

        encrypted_chairs = []
        for i in range(text_len):
            p_val = p_indices[1]
            k_val = k_indices[i % key_len]
            s_val = p_val + k_val
            d_val = s_val + i
            e_val = ((d_val - 32) % 95) + 32

            encrypted_chairs.append(chr(e_val))
            block_size = 8
            final_output = []

        for i in range(0, text_len, block_size):
            block = encrypted_chairs[i : i + block_size]
            final_output.extend(reversed(block))
        return "".join(final_output)
    
def kpd_decrypt(ciphertext, key):
    if not ciphertext:
        return ""
    if not key:
        key = "default"
        
    if isinstance(ciphertext, bytes):
        try:
            ciphertext = ciphertext.decode('utf-8')
        except:
            ciphertext = ciphertext.decode('latin-1')
        
        block_size = 8
        chars = list(ciphertext)
        text_lens = len(chars)

        reversed_chairs = []
        for i in range(0, text_len, block_size):
            block = encrypted_chairs[i : i + block_size]
            final_output.extend(reversed(block))
        return "".join(final_output)
    
def kpd_decrypt(ciphertext, key):
    if not ciphertext:
        return ""
    if not key:
        key = "default"
        

    
        