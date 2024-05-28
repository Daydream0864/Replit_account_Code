inputname = input("Input your name > David Morgan").strip()

inputdate = input("Input your date of birth > 01/01/1900").strip()

inputphone = input("Input your telephone number > 01234 567890").strip()

inputemail = input("Input your email > david@replit.com").strip()


dicname = {
  "name": inputname,
  "age": inputdate,
  "phone": inputphone,
  "email": inputemail
}


print(f"hi {dicname['name']}. dictionary says that you were born on {dicname['age']} ")