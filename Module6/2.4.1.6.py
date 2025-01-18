def seven_segment_display(number):
    digits = [
        ["###", "# #", "# #", "# #", "###"],  
        ["  #", "  #", "  #", "  #", "  #"],  
        ["###", "  #", "###", "#  ", "###"],  
        ["###", "  #", "###", "  #", "###"],  
        ["# #", "# #", "###", "  #", "  #"], 
        ["###", "#  ", "###", "  #", "###"], 
        ["###", "#  ", "###", "# #", "###"],  
        ["###", "  #", "  #", "  #", "  #"],  
        ["###", "# #", "###", "# #", "###"],  
        ["###", "# #", "###", "  #", "###"], 
    ]

    rows = [""] * 5
    for digit in str(number):
        for i in range(5):
            rows[i] += digits[int(digit)][i] + "  "

    return "\n".join(rows)


number = input("Enter a integer: ")

if not number.isdigit():
    print("please enter a non-negative integer.")
else:
    print(seven_segment_display(number))
