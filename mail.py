import mailtrap as mt

# create mail object
mail = mt.Mail(
    sender=mt.Address(email="mailtrap@linocesar.dev", name="Mailtrap Test"),
    to=[mt.Address(email="souzaces@gmail.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
)
