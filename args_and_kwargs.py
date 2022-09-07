# def test_arg(*args):
#     for arg in args:
#         print(arg)


# test_arg('hi',143,'Pratik')

def test_kwarg(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(key,value)

arg = [12,32,6]
kw = {'Name':'Pratik','age':25}
test_kwarg(*arg,**kw)



