# python_version == '3.7'
import pickle

def load_data(file):
    users = { }

    try:
        file_object = open(file, 'rb')
        users = pickle.load(file_object)
        file_object.close()
    except:
        users = { }

    return users

def query_following(user_name):
    following = []
    the_users = load_data('followers.pydata')
    for key, value in the_users.items():
        for i in value:
            if user_name == i:
                following.append(key)

    print (following)
    return following

def update():
    del theusers['Lorna Carrico']
    theusers['Anne Smelcer'] = ['Christine Phillips', 'Charles Mason', 'Tim Lathrop']

    try:
        file_object = open('followers-updated.pydata', 'wb')
        pickle.dump(theusers, file_object)
        file_object.close()
    except Exception as e:
        print(e)
        print("\n Couldn't figure out how to store the updates in the list")

def get_num_of_followers():
    followers_number = { }

    try:
        file_object = open('followers-updated.pydata', 'rb')
        followers_number = pickle.load(file_object)
        file_object.close()
    except:
        followers_number = {}

    for key, value in followers_number.items():
        followers_number[key] = len(value)

    return followers_number

a_file = 'followers.pydata'
theusers = load_data(a_file)

# for key in theusers.keys():
#     print(key)

username = 'William Smith'
query_following(username)
update()
get_num_of_followers()

