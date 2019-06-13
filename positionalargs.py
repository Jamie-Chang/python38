# PEP 570: Postional only arguments
import math

########################################################################

# RECAP


def kwarg_only_function(*, a, b):
    print(a, b)


kwarg_only_function(1, 2)
kwarg_only_function(a=1, b=2)

########################################################################

print(math.log(5))
print(math.log(5, math.e))

print(math.log(5, base=math.e))  # doesn't work...

help(math.log)

########################################################################

# Attempt 1, argument defaults


def log(x, base=math.e):
    return math.log(x, base)

log(1)
log(1, 2)
log(1, base=2)  # shouldn't work

########################################################################

# Attempt 2, use *args


def log(*args):
    base = math.e
    if (length := len(args)) == 1:
        x, = args
    elif length == 2:
        x, base = args
    else:
        raise TypeError(f"math.log requires 1 to 2 arguments got {length}")
    return math.log(x, base)

log(1)
log(1, 2)
log(1, base=2)  # shouldn't work

########################################################################

# Finally, positional args


def log(x, base=math.e, /):
    return math.log(x, base)


log(1)
log(1, 2)
log(1, base=2)  # No longer works
