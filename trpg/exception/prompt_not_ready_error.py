class PromptNotReadyError(Exception):
    def __init__(self):
        self.msg = "프롬프트화에 실패했어요. get_prompt(self)를 제대로 구현했는지 확인!"
    
    def __str__(self):
        return self.msg
    