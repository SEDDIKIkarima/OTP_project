import secrets
import os
import argparse


parent_dir = r"D:\M2\securite dans les sys d'information\[UAPV-SEC]_KARIMA_SEDDIKI_TP_03\dev\random"
p = r"D:\M2\securite dans les sys d'information\[UAPV-SEC]_KARIMA_SEDDIKI_TP_03"
'''
def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr
print(is_interface_up('eth0'))
'''
##############################################################################
                            # Generate mode #
##############################################################################
def gen_48() :
    # EMPTY -------> INT (48 BYTES)
    
    secretsgen = secrets.SystemRandom()
    otp = secretsgen.randrange(000000000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999)
    return otp

def gen_2000() :
    # EMPTY -------> INT (2000 BYTES)
    
    a=""
    for i in range(2000):
        a+="9"
    b=int(a)
    secretsgen = secrets.SystemRandom()
    otp = secretsgen.randrange(00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,b)
    return otp

path=''
dir_name = 0000

def generate():
     # EMPTY --------> DIRECTORIES,FILES
            ################# create directories #####################
            
    dir_name = 0000
    path = os.path.join(parent_dir, str(dir_name))      
    while os.path.exists(path):
        dir_name+=1
        path = os.path.join(parent_dir, str(dir_name))
    os.mkdir(path)

            ################### create files ######################
            
    for i in range(100):
        filename = str(i)+"p.txt"
        with open(os.path.join(path, filename), 'w') as temp_file:
            temp_file.write(str(gen_48()))
            
    for i in range(100):
        filename = str(i)+"s.txt"
        with open(os.path.join(path, filename), 'w') as temp_file:
            temp_file.write(str(gen_48()))

    for i in range(100):
        filename = str(i)+"c.txt"
        with open(os.path.join(path, filename), 'w') as temp_file:
            temp_file.write(str(gen_2000()))



##############################################################################
                            # Send mode #
##############################################################################    

def shift_letter(letter, shift):
    # str, int --------> str
    
    if letter.islower():
            alpha_position = ord('a')
    else:
            alpha_position = ord('A')
    gap = (ord(letter) - alpha_position + shift) % 26
    ord_letter = chr(gap + alpha_position)
    return ord_letter

def code(text, shift):
    # str, int --------> str
    
    index=0
    text_code=''
    for letter in text:
        result = shift_letter(letter, int(shift[index]))
        index += 1
        text_code += result
    return text_code

def send (path) :
    # STRING  ------------> FILES
    
    ################ get text #######################
    
    text=input("saisissez un message qui ne doit pas dépaser 2000 caractéres:")
    while (len(text) > 2000):
        print("le message ne doit pas dépasser 2000 caractéres")
        text=input("saissez un message :")
    
    ################ read Key ######################
    
    file_contain = os.path.join(path, "0c.txt")
    file = open(file_contain,'rt')
    key = file.read()
    
    ########## encrypt text with key file ##########
    
    code_text=code(text,key)
    
    ######### we get the prefix file and transform ######
    ########## it into alphabetic characters ############
    
    file_prefix = os.path.join(path , "0p.txt")
    file = open(file_prefix ,'rt')
    prefix = file.read()

    ord_prefix = ''
    for i in prefix:
        ord_prefix += chr(int(i) + ord('a'))
        
    ######### we get the suffix file and transform ######
    ########## it into alphabetic characters ############
    
    file_suffix = os.path.join(path , "0s.txt")
    file = open(file_suffix,'rt')
    suffix = file.read()

    ord_suffix = ''
    for i in suffix:
        ord_suffix += chr(int(i) + ord('a'))

    ########## we add to text encrypt prefix ############
    ########## and suffix to get file encrypt ###########
    
    encrypt_msg = ord_prefix + code_text + ord_suffix
    #with open(os.path.join(p, "dir-"+str(dir_name)+"-0t.txt"), 'w') as temp_file:
    a=path[-1:]
    with open(os.path.join(p, "dir-"+a+"-0t.txt"), 'w') as temp_file:
            temp_file.write(encrypt_msg)
            
    ########## remove contain file (key) ##########
    # remove file 00c
    #if os.path.exists(path , "0c.txt"):
        #os.remove('/path/0c.txt')


###############################################################################
                            # Receive mode #
###############################################################################
def decode(text, shift):
    # str, int --------> str
    
    data_decode = text [48 : -48]
    index=0
    text_decode=''
    for letter in data_decode:
        result = shift_letter(letter, -1 * int(shift[index]))
        index += 1
        text_decode += result
    return text_decode

def receive (file) :
    # File -----> File
    
    ############# get file to decrypt ############
    
    #transmission_code = os.path.join(p , "dir-"+str(dir_name)+"-0t.txt")
    transmission_code = os.path.join(p , file)
    file = open(transmission_code ,'rt')
    transmission = file.read()

    ############ open the first prefix file #################
    
    dir_number=0
    file_prefix1 = os.path.join(parent_dir , str(dir_number),"0p.txt")
    if os.path.exists(file_prefix1):
        file = open(file_prefix1 ,'rt')
        prefix1 = file.read()
        
    ########### regenerate the prefix file from ############
    ####### the file to decrypt (the first 48 bytes) #######
    
    prefix_data =""
    data = transmission [0:48]
    for i in data:
        prefix_data += str(ord(i) - ord('a'))
        
    ######### we check if it is equal to the file to #########
    ######### decrypt by browsing all the prefix files #######
    
    while prefix_data != prefix1:
        dir_number+=1
        file_prefix1 = os.path.join(parent_dir , str(dir_number),"0p.txt")
        if os.path.exists(file_prefix1):
            file = open(file_prefix1 ,'rt')
            prefix1 = file.read()

    ############ we recover the contain file which ##########
    ######## corresponds to the correct prefix file #########
    
    key_decode = os.path.join(parent_dir , str(dir_number),"0c.txt")
    if os.path.exists(key_decode):
        file = open(key_decode ,'rt')
        key1 = file.read()

    ############# decrypt and save file ###############

    decode_text=decode(transmission, key1)
    print('decrypt',decode_text)
    print('\n',p)

    with open(os.path.join(p, "dir-"+str(dir_number)+"-0m.txt"), 'w') as temp_file:
        temp_file.write(decode_text)
            
    ###### delete the file that contains the key ######
    # remove file 00c
    #if os.path.exists(path , "0c.txt"):
        #os.remove('/path/0c.txt')


    

parser = argparse.ArgumentParser()



parser.add_argument('-g' ,action="store_true", help='generate folders and files (prefix, content key, suffix)')
    
parser.add_argument('-s', action="store_true", help='encrypt text (input)')

parser.add_argument('-d', type= str , help='specify directory to encrypt') 
   
parser.add_argument('-r', action="store_true", help='decrypt file')
    
parser.add_argument('-f', type= str , help='name file to decrypt')

args = parser.parse_args()

if args.g:
    generate()
elif args.s:
    send(args.d)
elif args.r and args.f:
    receive(args.f)


        