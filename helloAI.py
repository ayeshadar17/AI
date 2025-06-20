print("i am AI bot. whats ur name?")
name=input()
print(f"nice to meet you,{name}")
print("how are you feeling today? good/bad")
mood=input().lower()
if mood=="good":
    print("i am glad to hear that")
elif mood=="bad":
    print("i am sorry to hear that")
else:
    print("i see sometimes its hard to put your feelings into words")
print(f"it was nice chatting with you {name}.good bye!")    