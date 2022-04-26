# Own generator. Please, don't punish me :(
def generator(start=0, end=0, step=1):
    if step == 0:
        raise ValueError("generator() arg 3 must not be zero")
    if start > end:
        if step < 0:
            while start > end:
                yield start
                start += step
        else:
            while end < start:
                yield end
                end += step
    elif start == 0 and end != 0:
        if end > 0:
            if step > 0:
                while start < end:
                    yield start
                    start += step
    elif start != 0 and end == 0:
        while end < start:
            yield end
            end += step
    elif start != 0 and end != 0:
        if start < end:
            if step > 0:
                while start < end:
                    yield start
                    start += step

# this is refactored code) 
def own_range(start=0, end=0, step=1):
	if step == 0:
		raise ValueError("own_range() arg 3 must be not zero")
	if start > end and step < 0:
		while start > end:
			yield start 
			start += step
	elif start > end or (start != 0 or end == 0) and start != 0 and end == 0:
		while end < start:
			yield end
			end += step
	elif start == 0 and end != 0 and end > 0 and step > 0 or (start != 0 or end == 0) and start != 0 and start < end and step > 0:
		while start < end:
			yield start
			start += step
