def evaluate(exp: Expression, env: Environment) -> Any:
    "Evaluate an expression in an environment."
    if isinstance(exp, Symbol): # variable reference
        return env[exp]
    # ... lines omitted
    elif exp[0] == 'quote': # (quote exp)
        (_, x) = exp
        return x
    elif exp[0] == 'if': # (if test conseq alt)
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda': # (lambda (parm…) body…)
        (_, parms, *body) = exp
        return Procedure(parms, body, env)
    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)

# Python 3.10
# def evaluate(exp: Expression, env: Environment) -> Any:
#     "Evaluate an expression in an environment."
#     match exp:
#     # ... lines omitted
#     case ['quote', x]:
#         return x
#     case ['if', test, consequence, alternative]:
#         if evaluate(test, env):
#             return evaluate(consequence, env)
#         else:
#             return evaluate(alternative, env)
#     case ['lambda', [*parms], *body] if body:
#         return Procedure(parms, body, env)
#     case ['define', Symbol() as name, value_exp]:
#         env[name] = evaluate(value_exp, env)
#     # ... more lines omitted
#     case _:
#         raise SyntaxError(lispstr(exp))