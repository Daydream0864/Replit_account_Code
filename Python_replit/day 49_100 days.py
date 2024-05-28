#print("""🌟Current Leader🌟

#Analyzing high scores......""")

#f = open("high.score","r")
#bank_accounts = f.read()

# Remove leading/trailing whitespaces and split by newline character
#account_entries = [entry.strip() for entry in #bank_accounts.strip().split('\n')]
#print(account_entries)
# Initialize an empty dictionary
#bank_dict = {}

#for entry in account_entries:
# Split each entry into bank abbreviation and account number
#  bank, account_number = entry.split(' ')

# Add bank abbreviation as a key and account number as its value
#   bank_dict[bank] = account_number

#print(bank_dict)

#####
bank_data = {}

# Open the file
with open('high.score', 'r') as f:
  lines = f.readlines()

for line in lines:
  # Remove leading/trailing whitespaces
  stripped_line = line.strip()

  # Split each entry into bank code and account number
  bank_code, account_number = stripped_line.split(' ')
  

  # Convert account number string to integer
  account_number = int(account_number)
  print(bank_code, account_number)

  # Store bank_code and account_number into our dictionary
  bank_data[bank_code] = account_number

print(bank_data)

highest_bank = max(bank_data, key=lambda k: bank_data[k])
print(
  f"The bank with the highest account number is '{highest_bank}'' with an account number of '{bank_data[highest_bank]}'."
)
