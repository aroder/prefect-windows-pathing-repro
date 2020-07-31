import prefect

@prefect.task
def hello():
    print('hello')

with prefect.Flow('prefect windows pathing repro') as flow:
    hello()
