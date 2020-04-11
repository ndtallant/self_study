def gale_shapley(hospitals, residents):
    '''Finds stable matching of bipartite graph made of 
    sets u and v, given their preferences.'''

    unmatched_hospitals = list(hospitals.keys())
    matchings = {}

    while unmatched_hospitals:
        hospital = unmatched_hospitals.pop(0)
        resident = hospitals[hospital].pop(0)

        if resident not in matchings.keys():
            matchings[resident] = hospital
        
        res_match = matchings[resident]
        res_preferences = residents[resident]
        if res_preferences.index(hospital) < res_preferences.index(res_match):
            unmatched_hospitals.append(res_match)
            matchings[resident] = hospital

    return matchings 

if __name__ == "__main__":

    hospitals = {
        "UChicago": ["Erin", "Sue"],
        "Laurie": ["Erin", "Sue"]
    }

    residents = {
        "Erin": ["Laurie", "UChicago"],
        "Sue": ["Laurie", "UChicago"]
    }

    print(gale_shapley(hospitals, residents))
