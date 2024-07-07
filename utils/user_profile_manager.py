def get_user_profile():
    print("Please enter the user's profile information:")
    user_profile = {
        "Age": int(input("Age: ")),
        "Gender": input("Gender: "),
        "Interests": input("Interests (such as books, movies, etc.): ").split(", "),
        "Place of life (country)": input("Place of life (country): "),
        "Education level": input("Education level: "),
        "Job": input("Job: "),
        "Previous experience working with the site": input("Previous experience working with the site (Yes/No): "),
        "Level of familiarity with the Internet": input("Level of familiarity with the Internet: "),
        "Mobile or desktop user": input("Mobile or desktop user (Mobile/Desktop): "),
        "Other behavioral characteristics": input("Other behavioral characteristics: ").split(", ")
    }
    return user_profile
