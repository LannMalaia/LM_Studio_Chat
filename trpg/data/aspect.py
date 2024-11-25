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
        일반 면모\n
        캐릭터나 아이템이 가진 특징. 간단한 문구와, 그에 대한 설명으로 이어진다.
    """
    def __init__(self, title: str, desc: str, aspect_type: ASPECT_TYPE = ASPECT_TYPE.NONE):
        self.title: str = title
        self.desc: str = desc
        self.aspect_type: ASPECT_TYPE = aspect_type
    
    def get_prompt(self):
        result = ""

        if ASPECT_TYPE == ASPECT_TYPE.POSITIVE:
            result += "(긍정적)"
        elif ASPECT_TYPE == ASPECT_TYPE.NEGATIVE:
            result += "(부정적)"
        
        result += f"{self.title}: {self.desc}"

        return result