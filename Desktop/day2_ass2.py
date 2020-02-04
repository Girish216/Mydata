def encode(message):
    output,temp,count=[],message[-1],1
    for i in range(len(message)-2,-2,-1):
        if message[i]!=temp or i==-1:
            output.insert(0,temp)
            output.insert(0,str(count))
            count=1
            temp=message[i]
        else:
            count+=1
    return "".join(output)
encoded_message=encode(input())
print(encoded_message)
            
            
        
        
