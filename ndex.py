import argparse
import pytsk3
import hashlib
import os


def extract_information(args):
    # Open the disk image file
    img = pytsk3.Img_File(args.image)

    # Create a TSK_FS_Info object to access the file system
    fs_info = pytsk3.FS_Info(img)

    # Get the root directory of the file system
    root_dir = fs_info.root_dir

    # Traverse the file system and extract information about each file
    for entry in root_dir:
        # Get information about the file
        file_info = entry.info
        file_type = file_info.type
        file_size = file_info.size
        file_name = entry.name.name.decode('utf-8')
        file_path = entry.path.decode('utf-8')
        file_hash = hashlib.sha256(entry.read_random(0, file_size)).hexdigest()

        # Write the information to the output file
        if args.output:
            with open(args.output, 'a') as f:
                f.write(f'{file_path},{file_type},{file_size},{file_hash}\n')
        else:
            # Print the information to the console with color formatting
            print('\033[95mN\033[0m\033[97mDex\033[0m')
            print(f'Path: {file_path}')
            print(f'Type: {file_type}')
            print(f'Size: {file_size}')
            print(f'Hash: {file_hash}')
            print('-' * 80)


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='\033[95mN\033[0m\033[97mDex\033[0m - Disk Analysis Tool')
    parser.add_argument('image', help='Path to disk image file')
    parser.add_argument('--output', help='Path to output file')
    args = parser.parse_args()

    # Extract information from disk image
    extract_information(args)
