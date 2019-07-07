def number_error_handling(comein):
    try:
        comein = int(comein)
    except IOError:
        return 0
    except ValueError as a:
        return 0
    except:
        return 0
    else:
        return comein
        
