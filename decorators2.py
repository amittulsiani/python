def wrap_with_prints(fn):
    # This will only happen when a function decorated
    # with @wrap_with_prints is defined
    print('wrap_with_prints runs only once \n')
 
    def wrapped():
        # This will happen each time just before
        # the decorated function is called
        print('About to run %s' % fn.__name__, "\n")
        # Here is where the wrapper calls the decorated function
        fn()
        # This will happen each time just after
        # the decorated function is called
        print('Done running %s' % fn.__name__, "\n")
 
    return wrapped
 
@wrap_with_prints
def func_to_decorate():
    print('Running the function that was decorated.\n')
 
func_to_decorate()
