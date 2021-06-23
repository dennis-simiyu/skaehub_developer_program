import statistics
import stat
def list_stats():
    team_list = ['chelsea', 'liverpool', 'machester_city', 'arsenal', 'totenhame', 'westham', 'fulham']
    eAfrica_countries_gdp = [2000, 4000, 6000,10000,4000]
    eAfrica_countries = ["Uganda", "Rwanda", "Burundi", "Kenya", "Tanania"]
    #median gdp
    statistics.median(eAfrica_countries_gdp)
    #mode gdp
    statistics.mode(eAfrica_countries_gdp)
    #reverse the list
    team_list.reverse()
    print(team_list)
    #sort the list
    team_list.sort()
    print(team_list)
    #print the len of the list
    print(len(team_list))
    #create a dictionary from the list comprised of the name of the team as the key and its lenght of characters as the values
    dict_list = {}
    
    for i in team_list:
        v = {i:len(i)}
        dict_list.update(v) 
        
    print(dict_list)
    
    



list_stats()