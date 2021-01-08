1. What is it?
----------------
The sender and receiver each have one of the copies.
When you send a message, you take each number in the message and “shift” it to the corresponding number in the random sequence, just as you would a silent Caesar number. The exhausted random sequence is then destroyed so that it cannot be reused. On receipt, the only remaining copy of the random sequence is used to cancel the resulting offset from the clear text message, after which it is also shredded.

2. How to use it?
-------------------
you must change the directory or your files will be saved.
we will generate the pad we use the following shell command

   >>> python main.py -g

to encrypt a message (read from standard input), use the following command you can specify the pad number used to encrypt for example (dev / random / 0000)

   >>> python main.py -s -d \ [UAPV-SEC] _..._ TP3 \ dev \ random \ 0
   
we find the decrypt message in the dir-0-0t.txt file
to decrypt a message, you must specify the name of the file.

    >>> python main.py -r -f dir-0-0t.txt
    
we find the decrypt message in the dir-0-0m.txt file