from UserGraph import user_graph, users
from Person import Person
import datetime

def is_empty_input(prompt, error_message):
    """
    function to validate user input is not empty
    """
    user_input = input(prompt).strip()
    while user_input == '':
        print(error_message)
        user_input = input(prompt).strip()
    return user_input


def select_user(prompt):
    """
    function to select a user by number from displayed list
    """
    print("\nAvailable users:")
    for i, u in enumerate(users, start=1):
        print(f"[{i}] {u.name}")

    selected_user = None
    while selected_user is None:
        choice_input = is_empty_input(prompt, "Input cannot be empty!")
        if not choice_input.isdigit():
            print("Invalid input! Enter the number corresponding to the user.")
            continue
        choice = int(choice_input)
        if choice < 1 or choice > len(users):
            print("Invalid choice! Select a number from the list.")
            continue
        selected_user = users[choice - 1]
    return selected_user

def display_all_users():
    """
    display all users names
    """
    print("\n" + "=" * 100)
    print(f"{'ALL USERS':^100s}")
    print("=" * 100)
    for i, u in enumerate(users, start=1):
        print(f"[{i}] {u.name}")
    print("-" * 100 + "\n")


def view_profile():
    """
    view profile of a selected user (with privacy check)
    """
    print("\n" + "=" * 100)
    print(f"{'VIEW PROFILE':^100s}")
    print("=" * 100)
    user = select_user("Enter the number of the user to view profile: ")
    print(f"\nName: {user.name}")
    if user.privacy.lower() == 'public':
        print(f"Gender: {user.gender}")
        print(f"Bio: {user.bio}")
        print(f"Privacy: {user.privacy}")
        print(f"Date of Birth: {user.dob}")
    else:
        print("Other details are hidden due to privacy settings.")
    print("-" * 100 + "\n")


def view_following():
    """
    view the list of accounts a user follows (outgoing edges)
    """
    print("\n" + "=" * 100)
    print(f"{'VIEW FOLLOWING':^100s}")
    print("=" * 100)
    user = select_user("Enter the number of the user to see who they follow: ")
    following = user_graph.listOutgoingAdjacentVertex(user)
    print(f"\n{user.name} follows:")
    if following:
        for u in following:
            print(f"- {u.name}")
    else:
        print("- No one")
    print("-" * 100 + "\n")


def view_followers():
    """
    view the list of users who follow the selected user (incoming edges)
    """
    print("\n" + "=" * 100)
    print(f"{'VIEW FOLLOWERS':^100s}")
    print("=" * 100)
    user = select_user("Enter the number of the user to see their followers: ")
    followers = []
    for u in users:
        following = user_graph.listOutgoingAdjacentVertex(u)
        if user in following:
            followers.append(u)
    print(f"\nFollowers of {user.name}:")
    if followers:
        for u in followers:
            print(f"- {u.name}")
    else:
        print("- No one")
    print("-" * 100 + "\n")


def add_user():
    """
    add a new user profile on-demand
    """
    print("\n" + "=" * 100)
    print(f"{'ADD NEW USER':^100s}")
    print("=" * 100)
    name = is_empty_input("Enter new user's name: ", "Name cannot be empty!")
    gender = is_empty_input("Enter gender: ", "Gender cannot be empty!")
    bio = is_empty_input("Enter bio: ", "Bio cannot be empty!")
    privacy = ''
    while privacy.lower() not in ['public', 'private']:
        privacy = is_empty_input("Enter privacy setting [Public/Private]: ", "Cannot be empty!")
        if privacy.lower() not in ['public', 'private']:
            print("Invalid input! Must be 'Public' or 'Private'.")
    dob = is_empty_input("Enter date of birth [YYYY-MM-DD]: ", "Cannot be empty!")

    new_user = Person(name, gender, bio, privacy, dob)
    users.append(new_user)
    user_graph.addVertex(new_user)
    print(f"\nUser '{name}' added successfully!\n")


def follow_user():
    """
    make a user follow another user on-demand
    """
    print("\n" + "=" * 100)
    print(f"{'FOLLOW USER':^100s}")
    print("=" * 100)
    follower = select_user("Enter the number of the follower: ")
    followed = select_user("Enter the number of the user to follow: ")
    if user_graph.hasEdge(follower, followed):
        print(f"{follower.name} already follows {followed.name}.\n")
    else:
        user_graph.addEdge(follower, followed)
        print(f"{follower.name} now follows {followed.name}.\n")


def unfollow_user():
    """
    make a user unfollow another user on-demand
    """
    print("\n" + "=" * 100)
    print(f"{'UNFOLLOW USER':^100s}")
    print("=" * 100)
    follower = select_user("Enter the number of the follower: ")
    followed = select_user("Enter the number of the user to unfollow: ")
    if user_graph.hasEdge(follower, followed):
        user_graph.removeEdge(follower, followed)
        print(f"{follower.name} has unfollowed {followed.name}.\n")
    else:
        print(f"{follower.name} does not follow {followed.name}.\n")


def menu():
    """
    main menu function
    """
    option = 0
    while option != 8:
        print("\n" + "=" * 100)
        print(f"{'WELCOME TO MINIGRAM!':^100s}")
        print("=" * 100)
        print("[1] View all users")
        print("[2] View someone's profile")
        print("[3] View following")
        print("[4] View followers")
        print("[5] Add a new user")
        print("[6] Follow a user")
        print("[7] Unfollow a user")
        print("[8] Exit")
        print("-" * 100)

        option_input = is_empty_input("Please select an option (1-9): ", "Input cannot be empty!")
        if not option_input.isdigit():
            print("Invalid input! Please enter a number between 1-9.")
            continue

        option = int(option_input)

        match option:
            case 1:
                display_all_users()
            case 2:
                view_profile()
            case 3:
                view_following()
            case 4:
                view_followers()
            case 5:
                add_user()
            case 6:
                follow_user()
            case 7:
                unfollow_user()
            case 8:
                print("\nExiting program. Byebye!")
            case _:
                print("Invalid choice! Please select a valid option.")

def main():
    menu()

if __name__ == "__main__":
    main()
