def run_bounded(operation,limit:int=2):
 if limit<1 or limit>5:raise ValueError('Bad attempt budget')
 for attempt in range(limit):
  try:return {'status':'completed','result':operation(),'attempts':attempt+1}
  except TimeoutError:
   if attempt+1==limit:return {'status':'failed','reason':'timeout','attempts':limit}
 raise RuntimeError('Unreachable')
