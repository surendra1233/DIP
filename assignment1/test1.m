data =  imread('DIP_2019_A1/fg.jpg');
k = 2;
ind = kmeans(data,k);
% myColors = zeros(size(data, 1), 3); % List of rgb colors for every data point.
% rowsToSetBlue = ind == 3;
% rowsToSetRed = ind == 1;
% rowsToSetGreen = ind == 2;
% rowsToSetY = ind == 4;
% rowsToSetGl = ind == 5;
% for i = 1:size(data,1)
%     if rowsToSetRed(i)
%         myColors(i,:) = [1,0,0];
%     elseif rowsToSetGreen(i)
%         myColors(i,:) = [0,1,0];
%     elseif rowsToSetBlue(i)
%         myColors(i,:) = [0,0,1];
%     elseif rowsToSetY(i)
%         myColors(i,:) = [1,1,0];
%     elseif rowsToSetGl(i)
%             myColors(i,:) = [0,1,1];
%     end
% end
% scatter(data(:,1),data(:,2),3,myColors);