from trpg.promptable import Promptable

class Skill(Promptable):
    """
        Ư��\n
        �� ĳ���͸��� �� �� �ִ� Ư���� ���.\n
        Ư�� ��Ȳ���� Ư�� �ൿ�� ���ʽ��� �ִ� ��.
    """

    def __init__(self) -> None:
        super().__init__()

    def get_prompt(self):
        return super().get_prompt()