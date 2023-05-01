# vaik-mnist-text-dataset

Create MNIST text dataset

## Example

![vaik-mnist-text-dataset](https://user-images.githubusercontent.com/116471878/235404955-4b4fbf1c-fed0-4911-8d72-4d899f526d2c.png)


## Usage

```shell
pip install -r requirements.txt
python main.py --output_file_path ~/.vaik-mnist-text-dataset/dataset/mnist.txt \
                --train_sample_num 10000 \
                --test_sample_num 100 \
                --valid_sample_num 100 \
                --image_max_size 28 \
                --image_min_size 28
```

## Output

```shell
cat ~/.vaik-mnist-text-dataset/dataset/mnist_train.txt
#input: [[  0   ・・・  17 219 160  ・・・   0   0]] ? output: 9
#input: [[  0   ・・・  83 213 177  ・・・   0]] ? output: 8
#input: [[  0   ・・・  13 133 212  ・・・   0]] ? output: 7
cat ~/.vaik-mnist-text-dataset/dataset/mnist_valid.txt
#input: [[  0   ・・・  84 193 130  ・・・   0   0]] ? output: 1
#input: [[  0   ・・・  81 175 217  ・・・   0]] ? output: 3
#input: [[  0   ・・・  23 194 123  ・・・   0]] ? output: 2
```