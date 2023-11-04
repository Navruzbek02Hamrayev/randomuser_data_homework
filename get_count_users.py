import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    return len(data)
x=get_data.get_data('randomuser_data.json')
print(get_count_users(x))