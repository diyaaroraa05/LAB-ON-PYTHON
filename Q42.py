def common_characters(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")
def main():
    common_characters('rose', 'goose')

main()
print("This code is written by DIYA ARORA ERP-0221BCA059")
