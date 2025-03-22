def memory_mib(df):
    return f'{df.memory_usage(deep=True).sum() / 1024 ** 2: .2f} MiB'
