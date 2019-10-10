a = imread('DIP_2019_A1/bg.jpg');
b = imread('DIP_2019_A1/fg.jpg');

out = chroma_key(b,a,[0 255 0]);
figure,
imshow(out);