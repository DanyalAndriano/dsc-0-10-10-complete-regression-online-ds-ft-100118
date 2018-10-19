def calc_slope(xs,ys):
    meanxs = sum(xs)/len(xs)
    meanys = sum(ys)/len(ys)
    xy = [a*b for a, b in list(zip(xs, ys))]
    xs_sqr = [i * i for i in xs]
    return (meanxs * meanys - (sum(xy)/len(xy))) / (meanxs**2 - (sum(xs_sqr)/len(xs_sqr)))

def best_fit(xs,ys):
    mean_y = sum(ys)/len(ys)
    mean_x = sum(xs)/len(xs)
    m = calc_slope(xs,ys)
    b = mean_y - (m*mean_x)
    return m, b

def reg_line (m, b, xs):
    y = [m*x + b for x in xs]
    return y

def sq_err(ys_a, ys_b):
    sqr_error = [(a - b)**2 for a, b in list(zip(ys_a, ys_b))]
    return sum(sqr_error)

def r_squared(ys_real, ys_predicted):
    ys_mean = sum(ys_real)/len(ys_real)
    ssr = sq_err(ys_real, ys_predicted)
    sst = [(a - ys_mean)**2 for a in ys_real]
    return 1 - (ssr/sum(sst))
