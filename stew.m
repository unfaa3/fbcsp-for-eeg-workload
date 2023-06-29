% 初始化三维数组
EEGsample = zeros(48, 14, 19200);

% 读取整个评分文件
all_ratings = load('D:/2023/py_bath/workload/data_set/STEW_Dataset/ratings.txt');

% 仅保留第三列的评分
substate = all_ratings(:, 3);

% 遍历所有的主题
for subject = 1:48
    % 根据你的命名规则，生成文件名
    if subject == 5 || subject == 24 || subject == 42
        continue
    end

    filename_hi = sprintf('D:/2023/py_bath/workload/data_set/STEW_Dataset/sub%02d_hi.txt', subject);

    % 读取数据
    data_hi = load(filename_hi);

     % 将数据转换为double类型
    data_hi = double(data_hi);

    % 将数据转置
    data_hi = data_hi';
    
    % 填充数据到对应的位置
    EEGsample(subject,:,1:size(data_hi,2)) = data_hi;
end

% 删除subject为5,24和42的数据
EEGsample([5,24,42],:,:) = [];

% 创建一个从1到45的序列
subindex = 1:45;
subindex = subindex';

% 寻找allData中所有为0的元素
zero_indices = (EEGsample == 0);

% 将所有为0的元素改为一个新的值，例如改为-1
EEGsample(zero_indices) = 4.0333300e+03;

num_zeros = sum(sum(sum(zero_indices)));

B = any(EEGsample(:) == 0);

% 将 substate 中的 4, 5, 6 转换为 1
substate(substate == 4 | substate == 5 | substate == 6) = 1;

% 将 substate 中的 7, 8, 9 转换为 2
substate(substate == 7 | substate == 8 | substate == 9) = 2;
% 保存数据
save('stew_dataset.mat', 'EEGsample', 'substate', 'subindex');
