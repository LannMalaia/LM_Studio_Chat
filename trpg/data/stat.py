from trpg.promptable import Promptable


class Stat(Promptable):
    """
        기능\n
        스테이터스의 힘민지 같은 거.\n
        모든 캐릭터가 이 기능을 통해서 행동할 수 있다.
    """
    def __init__(self):
        self.name: str = ""
        self.desc: str = ""
        self.examples: list = []
        self.min_lv: int = 0
        self.max_lv: int = 6
        pass

    # 해당 기능에 대하여 프롬프트로 표현한다.
    def get_prompt():
        result = ""

        return result