import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
result_dict= {row.letter:row.code for (index,row) in df.iterrows()}

inp = input("Enter a word: ").upper()
output_list = [result_dict[letter] for letter in inp]
print(output_list)




