clc; close all;

fileName = 'Galesnjak.jpg';
   
img = imread(fileName);

imshow(fileName);

figure, imagesc(img(:,:,1));
title('Red');

figure, imagesc(img(:,:,2));
title('Green');

figure, imagesc(img(:,:,3));
title('Blue');

