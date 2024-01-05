from code22.code import test
from model.model import TierListInfo
from fastapi import APIRouter

router = APIRouter(prefix='/summoner')

@router.get(
    path='/tier',
    response_model=TierListInfo
)
def summoner_tier(
        riot_id:str,
        tag:str
) -> TierListInfo:
    return test(riot_id=riot_id, tag=tag)