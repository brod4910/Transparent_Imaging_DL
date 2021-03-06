import argparse

def ArgsParserRecon():
    parser = argparse.ArgumentParser(description='Transparent Camera Reconstruction Pytorch')

    parser.add_argument('--epochs', type=int, default=40, metavar='N',
                    help='number of epochs to train (default: 40)')
    parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate (default: 0.01)')
    parser.add_argument('--batch-size', type=int, default=1, metavar='LR',
                    help='batch size (default: 1)')
    parser.add_argument('--log-interval', type=int, default=1000, metavar='N',
                    help='how many batches to wait before logging training status')
    parser.add_argument('--resize', required= True, type=int, default=None, 
                    help='dimensions of both height and width to be resized')
    parser.add_argument('--train-csv',
                    help='path to the img names for input images and gt images (names should match)')
    parser.add_argument('--val-csv',
                    help='path to the img names for input images and gt images (names should match)')
    parser.add_argument('--train-input-dir', default=None, 
                    help='path to training input image')
    parser.add_argument('--train-gt-dir', default=None, 
                    help='path to training ground truth images')
    parser.add_argument('--val-input-dir', default=None, 
                    help='path to validation input image')
    parser.add_argument('--val-gt-dir', default=None, 
                    help='path to validation ground truth images')
    parser.add_argument('--pred-img', default=None, metavar='N',
                    help='Path to image of prediction (default: None)')
    parser.add_argument('--checkpoint', default=None, metavar='N',
                    help='Path of the checkpoint file (default: None)')
    parser.add_argument('--cfg-file', required= True,
                    help='CSV file path for training images and labels')
    return parser

def ArgsParserClass():
    parser = argparse.ArgumentParser(description='Transparent Camera Classification Pytorch')

    parser.add_argument('--epochs', type=int, default=40, metavar='N',
                    help='number of epochs to train (default: 40)')
    parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate (default: 0.01)')
    parser.add_argument('--batch-size', type=int, default=12, metavar='B',
                    help='batch size (default: 12)')
    parser.add_argument('--log-interval', type=int, default=500, metavar='N',
                    help='how many batches to wait before logging training status')
    parser.add_argument('--resize', required= True, type=int, default=None, 
                    help='dimensions of both height and width to be resized')
    parser.add_argument('--cfg-file', required= True,
                    help='CSV file path for training images and labels')
    parser.add_argument('--train-csv', required= True,
                    help='CSV file path for training images and labels')
    parser.add_argument('--val-csv', required= True,
                    help='CSV file path for testing images and labels')
    parser.add_argument('--root-dir', required= True,
                    help='root directory of both the train and test folders')
    parser.add_argument('--checkpoint', default=None, metavar='N',
                    help='Path of the checkpoint file (default: None)')
    return parser