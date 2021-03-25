import sys
import os
import main


def track():
    while True:
        filename = input('filename: ')
        if os.path.exists(filename):
            break
        print("Invalid option")

    while True:
        length = input('length: ')
        try:
            length = float(length)
            break
        except Exception:
            pass
        print("Invalid option")

    main.video = filename
    main.track(length)


def quit_program():
    """
    Quits program
    """
    print('Goodbye!')
    sys.exit()


def menu():
    menu_options = {
        'A': track,
        # 'B': load_status_updates,
        # 'C': add_user,
        # 'D': update_user,
        # 'E': search_user,
        # 'F': delete_user,
        # 'H': add_status,
        # 'I': update_status,
        # 'J': search_status,
        # 'K': delete_status,
        # 'L': add_image,
        # 'M': list_user_images,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
    A: track a file
    B: blah
    C: blah
    D: blah
    Q: Quit

    Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")


if __name__ == '__main__':
    menu()
