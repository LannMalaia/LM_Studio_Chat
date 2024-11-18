from trpg.data.stat import Stat


class StatManager:
    """
        기능 매니저
        게임 내에서 쓰이는 기능들을 관리
    """
    def __init__(self):
        self._stats: list[Stat] = []
        
    def get_stat(self, name: str):
        for stat in self._stats:
            if stat.name == name:
                return stat
        raise ValueError(f"{name}이라는 기능은 없습니다!")

    def get_description_prompt(self):
        """
            각 기능들에 대해 이름과 설명등을 써서 문서화한다.\n
            이 때 어떻게 해야하지? 하는 순간에 기능을 추천받거나 할 때 좋다.
        """
        return ""