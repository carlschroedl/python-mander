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


"""
Compute the plan's Competitiveness.

Competitiveness is defined here as the number of districts that 
have a partisan index (democratic or republican) that falls within
a desired range of .5 (by default).

"""
def competitiveness(plan, range=0.5):
    """
    Compute the competitiveness.

    @param plan: A L{Plan} whose set of districts should be 
        evaluated for competitiveness.
    """
    districts = plan.get_districts()
    low = .5 - range 
    high = .5 + range

    fair = 0
    for district in districts:
        if district.district_id == 0:
            continue

        tmpdem = district.democratic
        tmprep = district.republican

        if tmpdem is None or tmprep is None:
            continue

        dem = float(tmpdem)
        rep = float(tmprep)

        if dem == 0.0 and rep == 0.0:
            continue

        pidx = dem / (dem + rep)
        if pidx > low and pidx < high:
            fair += 1

    return fair


"""
This calculator determines how many times a district splits a given collection of features.
"""
def count_splits(district, features):
    """
    Calculate splits between a district and other features.

    @keyword district: A L{District} whose splits should be computed.
    @keyword boundary_id: The ID of the geolevel to compare for splits.
    """
    if district.geom.empty:
        return
    # https://toblerity.org/shapely/manual.html#de-9im-relationships
    #todo: https://en.wikipedia.org/wiki/DE-9IM
    #'***T*****'
    num_splits = -1

    return num_splits

"""
Calculate the ratio of the area of a district to the area of its convex hull.

This calculator will either calculate a single district's convex hull ratio,
or the average convex hull ratio of all districts.
"""
def convex_hull_ratio(**kwargs):
    """
    Calculate the convex hull ratio of a district or a plan.

    @keyword district: A L{District} whose convex hull ratio should be 
        computed.
    @keyword plan: A L{Plan} whose district convex hull ratios should be 
        averaged.
    """
    districts = []
    if 'district' in kwargs:
        districts = [kwargs['district']]
        if districts[0].geom.empty:
            return

    elif 'plan' in kwargs:
        plan = kwargs['plan']
        districts = plan.get_districts()

    else:
        return

    num = 0
    ratios = 0.0
    for district in districts:
        if district.geom.empty or district.geom.length == 0 or district.district_id == 0:
            continue

        ratios += district.geom.area / district.geom.convex_hull.area
        num += 1

    result = (ratios / num) if num > 0 else 0
    return result
