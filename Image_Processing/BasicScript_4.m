clc; clear; close all;

fileName = 'Galesnjak.jpg';

img = imread(fileName);
gray = rgb2gray(img);

adjImg = imadjust(gray);
imshow(adjImg);

adjImg = imadjust(gray, [0.3, 0.7], []); 
%adjImg = imadjust(gray, [0.3, 0.7], []);
figure, imshow(adjImg);