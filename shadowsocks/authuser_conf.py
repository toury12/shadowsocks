#coding:utf-8
from shadowsocks import lru_cache

USER_INFO_CACHE = lru_cache.LRUCache(timeout=600)

# 如果后期需要用mysql的数据，可以修改这里面的逻辑
def user_info(config):
    if 'enable_auth' in config and config['enable_auth']:
        if 'username' in config and 'passwd' in config:
            return (True, config['username'], config['passwd'])
    return (False, None, None)  
