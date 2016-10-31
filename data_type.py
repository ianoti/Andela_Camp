def data_type(argument):
  if type(argument) == str:
    return len(argument)
  elif argument is None:
    return "no value"
  elif type(argument) == bool:
    return argument
  elif type(argument) == int:
    if argument < 100:
      return "less than 100"
    elif argument == 100:
      return "equal to 100"
    elif argument > 100:
      return "more than 100"
  elif type(argument) == list:
    if len(argument) >= 3:
      return argument[2]
    else:
      return None
  elif type(argument) != list and type(argument) != int and type(argument) != bool and type(argument) != str:
    return "Function can't evaluate that, confirm input is a string, boolean, integer or list"
    