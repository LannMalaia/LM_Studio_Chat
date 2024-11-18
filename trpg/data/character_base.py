
from .stat import Stat
from trpg.promptable import Promptable


class Character_Base(Promptable):
    """
        모든 캐릭터들의 베이스
    """
    def __init__(self):
        self.name: str
        self.hit_stress: int
        self.mind_stress: int
        self.fate_point: int
        self.max_hit_stress: int
        self.max_mind_stress: int
        self.max_fate_point: int
        self.aspects: list[str] = []
        self.stats: list[Stat]
    
    def get_prompt(self):
        return super().get_prompt()