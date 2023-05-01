import os
import argparse
import random

import numpy as np
import tensorflow as tf
from PIL import Image

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


def resize(np_image, width, height):
    pil_image = Image.fromarray(np_image)
    resize_pil_image = pil_image.resize((width, height))
    return np.asarray(resize_pil_image)


def dump(output_file_path, x, y, sample_num, image_max_size, image_min_size):
    with open(output_file_path, mode='w') as f:
        for index in range(sample_num):
            mnist_index = random.randint(0, y.shape[0] - 1)
            resize_np_image = resize(x[mnist_index], random.randint(image_min_size, image_max_size), random.randint(image_min_size, image_max_size))
            input_text = str(resize_np_image).replace('\n', '').strip()
            output_text = str(y[mnist_index]).replace('\n', '').strip()
            f.write(f'input: {input_text} ? output: {output_text}\n')


def parse(output_file_path, train_sample_num, test_sample_num, image_max_size, image_min_size):
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    file_path, ext = os.path.splitext(output_file_path)
    output_train_file_path = os.path.join(f'{file_path}_train{ext}')
    dump(output_train_file_path, x_train, y_train, train_sample_num, image_max_size, image_min_size)

    file_path, ext = os.path.splitext(output_file_path)
    output_valid_file_path = os.path.join(f'{file_path}_valid{ext}')
    dump(output_valid_file_path, x_test, y_test, test_sample_num, image_max_size, image_min_size)


def main():
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--output_file_path', type=str, default='~/.vaik-mnist-text-dataset/dataset/mnist.txt')
    parser.add_argument('--train_sample_num', type=int, default=10000)
    parser.add_argument('--test_sample_num', type=int, default=100)
    parser.add_argument('--image_max_size', type=int, default=28)
    parser.add_argument('--image_min_size', type=int, default=28)
    args = parser.parse_args()

    args.output_file_path = os.path.expanduser(args.output_file_path)

    parse(**args.__dict__)


if __name__ == '__main__':
    main()
