#IMPORT SECTION
import re
import typing
import collections

#INPUT HANDLING
with open('Day19/input.txt') as file:
    data = file.read().split('\n')

#FUNCIONS AND VARIABLES
regex = re.compile(r'Each (\w+) robot costs (\d+) (\w+)(?: and (\d+) (\w+))?\.') # thanks OPENAI

def count(strings: tuple[str,...]) -> dict[str,int]:
    retenue: dict[str,int] = {}
    for string in strings:
        retenue.setdefault(string,0)
        retenue[string] += 1
    return retenue

def add(*ms: typing.Mapping[str,int]) -> dict[str,int]:
    retenue: dict[str,int] = {}
    for m in ms:
        for key, value in m.items():
            retenue.setdefault(key,0)
            retenue[key] += value
    return retenue

def purchasable(res: typing.Mapping[str,int],cost: typing.Mapping[str,int]) -> bool:
    return all(res.get(key,0) >= value for key, value in cost.items())

def nega(cost: typing.Mapping[str,int]) -> dict[str,int]:
    return {key: -value for key, value in cost.items()}

class Cost(typing.NamedTuple):
    geo_bot_ore: int
    geo_bot_obs: int
    ore_bot_ore: int
    cla_bot_ore: int
    obs_bot_ore: int
    obs_bot_cla: int
    
#PART-1
def main(items: list[tuple[str, str, str, str, str]]) -> int:
    costs: dict[str,dict[str,int]] = collections.defaultdict(dict)
    for bot_key, n1, cost2, n2, cost3 in items:
        costs[bot_key][cost2] = int(n1)
        if n2:
            costs[bot_key][cost3] = int(n2)
    cost = Cost(
        geo_bot_ore=costs['geode']['ore'],
        geo_bot_obs=costs['geode']['obsidian'],
        ore_bot_ore=costs['ore']['ore'],
        cla_bot_ore=costs['clay']['ore'],
        obs_bot_ore=costs['obsidian']['ore'],
        obs_bot_cla=costs['obsidian']['clay'],
    )

    maxo = max(
        cost.obs_bot_ore,
        cost.ore_bot_ore,
        cost.cla_bot_ore,
        cost.geo_bot_ore,
    )

    visited = set()
    best: dict[int,int] = {}
    todo = collections.deque([(0, 1, 0, 0, 0, 0, 0, 0, 0)])
    while todo:
        m, ore_b, cla_b, obs_b, geo_b, ore, cla, obs, geo = todo.popleft()
        ore = min(maxo * (24-m), ore)
        cla = min(cost.obs_bot_cla * (24-m), cla)
        obs = min(cost.geo_bot_obs * (24-m), obs)
        ore_b = min(ore_b, maxo)
        cla_b = min(cla_b, cost.obs_bot_cla)
        geo_b = min(geo_b, cost.geo_bot_obs)
        
        tupl = (m,ore_b,cla_b,geo_b,ore,cla,obs,geo)
        if tupl in visited:
            continue
        else:
            visited.add(tupl)
        
        best[m] = max(best.get(m,0),geo)
        
        if m == 24:
                continue
            
        if ore >= cost.ore_bot_ore and obs >= cost.geo_bot_obs:
            todo.apped((
                m+1,
                ore_b,
                cla_b,
                obs_b,
                geo_b +1,
                ore + ore_b - cost.geo_bot_ore,
                cla + cla_b,
                obs + obs_b - cost.geo_bot_obs,
                geo + geo_b,
            ))
            continue
        
        if ore >= cost.cla_bot_ore and cla >= cost.geo_bot_cla:
            todo.append((
                m +1,
                ore_b,
                cla_b,
                obs_b + 1,
                geo_b,
                ore + ore_b - cost.obs_bot_ore,
                cla + cla_b - cost.obs_bot_cla,
                obs + obs_b,
                geo + geo_b,
            ))
            
        if ore >= cost.cla_bot_ore:
            todo.append((
                m + 1,
                ore_b,
                cla_b + 1,
                obs_b,
                geo_b,
                ore + ore_b - cost.cla_bot_ore,
                cla + cla_b,
                obs + obs_b,
                geo + geo_b,
            ))
        
        if ore >= cost.ore_bot_ore:
            todo((
                m + 1,
                ore_b + 1,
                cla_b,
                obs_b,
                geo_b,
                ore + ore_b - cost.ore_bot_ore,
                cla + cla_b,
                obs + obs_b,
                geo + geo_b,
            ))
        
        todo.append((
                m + 1,
                ore_b,
                cla_b,
                obs_b,
                geo_b,
                ore + ore_b,
                cla + cla_b,
                obs + obs_b,
                geo + geo_b,
            ))
        print(best)
        return(best[24])
    
    
returnval = 0 
for i, line in enumerate(data,1):
    res = main(regex.findall(line))
    returnval += i * res
print(res)