from trpg.promptable import Promptable

class Skill(Promptable):
    """
        특기\n
        그 캐릭터만이 할 수 있는 특별한 기술.\n
        특정 상황에서 특정 행동에 보너스를 주는 식.
    """

    def __init__(self) -> None:
        super().__init__()

    def get_prompt(self):
        return super().get_prompt()