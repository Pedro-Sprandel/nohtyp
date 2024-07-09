from translator import translate

with open('example.yp', 'r') as f:
    input_code = f.read()

if __name__ == "__main__":
    translated_code = translate(input_code)

    with open('resultado.py', 'w') as f:
        f.write(translated_code)

    print("Translation saved to resultado.txt")