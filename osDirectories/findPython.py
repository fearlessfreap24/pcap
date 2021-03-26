import os


def print_path(root_dir, dirs):
    return


def travel_dirs(path: str, dirs: str):
    os.chdir(path)
    curr_dir = os.getcwd()
    dirs_list = os.listdir()
    if len(dirs_list) == 0:
        return
    else:
        if curr_dir.endswith(dirs):
            print_path(path, curr_dir)

        for item in dirs_list:
            travel_dirs(curr_dir+"/"+item, dirs)


def get_user_input():
    valid_dirs = ['tree', 'c', 'cpp', 'python', 'other_courses']
    user_path = input("Please type the path to start with (must start with ./tree): ")
    while not user_path.startswith("./tree"):
        print("User input not valid")
        user_path = input("Please type the path to start in (must start with ./tree): ")

    return user_path


def validate_path(user_path):    
    valid_dirs = ['tree', 'c', 'cpp', 'python', 'other_courses']
    for dirs in user_path.split('/')[1:]:
        if dirs not in valid_dirs:
            return False
    return True


if __name__ == "__main__":
    path = get_user_input()

    valid_path = validate_path(path)

    while not valid_path:
        path = get_user_input()
        valid_path = validate_path(path)