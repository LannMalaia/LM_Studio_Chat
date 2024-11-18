from trpg.promptable import Promptable


class Aspect(Promptable):
    """
        면모
        캐릭터나 아이템이 가진 특징. 간단한 문구와, 그에 대한 설명으로 이어진다.
    """
    def __init__(self):
        self.title: str = ""
        self.desc: str = ""
    
    def get_prompt(self):
        super.get_prompt()