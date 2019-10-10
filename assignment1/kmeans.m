function ind = kmeans(data,k)
    randidx = randperm(size(data,1));
    means = data(randidx(1:k),:);
    [s,cols] = size(data);
    %ind = zeros(s,1);
    indices = 0;
    while(indices<100)
        %assigning the means
        dists = pdist3(data,means);
        [~,ind] = min(dists');
        ind = ind';
        %recalculating the value of means
        means = zeros(k,cols);
        count = zeros(k,1);
        for j = 1:s 
            means(ind(j)) = means(ind(j)) + data(j);
            count(ind(j)) = count(ind(j)) + 1;
        end
        means = means./count;
        indices = indices +1;
    end
end