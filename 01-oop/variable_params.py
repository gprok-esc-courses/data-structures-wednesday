
def test_params(value, *args, **kwargs):
    print(value)
    print(args)
    print(kwargs)


test_params(10, color="blue", size="SM", price=103.12)