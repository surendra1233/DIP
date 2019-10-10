function out = chroma_key(fg,bg1,col)
    bg = imresize(bg1,[size(fg,1) size(fg,2)]);
    out = fg;
    s = size(fg);
    for i = 1:s(1)
        for j = 1:s(2)
            temp = [out(i,j,1) - col(1) (out(i,j,2) - col(2)) out(i,j,3) - col(3)];
            su = [out(i,j,1) out(i,j,2) out(i,j,3)];
            temp = abs(temp);
            if sum(temp) <=70 && sum(su)>150
                out(i,j,:) = bg(i,j,:);
            end
        end
    end
    
   % out(:,:,1) = medfilt2(out(:,:,1));
    %out(:,:,2) = medfilt2(out(:,:,2));
    %out(:,:,3) = medfilt2(out(:,:,3));
end