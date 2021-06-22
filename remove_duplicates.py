def removeDuplicates():
    unfiltered_list= ['denis', 'humphrey','john','dennis','john']
    filtred_list = []
    for name in unfiltered_list:
        if name not in filtred_list:
            filtred_list.append(name)
            
    return filtred_list
    
print(removeDuplicates())