def fizzBuzz(n: int) -> List[str]:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return list(str(n))
    

def generate_data(size):
    numbers = [*range(*size)]
    results = list(map(fizzBuzz, [*range(*size)]))
    return results


def prepare_data(data):
    import pandas as pd
    clean_data = [n[0]  if isinstance(n, list) else n for n in data]
    df = pd.DataFrame(clean_data)
    df.columns = ['result']
    df['result'] = df['result'].apply(lambda row: 'numbers' if str(row).isdigit() else row)

    return df



def visualize_data(df, col: str):
    # Count the occurrences of each unique value in the column
    value_counts = df[col].value_counts().reset_index()

    # Rename the columns for clarity
    value_counts.columns = ['Value', 'Count']

    # Count the occurrences of each unique value in the column
    value_counts = df[col].value_counts().reset_index()

    # Rename the columns for clarity
    value_counts.columns = ['Value', 'Count']

    # Create a bar chart using Plotly Express with color
    fig = px.bar(value_counts, x='Value', y='Count', color='Value',
                labels={'Value': 'FizzBuzz Result', 'Count': 'Count'},
                title='FizzBuzz Result Counts with Color')

    fig.show()

if __name__ == "__main__":
    size = (1, 15 + 1)
    data = generate_data(size)
    df = prepare_data(data)
    visualize_data(df, 'result')

