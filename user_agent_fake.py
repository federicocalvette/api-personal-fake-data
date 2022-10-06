from fake_useragent import UserAgent
ua = UserAgent()

def get_user_agent_fake():
    user_agent = ua.random
    print(f'User-Agent: {user_agent}')
    return user_agent