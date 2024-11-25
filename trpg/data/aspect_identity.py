from .aspect import ASPECT_TYPE, Aspect

class Aspect_Identity(Aspect):
    """
        정체성 면모
        캐릭터나 아이템을 대표하는 단 하나의 특징.
    """
    def __init__(self, title: str, desc: str):
        super().__init__(title, desc, ASPECT_TYPE.NONE)

    def get_prompt(self):
        return f"{self.title}: {self.desc}"