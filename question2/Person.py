class Person:
    def __init__(self, name, gender, bio, privacy, dob):
        """
        initialize a Person object

        :param name: full name of the user
        :param gender: gender of the user (male/female)
        :param bio: short biography of the user
        :param privacy: profile privacy setting (public/private)
        :param dob: date of birth of the user (format: YYYY-MM-DD)
        """
        self.name = name  # full name
        self.gender = gender  # gender
        self.bio = bio  # short biography
        self.privacy = privacy  # public/private
        self.dob = dob  # date of birth

    def view_profile(self):
        # display all info if public, otherwise name only
        if self.privacy.lower() == "public":
            print(f"Name: {self.name}")
            print(f"Gender: {self.gender}")
            print(f"Bio: {self.bio}")
            print(f"DOB: {self.dob}")
            print(f"Privacy: {self.privacy}")
        else:
            print(f"Name: {self.name} (Private Profile)")

    def __str__(self):
        output = ''
        output += '\nName     : ' + self.name + '\n'
        output += 'Gender   : ' + self.gender + '\n'
        output += 'Bio      : ' + self.bio + '\n'
        output += 'Privacy  : ' + self.privacy + '\n'
        output += 'DOB      : ' + self.dob + '\n'
        return output

