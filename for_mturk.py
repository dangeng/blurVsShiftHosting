import os
from pathlib import Path
from shutil import copyfile

blur_path = Path('blurs')
shift_path = Path('shifts')

blurs = sorted(os.listdir(blur_path))
shifts = sorted(os.listdir(shift_path))

# shifts go to `gt`!
global_idx = 0
for blur_name in blurs:
    for shift_name in shifts:
        src_path_1 = blur_path / blur_name
        src_path_2 = shift_path / shift_name

        dst_path_1 = Path('for_mturk/blur') / f'{global_idx:03d}.png'
        dst_path_2 = Path('for_mturk/gt') / f'{global_idx:03d}.png'

        copyfile(src_path_1, dst_path_1)
        copyfile(src_path_2, dst_path_2)

        global_idx += 1
