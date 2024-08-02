from .error import Error

def test():
    e = Error()
    try:
        e.error2()
    except RuntimeError as exc:
        print("Captured the C++ error correctly")
