train_filename = "train.txt"
val_filename = "val.txt"
trainval_filename = "trainval.txt"
test_filename = "test.txt"

test_set = set()
val_set = set()
train_set = set()

for i in range(877):
    id = f"road{i}"
    if i % 4 == 0:
        test_set.add(id)
    elif i % 4 == 1:
        val_set.add(id)
    else:
        train_set.add(id)

with open(train_filename, 'w') as f:
    for id in train_set:
        f.write(f"{id}\n")

with open(val_filename, 'w') as f:
    for id in val_set:
        f.write(f"{id}\n")

with open(trainval_filename, 'w') as f:
    for id in train_set:
        f.write(f"{id}\n")
    for id in val_set:
        f.write(f"{id}\n")
    
with open(test_filename, 'w') as f:
    for id in test_set:
        f.write(f"{id}\n")