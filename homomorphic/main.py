import argparse

import numpy as np
from PIL import Image

import homomorphic


def main():
    parser = argparse.ArgumentParser(description="Homomorphic filtering demo.")

    parser.add_argument(
        '--alpha',
        metavar='float',
        type=float,
        help="Variable alpha. Default is 0.75",
        default=0.75)

    parser.add_argument(
        '--beta',
        metavar='float',
        type=float,
        help="Variable beta. Default is 1.25",
        default=1.25)

    parser.add_argument(
        '--filter',
        metavar='str',
        type=str,
        help="Filter to use. Either 'butterworth' or 'gaussian'. Default is 'butterworth'",
        default='butterworth')

    parser.add_argument(
        '--cutoff-freq',
        metavar='float',
        type=float,
        help="Cutoff frequency. Default is 30",
        default=30)

    parser.add_argument(
        '--order',
        metavar='float',
        type=float,
        help="Filter order, only used butterworth filter. Default is 2",
        default=2)

    parser.add_argument('imgpath', metavar='imgpath', type=str, help="Input image file")

    args = parser.parse_args()

    img = Image.open(args.imgpath)
    if img.mode == 'RGB':
        img = img.convert('L')
    img = np.asarray(img, dtype=np.uint8)

    img = homomorphic.apply(
        img,
        alpha=args.alpha,
        beta=args.beta,
        filter_type=args.filter,
        cutoff_freq=args.cutoff_freq,
        order=args.order)

    Image.fromarray(img).show()

if __name__ == "__main__":
    main()
