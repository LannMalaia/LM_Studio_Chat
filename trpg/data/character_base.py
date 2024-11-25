
from trpg.data.aspect import Aspect
from trpg.data.aspect_identity import Aspect_Identity
import utils
import utils.list_to_numbered_list_str
from .stat import Stat
from trpg.promptable import Promptable


class Character_Base(Promptable):
    """
        모든 캐릭터들의 베이스
    """
    def __init__(self):
        self.name: str
        self.identity: Aspect_Identity = Aspect_Identity()
        self.aspects: list[Aspect] = []
        self.stats: list[Stat]
        self.hit_stress: int
        self.mind_stress: int
        self.fate_point: int
        self.max_hit_stress: int
        self.max_mind_stress: int
        self.max_fate_point: int
        self.skills: list[str]
    
    def get_prompt(self):
        result = f"""
        [이름]
         {self.name}
        [정체성 면모]
         {self.identity}
        [면모]
        {utils.list_to_numbered_list_str.list_to_numbered_list_aspect(self.aspects)}
        기능:
        [현재 운명점]
         {self.fate_point}
        [현재 신체 스트레스]
         {self.hit_stress}
        [현재 정신 스트레스]
         {self.mind_stress}
        [최대 운명점]
         {self.max_fate_point}
        [최대 신체 스트레스]
         {self.max_hit_stress}
        [최대 정신 스트레스]
         {self.max_mind_stress}
        """
        return result