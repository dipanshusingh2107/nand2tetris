import os
script_dir = os.path.dirname(__file__)

def Ainstruction(instruct):
    address = ""
    for i in instruct:
        if i=='@':
            continue
        elif i=='/':
            break
        else:
            address+=i
    
    digit = int(address)

    binary = []
    for i in range(15):
        binary.append(digit & 1)
        digit = digit>>1
    
    binary.append(0)
    binary.reverse()
    binary = [str(x) for x in binary ]
    return "".join(binary)


def Cinstruction(instruct):

    dest = ""
    comp = ""
    jump = ""

    for i in range(len(instruct)):
        if instruct[i] == '/':
            instruct = instruct[ :i]
            break
    
    if len(instruct) == 0:
        return

    indexofequal = -1
    indexofsemi = -1
    for i in range(len(instruct)):
        if instruct[i] == ';':
            jump = instruct[ i+1:]
            indexofsemi = i+1
            break
        if instruct[i] == '=':
            indexofequal = i
    
    if indexofequal == -1 and indexofsemi == -1:    # D
        comp = instruct
    elif indexofequal != -1 and indexofsemi != -1:  # D = M+A; JMP
        comp = instruct[indexofequal+1:indexofsemi-1]
        dest = instruct[:indexofequal]
    elif indexofequal != -1 and indexofsemi == -1:  #   D = M+A
        comp = instruct[indexofequal+1:]
        dest = instruct[:indexofequal]
    else:                                           # M+A;JMP
        comp = instruct[:indexofsemi-1]

    ans = "111"

    d1 ="0"
    d2 = "0"
    d3 = "0"
    a = '0'
    for i in comp:
        if i == 'M':
            a = '1'
    ans+= a

    if a == '0':
        compDict = dict({
            '0':'101010' , '1':'111111' ,'-1':'111010','D':'001100','A':'110000','!D':'001101',
            '!A':'110001','-D':'001111','-A':'110011','D+1':'011111','A+1':'110111','D-1':'001110',
            'A-1':'110010','D+A':'000010','D-A':'010011','A-D':'000111','D&A':'000000','D|A':'010101'
        })
        ans+= compDict[comp]
    else:
        compDict = dict({
            '0':'101010' , '1':'111111' ,'-1':'111010','D':'001100','M':'110000','!D':'001101',
            '!M':'110001','-D':'001111','-M':'110011','D+1':'011111','M+1':'110111','D-1':'001110',
            'M-1':'110010','D+M':'000010','D-M':'010011','M-D':'000111','D&M':'000000','D|M':'010101'
        })
        ans+= compDict[comp]

    for i in dest:
        if i == 'A':
            d1 = '1'
        elif i == 'D':
            d2 = '1'
        elif i == 'M':
            d3 = '1'

    ans+= (d1+d2+d3)


    if len(jump) == 0:
        ans+='000'
    else:
        JumpDict = dict({
            'JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'
        })
        ans+= JumpDict[jump]

    return ans


if __name__ == "__main__":

    path = input()
    print(path)
    abs_file_path = os.path.join(script_dir, path)
    f = open(abs_file_path,'r')
    lines = f.readlines()

    code = open("code.hack", "w") 
    
    for instruction in lines:
        instruction = instruction.strip()
        instruction = instruction.replace(" ","")
        if len(instruction) == 0:
            continue
        if(instruction[0] == '@'):
            x = Ainstruction(instruction) 
            if x != None:
                code.write(x+'\n')
            # print(Ainstruction(instruction))
        else:
            x = Cinstruction(instruction)
            if x != None:
                code.write(x+'\n')
            # print(Cinstruction(instruction))

        #print(instruction)
    
    f.close()
    code.close()