from trpg.data.aspect import Aspect


def list_to_numbered_list_str(arr: list[str]):
    result = ""
    for i in range(len(arr)):
        s = arr[i]
        result += ("\n" if i > 0 else "") + f"{i + 1}. {s}"
    return result

def list_to_numbered_list_aspect(arr: list[Aspect]):
    result = ""
    for i in range(len(arr)):
        s = arr[i].get_prompt()
        result += ("\n" if i > 0 else "") + f"{i + 1}. {s}"
    return result