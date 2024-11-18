from abc import ABC, abstractmethod

from trpg.exception.prompt_not_ready_error import PromptNotReadyError

class Promptable(ABC):
    @abstractmethod
    def get_prompt(self):
        raise PromptNotReadyError()
