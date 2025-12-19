from IGBO import igbo
from HAUSA import hausa
from TIV import tiv
from YORUBA import yoruba
from igbera import igbera

print("WELCOME TO COS 101 LANGUAGE TRANSLATOR")
print("-------------------------------------")
print("Choose a language:")
print("1. Igbo")
print("2. Hausa")
print("3. Tiv")
print("4. Yoruba")
print("5. igbera")

choice = input("Enter your choice (1-5): ")
word = input("Enter an English word: ").lower()

if choice == "1":
    print("Igbo:", igbo.get(word, "Word not found"))
elif choice == "2":
    print("Hausa:", hausa.get(word, "Word not found"))
elif choice == "3":
    print("Tiv:", tiv.get(word, "Word not found"))
elif choice == "4":
    print("Yoruba:", yoruba.get(word, "Word not found"))
elif choice == "5":
    print("igbera:", igbera.get(word, "Word not found"))
else:
    print("Invalid choice")



