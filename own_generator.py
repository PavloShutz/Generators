# Own generator. Please, don't punish me :(
def generator(end, start=0, step=1):
    while start < end:
        yield start
        start += step
