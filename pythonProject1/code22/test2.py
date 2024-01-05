import requests
from model.model import TierInfo, TierListInfo
import random


# 참조->
def get_tier(queue, tier, division, lp) -> TierInfo:
    return TierInfo(
        queue=queue,
        tier=tier,
    division = division,
    lp = lp
    )

def test(tier: str,
             division: str
             ):
        api_key = 'RGAPI-bfce5f5d-df88-492d-a316-712d9a8fe9ba'

        url1 = f'https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}?page=1&api_key={api_key}'
        # f 포멧팅 해주고 ,아이디 {},태그{},API{}
        res = requests.get(url1).json()
        r_res = random.choices(res, k=5)


        tier_list = []
        for league in r_res:
            if league['queueType'] == 'RANKED_SOLO_5x5':
                queue = league['queueType']
                solo_rank_tier = league['tier']
                solo_rank_division = league['rank']
                solo_rank_lp = league['leaguePoints']
                tier = get_tier(queue, solo_rank_tier, solo_rank_division, solo_rank_lp)
                tier_list.append(tier)
            elif league['queueType'] == 'RANKED_FLEX_SR':
                queue = league['queueType']
                flex_rank_tier = league['tier']
                flex_rank_division = league['rank']
                flex_rank_lp = league['leaguePoints']
                tier = get_tier(queue, flex_rank_tier, flex_rank_division, flex_rank_lp)
                tier_list.append(tier)
        return TierListInfo(
                total_tier_list=tier_list
            )