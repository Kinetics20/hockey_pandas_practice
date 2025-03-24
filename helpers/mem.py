def memory_mib(df):
    return f'{df.memory_usage().sum() / 1024 ** 2:.2f} MiB'