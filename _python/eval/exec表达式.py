import types




if __name__ == "__main__":
    module_code = compile(
        '''def foobar(): 
            result = "foo"
            result = result + "bar"
            for i in range(5):
                result = result + str(i)
            return result
        ''',
        '',
        'exec')
    function_code = [c for c in module_code.co_consts if isinstance(c, types.CodeType)][0]
    foobar = types.FunctionType(function_code, {})
    print(foobar())

    # module_code2 = compile(
    #     '''def goobar():
    #         return foobar()
    #     ''',
    #     '',
    #     'exec')
    # function_code2 = [c for c in module_code2.co_consts if isinstance(c, types.CodeType)][0]
    # goobar = types.FunctionType(function_code2, {})
    # print(goobar())

