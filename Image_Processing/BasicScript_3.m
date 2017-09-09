clc; clear; close all;

fileName = 'Galesnjak.jpg';

sz = size(fileName);

img = imread(fileName);

grayImg = rgb2gray(img);

imshow(grayImg);

imwrite(grayImg, 'grayImage.png', 'png');

figure, imhist(grayImg);

image = double(img);
RedB = image(:, :, 1); RedB = uint8(RedB); figure, imagesc(RedB);
GreenB = image(:, :, 2); GreenB = uint8(GreenB); figure, imagesc(GreenB);
BlueB = image(:, :, 3); BlueB = uint8(BlueB); figure, imagesc(BlueB);

[yRed, x] = imhist(RedB);
[yGreen, x] = imhist(GreenB);
[yBlue, x] = imhist(BlueB);

plot(x, yRed, 'Red', x, yGreen, 'Green', x, yBlue, 'Blue');
