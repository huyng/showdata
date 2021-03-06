def bar(x, y=None, title='', xlabel='', ylabel=''):
    import pylab as P
    import numpy as np
    L = (tuple, list, np.ndarray)

    # separate arrays
    if isinstance(x,L) and isinstance(y,L):
        xylist = zip(x,y)
    # list of two-tuples
    elif isinstance(x, L) and isinstance(x[0], L) and len(x[0]) == 2:
        xylist = x
    else:
        raise TypeError

    P.figure(figsize=(10, 5)) # image dimensions   
    P.title(title, size='medium')
    P.xlabel(xlabel)
    P.ylabel(ylabel)
    
    # add bars
    for i, item in enumerate(xylist): 
        P.bar(i + 0.25 , item[1])
    
    # set ylim
    height = np.max(zip(*xylist)[1])
    P.ylim(0, height*1.1)

    # axis setup
    P.xticks(np.arange(0.65, len(xylist)),  ['%s' % x for x,y in xylist], size='medium')

data = [("a", 1), ("b", 2), ("c", 3)]
bar(data)
raw_input('press ENTER to exit')
