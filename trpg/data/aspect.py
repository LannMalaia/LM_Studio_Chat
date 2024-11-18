from enum import Enum
from trpg.promptable import Promptable

class ASPECT_TYPE(Enum):
    """
        좋은 면모인지, 나쁜 면모인지를 결정한다.\n
        스트레스의 타격이나, 그런 부분에서 사용됨
    """
    POSITIVE = 1,
    NEGATIVE = 2,
    NONE = 0

class Aspect(Promptable):
    """
        면모\n
        캐릭터나 아이템이 가진 특징. 간단한 문구와, 그에 대한 설명으로 이어진다.
    """
    def __init__(self, title: str, desc: str, aspect_type: ASPECT_TYPE):
        self.title: str = ""
        self.desc: str = ""
        self.aspect_type: ASPECT_TYPE = ASPECT_TYPE.NONE
    
    def get_prompt(self):
        super.get_prompt()