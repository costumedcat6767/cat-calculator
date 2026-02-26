def count_fish():
    print("Welcome to Cat Fish Inventory Calculator!")

    try:
        tuna = int(input("Enter number of Tuna fish: "))
        salmon = int(input("Enter number of Salmon fish: "))
        sardine = int(input("Enter number of Sardines: "))

        total = tuna + salmon + sardine

        print("\nFish Summary:")
        print("Tuna:", tuna)
        print("Salmon:", salmon)
        print("Sardines:", sardine)
        print("----------------------")
        print("Total Fish:", total)

        if total > 100:
            print("Wow! Your stock is booming!")
        elif total == 0:
            print("No fish left! Time to restock!")
        else:
            print("Get some more fish!")

    except ValueError:
        print("⚠️ Please enter valid numbers only.")

if __name__ == "__main__":
    count_fish()

#remember RC2 ~