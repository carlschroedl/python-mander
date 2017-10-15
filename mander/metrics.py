"""
The representational fairness measure, or partisan differential,
is absolute value of the number of districts where the partisan
index for a one party is above 50% minus the number of districts
where the partisan index for the other party is above 50%

The Democratic Partisan Index is the number of democratic 
votes divided by the combined number of democratic and republican 
votes. The Republican Partisan Index is the number of republican 
votes divided by the combined number of democratic and republican 
votes.

When passed a plan, this calculator will compute the
representational fairness for all districts in the plan.
The result is a tuple with - the first item is the differential
and the second item is the party toward which the plan's 
districts are biased
"""
def representational_fairness(plan):
    """
    Compute the representational fairness.

    @param plan: A L{Plan} whose set of districts should be 
        evaluated for representational fairness.
    """
    districts = plan.get_districts()
    
    dems = 0
    reps = 0
    for district in districts:
        #hardcoded attributes for now
        dem = district.democratic
        rep = district.republican
        if dem is None or rep is None:
            continue

        dem = float(dem)
        rep = float(rep)

        if dem == 0.0 and rep == 0.0:
            continue

        dem_pi = dem / (rep + dem)
        if dem_pi > .5:
            dems += 1
        else:
            rep_pi = rep / (rep + dem)
            if rep_pi > .5:
                reps += 1

    result = dems - reps
    return result
