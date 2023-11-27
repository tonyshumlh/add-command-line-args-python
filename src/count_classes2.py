import pandas as pd
import click

@click.command()
@click.argument('input_data', type=str)
@click.argument('col', type=str)
@click.argument('output_dir', type=str)

def main(input_data, col, output_dir):
    # read in data
    data = pd.read_csv(f'data/{input_data}')

    result = data.groupby(col).size().reset_index(name='Count')
    result = result.rename(columns={col: 'Class'})

    result.to_csv(f'results/{output_dir}/class_count.csv', index=False)

if __name__ == "__main__":
    main()

# python src/count_classes2.py agaricus-lepiota.csv mushroom-class mushroom
