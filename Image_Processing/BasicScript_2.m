clc; close all; clear;

fileName = 'SIP_4.jpg';

imshow(fileName);

img = imread(fileName);

redImg = double(img);

redImg(:,:,1) = 4 * redImg(:,:,1);

redImg = uint8(redImg);

figure, imshow(redImg);

imwrite(redImg, 'redEnh4Img.png', 'png');

