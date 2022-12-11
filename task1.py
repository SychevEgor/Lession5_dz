text = 'абв и длт и абв и  так далее абв'

def delite(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delite(text)
print(text)