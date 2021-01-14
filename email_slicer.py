def email_slicer():
    email = input("Enter your email address : ").strip()
    user_name = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print("user_name: {}\ndomain: {}".format(user_name, domain))

email_slicer()