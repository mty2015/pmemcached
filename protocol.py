# -*- coding:utf-8 -*-
from pmemcached import StoreException

ERROR_COMMAND = 'ERROR'
ERROR_CLIENT = 'CLIENT_ERROR'
ERROR_SERVER = 'SERVER_ERROR'

SPACE = ' '

def assemble_store_command(command_type,key,value,tracking_data,exptime,asyn,cas=''):
    command_line = command_type + SPACE + key + SPACE + str(tracking_data) + SPACE + str(exptime) + SPACE \
                        + str(len(value)) + SPACE
    if command_type == 'cas':
        command_line = command_line + cas + SPACE 
    
    command_line = command_line + (asyn and 'noreply' or '')
    return command_line                    

def assemble_get_command(key,cas):
    return (cas and 'gets' or 'get') + SPACE + key

def check_reply_error(reply):
    if ERROR_COMMAND in reply:
        raise StoreException("data sent doesn't conform to the protocol in some way :" + reply[len(ERROR_COMMAND):])
    elif ERROR_SERVER in reply:
        raise StoreException("server error :" + reply[len(ERROR_SERVER):])
    elif ERROR_COMMAND in reply:
        raise StoreException('sent a nonexistent command name')
    

def parse_store_reply(handler):
    reply = handler.read_line()
    check_reply_error(reply)
    if ('NOT_FOUND' in reply) or ('EXISTS' in reply) or ('NOT_STORED' in reply) :
        return False
    elif 'STORED' in reply:
        return True
    else:
        raise StoreException('encounter an understand error!')
 
def parse_get_reply(handler,cas):
    reply = handler.read_line()
    check_reply_error(reply)
    if 'END' == reply :
        return None
    reply_segs = reply.split(SPACE)
    if reply_segs[0] != 'VALUE' :
        raise StoreException('expect [VALUE],but not')
    result = {}
    result['tracking_data'] = reply_segs[2]
    if len(reply_segs) == 5 :
        result['cas'] = reply_segs[4]
    byte_number = int(reply_segs[3])
    result['value'] = handler.read(byte_number)
    handler.read_line()# END\r\n
    return result
    
    
        
