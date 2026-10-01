"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")

print(f"\nOriginal String: {raw_message}")
print(f"Modified String Strip: {raw_message.strip()}")
print(f"Modified String Title: {raw_message.title()}")
print(f"Modified String Upper: {raw_message.upper()}")

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
