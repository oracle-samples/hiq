# Author: Henry Fuheng Wu
# Inside a class function actually
global __author__
__author__ = "Henry Fuheng Wu"

@s.inserter
def {tag}({signature}):
    _r = None
    try:
        _r = s.o_{tag}({spec_wo_default})
        🐚
        """
        __co_name = inspect.stack()[0][0].f_code.co_name
        if '__ior' == __co_name:
            s.dio_bytes_r += len(_r)
        elif '__nio_get' == __co_name:
            s.nio_bytes_r += len(_r.content) if (_r and _r.status_code < 400) else 0
        """
        return _r
    except Exception as e:
        if s.verbose:
            print(traceback.format_exc())
        #if s.pop_exception:
        #    print("exception happens at {tag}")
        #    raise e
        raise e
    #finally:
    #    return _r

try:
    if is_hiqed(hiq.mod('{module_name}').{_class_name}.{_funct_name}, "{_funct_name}"):
        msg = (
            "🅳 {module_name}.{_class_name}.{_funct_name} cannot be hiqed twice. "
            "Please check your hiq table."
        )
        raise HiQException(msg)
    else:
        pass
        # print(f"{_funct_name} is not hiqed")
    if "{module_name}.{_class_name}.{_funct_name}" in HIQ_C_SET:
        s.o_{tag} = s.enable_c('{module_name}', "{_class_name}", "{_funct_name}", {tag})
    else:
        #print("{module_name}.{_class_name}.{_funct_name}")
        #print(hiq.mod('{module_name}').{_class_name}.{_funct_name}, '=>' ,{tag})
        hiq.mod('{module_name}').{_class_name}.{_funct_name} = {tag}
except TypeError as e:
    try:
        s.o_{tag} = s.enable_c('{module_name}', "{_class_name}", "{_funct_name}", {tag})
    except Exception as e:
        if s.verbose:
            print(traceback.format_exc())

# print("💧", s)
###############################################################################
